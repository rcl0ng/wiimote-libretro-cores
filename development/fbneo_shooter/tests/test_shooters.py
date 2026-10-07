import ctypes as C,json
from pathlib import Path
from PIL import Image
BASE=Path(__file__).resolve().parent
import argparse
ap=argparse.ArgumentParser()
ap.add_argument('--game',required=True,choices=['galaxian','invaders','galaga3','galaga88'])
ap.add_argument('--core',required=True)
ap.add_argument('--rom',required=True)
args=ap.parse_args()
NAME=args.game
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
class Category(C.Structure):_fields_=[("key",C.c_char_p),("desc",C.c_char_p),("info",C.c_char_p)]
class Opts(C.Structure):_fields_=[('categories',C.c_void_p),('defs',C.POINTER(Opt))]
class Controller(C.Structure):_fields_=[('desc',C.c_char_p),('id',C.c_uint)]
class Controllers(C.Structure):_fields_=[('types',C.POINTER(Controller)),('count',C.c_uint)]
class Game(C.Structure):_fields_=[('path',C.c_char_p),('data',C.c_void_p),('size',C.c_size_t),('meta',C.c_char_p)]
choices={};categories={};cheat_defs={};values={};changed=False;pixel=1;frame=0;buttons=[set(),set()];axes=[0,0];ys=[0,0];last_image=None
folder=C.create_string_buffer(str(BASE).encode()); devices=[]
@Env
def env(cmd,p):
 global pixel,changed
 if cmd in (9,30,31):C.cast(p,C.POINTER(C.c_char_p))[0]=C.cast(folder,C.c_char_p);return True
 if cmd==52:C.cast(p,C.POINTER(C.c_uint))[0]=2;return True
 if cmd==67:
  opts=C.cast(p,C.POINTER(Opts)).contents
  cats=C.cast(opts.categories,C.POINTER(Category));j=0
  while cats[j].key:
   categories[cats[j].key]=cats[j].desc;j+=1
  ds=opts.defs;i=0
  while ds[i].key:
   if ds[i].default:values.setdefault(ds[i].key,ds[i].default)
   if ds[i].key.startswith(b'galaga-ir-'):
    cheat_defs[ds[i].key]=(ds[i].desc,ds[i].cat)
    choices[ds[i].key]=[v.value for v in ds[i].values if v.value]
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
 if device==5 and index==0:return axes[port] if id==0 else ys[port]
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
lib.retro_init();lib.retro_set_controller_port_device(0,1)
g=Game(str(Path(args.rom).resolve()).encode(),None,0,None)
assert lib.retro_load_game(C.byref(g))
lib.retro_set_controller_port_device(0,1)
ptr=lib.retro_get_memory_data(2);size=lib.retro_get_memory_size(2)
ram=(C.c_uint8*size).from_address(ptr)
def snap(tag):
 (BASE/(NAME+'-'+tag+'.ram')).write_bytes(bytes(ram))
 if last_image:last_image.save(BASE/(NAME+'-'+tag+'.png'))
def run(n):
 global frame
 for _ in range(n):
  lib.retro_run();frame+=1

def option(k,v):
 global changed
 values[k.encode()]=v.encode();changed=True
lib.retro_set_controller_port_device(0,5377)
lib.retro_set_controller_port_device(1,5377)
assert categories[b'cheat']==b'Cheats'
assert all(v[1]==b'cheat' for v in cheat_defs.values())
assert cheat_defs[b'galaga-ir-unlimited-lives'][0]==b'Infinite Lives'
print('PASS Cheats submenu and labels',flush=True)
option('galaga-ir-invincibility','enabled');option('galaga-ir-unlimited-lives','enabled')
run(1200)
buttons[0]={2};run(3);buttons[0]=set();run(30)
buttons[0]={3};run(3);buttons[0]=set()
if NAME=='galaga88':
 run(120);buttons[0]={0};run(3);buttons[0]=set();run(1450)
