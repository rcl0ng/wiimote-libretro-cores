import ctypes as C,json
from pathlib import Path
import argparse
from PIL import Image
BASE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser()
ap.add_argument('--core',required=True)
ap.add_argument('--rom',required=True)
args=ap.parse_args()
lib=C.CDLL(str(Path(args.core).resolve()))
Env=C.CFUNCTYPE(C.c_bool,C.c_uint,C.c_void_p)
Poll=C.CFUNCTYPE(None)
State=C.CFUNCTYPE(C.c_int16,C.c_uint,C.c_uint,C.c_uint,C.c_uint)
Video=C.CFUNCTYPE(None,C.c_void_p,C.c_uint,C.c_uint,C.c_size_t)
Audio=C.CFUNCTYPE(None,C.c_int16,C.c_int16)
Batch=C.CFUNCTYPE(C.c_size_t,C.c_void_p,C.c_size_t)
class Var(C.Structure):_fields_=[('key',C.c_char_p),('value',C.c_char_p)]
class Val(C.Structure):_fields_=[('value',C.c_char_p),('label',C.c_char_p)]
class Opt(C.Structure):_fields_=[('key',C.c_char_p),('desc',C.c_char_p),('desc_cat',C.c_char_p),('info',C.c_char_p),('info_cat',C.c_char_p),('cat',C.c_char_p),('values',Val*128),('default',C.c_char_p)]
class Opts(C.Structure):_fields_=[('categories',C.c_void_p),('defs',C.POINTER(Opt))]
class Controller(C.Structure):_fields_=[('desc',C.c_char_p),('id',C.c_uint)]
class Controllers(C.Structure):_fields_=[('types',C.POINTER(Controller)),('count',C.c_uint)]
class Game(C.Structure):_fields_=[('path',C.c_char_p),('data',C.c_void_p),('size',C.c_size_t),('meta',C.c_char_p)]
values={};changed=False;pixel=1;frame=0;buttons=[set(),set()];axes=[0,0];last_image=None
folder=C.create_string_buffer(str(BASE).encode()); devices=[]
@Env
def env(cmd,p):
 global pixel,changed
 if cmd in (9,30,31):C.cast(p,C.POINTER(C.c_char_p))[0]=C.cast(folder,C.c_char_p);return True
 if cmd==52:C.cast(p,C.POINTER(C.c_uint))[0]=2;return True
 if cmd==67:
  ds=C.cast(p,C.POINTER(Opts)).contents.defs;i=0
  while ds[i].key:
   if ds[i].default:values.setdefault(ds[i].key,ds[i].default)
   i+=1
  return True
 if cmd==15:
  v=C.cast(p,C.POINTER(Var)).contents
  v.value=values.get(v.key)
  return bool(v.value)
 if cmd==17:C.cast(p,C.POINTER(C.c_bool))[0]=changed;changed=False;return True
 if cmd==10:pixel=C.cast(p,C.POINTER(C.c_uint))[0];return True
 if cmd==35:
  a=C.cast(p,C.POINTER(Controllers));i=0
  while a[i].count:
   devices.append([(a[i].types[j].desc.decode(),a[i].types[j].id) for j in range(a[i].count)]);i+=1
  return True
 if cmd in (3,51|0x10000):return True
 if cmd==39:C.cast(p,C.POINTER(C.c_uint))[0]=0;return True
 if cmd in (18,32,37,36|0x10000,68,69):return True
 return False
@Poll
def poll():pass
@State
def state(port,device,index,id):
 if port>=2:return 0
 if device==1:return sum(1<<i for i in buttons[port]) if id==256 else int(id in buttons[port])
 if device==5 and index==0:return axes[port] if id==0 else 0
 return 0
@Video
def video(p,w,h,pitch):
 global last_image
 if p:
  b=C.string_at(p,h*pitch)
  if pixel==1:last_image=Image.frombytes('RGB',(w,h),b,'raw','BGRX',pitch)
@Audio
def audio(l,r):pass
@Batch
def batch(p,n):return n
for n,t,cb in [('environment',Env,env),('input_poll',Poll,poll),('input_state',State,state),('video_refresh',Video,video),('audio_sample',Audio,audio),('audio_sample_batch',Batch,batch)]:
 f=getattr(lib,'retro_set_'+n);f.argtypes=[t];f(cb)
lib.retro_load_game.argtypes=[C.POINTER(Game)];lib.retro_load_game.restype=C.c_bool
lib.retro_get_memory_data.argtypes=[C.c_uint];lib.retro_get_memory_data.restype=C.c_void_p
lib.retro_get_memory_size.argtypes=[C.c_uint];lib.retro_get_memory_size.restype=C.c_size_t
lib.retro_init();lib.retro_set_controller_port_device(0,5377);lib.retro_set_controller_port_device(1,5377)
g=Game(str(Path(args.rom).resolve()).encode(),None,0,None)
assert lib.retro_load_game(C.byref(g)), 'ROM load failed'
lib.retro_set_controller_port_device(0,5377);lib.retro_set_controller_port_device(1,5377)
assert any(('Wiimote IR Ship + Buttons',5377) in d for d in devices)
assert values[b'galaga-ir-double-fighter']==b'disabled'
assert values[b'galaga-ir-unlimited-lives']==b'disabled' and values[b'galaga-ir-invincibility']==b'disabled'
ptr=lib.retro_get_memory_data(2);size=lib.retro_get_memory_size(2)
print('RAM size',size,flush=True);assert ptr and size>=0x1400
ram=(C.c_uint8*size).from_address(ptr)
def off(a):
 if 0x8000<=a<0x8800:return a-0x8000
 if 0x8800<=a<0x8c00:return a-0x8800+0x800
 if 0x9000<=a<0x9400:return a-0x9000+0xc00
 if 0x9800<=a<0x9c00:return a-0x9800+0x1000
 raise ValueError(hex(a))
def read(a):return ram[off(a)]
def write(a,v):ram[off(a)]=v
samples=[]
def run(n):
 global frame
 for _ in range(n):lib.retro_run();frame+=1
 def r(a):return read(a)
 samples.append(dict(frame=frame,state=r(0x9201),task=r(0x9014),x=r(0x9362),video_x=r(0x93e2),reserves=r(0x9820),player=r(0x9840),double=r(0x9827)))
def shot(name):
 if last_image:last_image.save(BASE/(name+'.png'))
def option(k,v):
 global changed
 values[k.encode()]=v.encode();changed=True
run(1200);shot('boot');print(samples[-1],flush=True)
buttons[0]={2};run(2);buttons[0]=set();run(30)
buttons[0]={3};run(2);buttons[0]=set();run(900);shot('started');print(samples[-1],flush=True)
option('galaga-ir-invincibility','enabled');run(1)
for x in [-32768,0,32767,-16000,16000]:
 axes[0]=x;run(2);print('axis',x,samples[-1],flush=True)
shot('right')
(BASE/'first-test.json').write_text(json.dumps(samples,indent=2))
# Exact positions, single-frame changes, steady hold and independent input.
for x in [-32768, -16384, 0, 16384, 32767]:
 axes[0]=x;run(1)
 expected=18+((x+32768)*207+32767)//65535
 assert read(0x9362)==expected,(x,expected,read(0x9362))
 run(1);assert read(0x93e2)==expected