else:run(900)
positions={'galaxian':0x202,'invaders':0x1b,'galaga3':0x1600,'galaga88':0x9051}
for x in [-32768,0,32767,-20000,20000,0]:
 axes[0]=x;run(4)
 expected={'galaxian':233-((x+32768)*211+32767)//65535,'invaders':48+((x+32768)*169+32767)//65535,'galaga3':13+((x+32768)*205+32767)//65535,'galaga88':33+((x+32768)*191+32767)//65535}[NAME]
 assert ram[positions[NAME]]==expected,(NAME,x,ram[positions[NAME]],expected)
 print('POSITION',x,ram[positions[NAME]], 'Y',ram[0x1601] if NAME=='galaga3' else '-',flush=True)
 snap('ir-'+str(x))
if NAME=='galaga3':
 for y in [-32768,0,32767]:
  ys[0]=y;run(4);print('Y',y,ram[0x1601],ram[0x1e01],flush=True);snap('ir-y'+str(y))
run(30);assert ram[positions[NAME]]==expected,'Position drift while holding still'
print('PASS absolute movement and held-position stability',flush=True)
player_addr={'galaxian':0xd,'invaders':0x67,'galaga3':0x102d,'galaga88':0x902f}[NAME]
lib.retro_serialize_size.restype=C.c_size_t
lib.retro_serialize.argtypes=[C.c_void_p,C.c_size_t];lib.retro_serialize.restype=C.c_bool
lib.retro_unserialize.argtypes=[C.c_void_p,C.c_size_t];lib.retro_unserialize.restype=C.c_bool
save_size=lib.retro_serialize_size();save=C.create_string_buffer(save_size)
assert lib.retro_serialize(save,save_size)
oldplayer=ram[player_addr];ram[player_addr]=0x22 if NAME=='invaders' else 1
axes[0]=-20000;axes[1]=20000;run(4)
p2expected={'galaxian':63,'invaders':184,'galaga3':178,'galaga88':187}[NAME]
assert ram[positions[NAME]]==p2expected,(NAME,'P2 aim',ram[positions[NAME]],p2expected)
print('PASS independent P2 axis routing',flush=True)
assert lib.retro_unserialize(save,save_size);axes[0]=0;run(4)
buttons[0]={0};run(45);buttons[0]=set();snap('ir-shoot')
max_count=6 if NAME=='galaga3' else 2 if NAME=='galaga88' else 0
if max_count:
 assert choices[b'galaga-ir-double-fighter']==[b'disabled']+[str(i).encode() for i in range(1,max_count+1)]
 for count in list(range(1,max_count+1))+[1,max_count]:
  option('galaga-ir-double-fighter',str(count));run(16)
  if NAME=='galaga3':
   actual=sum(bool(ram[0x1ec3+2*i]&0x80) for i in range(6))
   assert actual==count,(count,actual)
   assert ram[0x10dc]==count,('native count',count,ram[0x10dc])
   lo,hi=ram[0x1078],ram[0x1079]
   axes[0]=-32768;run(4);assert ram[0x1600]==ram[0x1078],('left',count,ram[0x1600],ram[0x1078])
   axes[0]=32767;run(4);assert ram[0x1600]==ram[0x1079],('right',count,ram[0x1600],ram[0x1079])
   print('PASS count',count,'native X limits',lo,hi,flush=True)
  else:
   assert ram[0x9064]==count,(count,ram[0x9064])
   print('PASS extra ships',count,flush=True)
 axes[0]=0;run(4)
run(3600);snap('ir-multiple-later')
stateaddr={'galaxian':6,'invaders':0xef,'galaga3':0x102f,'galaga88':0x9035}[NAME]
alive=(1<=ram[stateaddr]<9) if NAME=='galaga3' else ram[stateaddr] == {'galaxian':1,'invaders':1,'galaga88':5}[NAME]
assert alive,('Protected game ended',NAME)
print('PASS protected gameplay remains active for 3600 frames',flush=True)
print('PASS movement, submenu and P2 routing:',NAME,flush=True)
lib.retro_unload_game();lib.retro_deinit()