print('PASS: exact endpoints and intermediate targets applied within one frame',flush=True)
axes[0]=0;axes[1]=32767;run(1)
assert read(0x9362)==122
write(0x9840,1);run(1);assert read(0x9362)==225
axes[0]=-32768;run(1);assert read(0x9362)==225
write(0x9840,0);run(1);assert read(0x9362)==18
print('PASS: active-player routing; stationary P2 does not follow moving P1',flush=True)
write(0x9840,1);before=read(0x9846)+256*read(0x9847)
buttons[0]={0};buttons[1]=set();run(12)
assert read(0x9846)+256*read(0x9847)==before
buttons[0]=set();buttons[1]={0};run(12);buttons[1]=set()
assert read(0x9846)+256*read(0x9847)>before
write(0x9840,0)
print('PASS: P2 uses its own trigger on an upright cabinet',flush=True)
# Native zero-position guard must keep an absent ship absent during respawn.
old=read(0x9362);write(0x9362,0);run(1);assert read(0x9362)==0;write(0x9362,old)
print('PASS: inactive ship/respawn zero-position guard',flush=True)
write(0x9827,1);axes[0]=32767;run(1)
assert read(0x9362)==209 and read(0x9360)==224
write(0x9827,0);axes[0]=0;run(1)
print('PASS: double-fighter right limit and native 15-pixel spacing',flush=True)
buttons[0]={0};before=read(0x9846)+256*read(0x9847);run(12);buttons[0]=set()
after=read(0x9846)+256*read(0x9847)
assert after>before,(before,after)
print('PASS: B trigger increments native shot counter',flush=True)
# Double-fighter option must initialize native graphics, position and shot logic.
write(0x9360,0);write(0x9827,0);option('galaga-ir-double-fighter','enabled');run(2)
assert read(0x9827)==1 and read(0x8b60)==6 and read(0x8b61)==9
assert read(0x9360)==read(0x9362)+15
assert read(0x9361)==read(0x9363) and read(0x9b61)==read(0x9b63)
buttons[0]={0};run(12);buttons[0]=set();shot('double-fighter')
option('galaga-ir-double-fighter','disabled');run(1);assert read(0x9827)==1
print('PASS: Double Fighter initializes real paired ships; disabling stops granting without erasing the pair',flush=True)
# Restore the single-ship fixture for independent survival comparisons.
write(0x9360,0);write(0x9827,0)
# Save a real active-game snapshot and compare cheat-on/off simulations.
lib.retro_serialize_size.restype=C.c_size_t
lib.retro_serialize.argtypes=[C.c_void_p,C.c_size_t];lib.retro_serialize.restype=C.c_bool
lib.retro_unserialize.argtypes=[C.c_void_p,C.c_size_t];lib.retro_unserialize.restype=C.c_bool
length=lib.retro_serialize_size();save=C.create_string_buffer(length)
assert lib.retro_serialize(save,length)
def restore():assert lib.retro_unserialize(save,length)
def survival(lives,invincible,n=12000):
 restore();option('galaga-ir-unlimited-lives',lives);option('galaga-ir-invincibility',invincible)
 axes[0]=0;buttons[0]=set();dead=0;events=[];previous=read(0x9014);res=set();last=read(0x9820)
 for _ in range(n):
  run(1);now=read(0x9014)
  if previous and not now:
   dead+=1;events.append(dict(frame=frame,capture_task=read(0x901c),capture_status=read(0x928b),collision=read(0x99bf),state=read(0x9201)))
  previous=now;res.add(read(0x9820))
 return dict(deaths_or_capture=dead,events=events,reserves=sorted(res),state=read(0x9201))
normal=survival('disabled','disabled')
protected=survival('disabled','enabled')
endless=survival('enabled','disabled')
print('Normal play:',normal,flush=True)
print('Invincibility:',protected,flush=True)
print('Unlimited lives:',endless,flush=True)
assert normal['deaths_or_capture']>0
assert protected['state']==3 and all(e['capture_task'] for e in protected['events']),protected
assert endless['deaths_or_capture']>0 and endless['state']==3 and 255 not in endless['reserves'],endless
print('PASS: natural deaths occur normally; invincibility survives while allowing capture; unlimited lives keeps normal deaths/respawns playable',flush=True)
restore();option('galaga-ir-unlimited-lives','disabled');option('galaga-ir-invincibility','disabled');run(1)
lib.retro_set_controller_port_device(0,5);axes[0]=0;run(1);old=read(0x9362)
axes[0]=32767;run(1);assert read(0x9362)-old<=2
print('PASS: native Classic device restores original speed-limited movement',flush=True)
(BASE/'test-results.json').write_text(json.dumps({'normal':normal,'invincibility':protected,'unlimited':endless},indent=2))
lib.retro_unload_game();lib.retro_deinit()
print('PASS: load, advertised custom device, default cheats disabled, start and axis smoke test',flush=True)
