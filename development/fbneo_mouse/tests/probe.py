import ctypes as C,sys,pathlib,json,os
import numpy as np
from PIL import Image
root=pathlib.Path(__file__).resolve().parent
lib=C.CDLL(str(root.parent/'fbneo-source/src/burner/libretro/fbneo_mouse_libretro.so'))
class Game(C.Structure):_fields_=[('path',C.c_char_p),('data',C.c_void_p),('size',C.c_size_t),('meta',C.c_char_p)]
class Var(C.Structure):_fields_=[('key',C.c_char_p),('value',C.c_char_p)]
ENV=C.CFUNCTYPE(C.c_bool,C.c_uint,C.c_void_p);VIDEO=C.CFUNCTYPE(None,C.c_void_p,C.c_uint,C.c_uint,C.c_size_t);AUDIO=C.CFUNCTYPE(None,C.c_int16,C.c_int16);BATCH=C.CFUNCTYPE(C.c_size_t,C.c_void_p,C.c_size_t);POLL=C.CFUNCTYPE(None);INPUT=C.CFUNCTYPE(C.c_int16,C.c_uint,C.c_uint,C.c_uint,C.c_uint)
LOG=C.CFUNCTYPE(None,C.c_int,C.c_char_p,C.c_size_t,C.c_size_t,C.c_size_t)
@LOG
def logger(level,msg,a,b,c):
 if b"is required" in msg:print("MISSING",a,C.string_at(b).decode(),hex(c),flush=True)
 else:print("LOG",level,msg.decode(errors="replace"),flush=True)
opts={}
opts.update({k.encode():v.encode() for k,v in json.loads(os.environ.get('PROBE_OPTIONS','{}')).items()})
root_bytes=str(root).encode()
save_directory=pathlib.Path(os.environ.get("PROBE_SAVE_DIR",str(root)));save_directory.mkdir(parents=True,exist_ok=True)
save_bytes=str(save_directory).encode()
fmt=2;frame=None;buttons=[0,0];mouse=[[0,0,0,0],[0,0,0,0]];axes=[[0,0],[0,0]]
@ENV
def env(cmd,data):
 global fmt
 if cmd==27:C.cast(data,C.POINTER(C.c_void_p))[0]=C.cast(logger,C.c_void_p).value;return True
 if cmd==11:
  class Desc(C.Structure):_fields_=[('port',C.c_uint),('device',C.c_uint),('index',C.c_uint),('id',C.c_uint),('description',C.c_char_p)]
  ds=C.cast(data,C.POINTER(Desc));i=0
  while ds[i].description:
   if True:print('BIND',ds[i].port,ds[i].device,ds[i].id,ds[i].description,flush=True)
   i+=1
  return True
 if cmd==16:
  vs=C.cast(data,C.POINTER(Var));i=0
  while vs[i].key:
   default=vs[i].value.split(b'; ',1)[1].split(b'|')[0]
   opts.setdefault(vs[i].key,default);i+=1
  return True
 if cmd==15:
  v=C.cast(data,C.POINTER(Var)).contents;v.value=opts.get(v.key);return bool(v.value)
 if cmd==17:C.cast(data,C.POINTER(C.c_bool))[0]=False;return True
 if cmd==10:fmt=C.cast(data,C.POINTER(C.c_int))[0];return True
 if cmd in (9,31):C.cast(data,C.POINTER(C.c_char_p))[0]=save_bytes if cmd==31 else root_bytes;return True
 if cmd in (16,18,11,35,37):return True
 return False
@VIDEO
def video(data,w,h,pitch):
 global frame
 if not data or data==C.c_void_p(-1).value:return
 if fmt==1:
  a=np.frombuffer(C.string_at(data,h*pitch),dtype=np.uint32).reshape(h,pitch//4)[:,:w];frame=np.stack(((a>>16)&255,(a>>8)&255,a&255),2).astype('uint8')
 else:
  a=np.frombuffer(C.string_at(data,h*pitch),dtype=np.uint16).reshape(h,pitch//2)[:,:w]
  frame=np.stack((((a>>(11 if fmt==2 else 10))&31)*255//31,((a>>5)&(63 if fmt==2 else 31))*255//(63 if fmt==2 else 31),(a&31)*255//31),2).astype('uint8')
@AUDIO
def audio(a,b):pass
@BATCH
def batch(data,n):return n
@POLL
def poll():pass
@INPUT
def inp(port,device,index,id):
 if port>1:return 0
 if device==1:
  v=(buttons[port]>>id)&1
  if False:print("PRESSED",port,id,flush=True)
  return v
 if device==2:return mouse[port][id] if id<4 else 0
 if device==5:return axes[port][id] if index==0 and id<2 else 0
 return 0
for name,cb in [('environment',env),('video_refresh',video),('audio_sample',audio),('audio_sample_batch',batch),('input_poll',poll),('input_state',inp)]:getattr(lib,'retro_set_'+name)(cb)
lib.retro_init()
rom=pathlib.Path(sys.argv[1]);buf=C.create_string_buffer(rom.read_bytes());game=Game(str(rom).encode(),C.cast(buf,C.c_void_p),len(buf)-1,None)
lib.retro_load_game.argtypes=[C.POINTER(Game)];lib.retro_load_game.restype=C.c_bool
assert lib.retro_load_game(C.byref(game))
devices=json.loads(os.environ.get('PROBE_DEVICES','[773,1]'))
for port,device in enumerate(devices):lib.retro_set_controller_port_device(port,device)
lib.retro_get_memory_data.argtypes=[C.c_uint];lib.retro_get_memory_data.restype=C.c_void_p
lib.retro_get_memory_size.argtypes=[C.c_uint];lib.retro_get_memory_size.restype=C.c_size_t
lib.retro_serialize_size.restype=C.c_size_t
lib.retro_serialize.argtypes=[C.c_void_p,C.c_size_t];lib.retro_serialize.restype=C.c_bool
lib.retro_unserialize.argtypes=[C.c_void_p,C.c_size_t];lib.retro_unserialize.restype=C.c_bool
print("RAM",lib.retro_get_memory_size(2),flush=True)
ram=np.ctypeslib.as_array((C.c_uint8*lib.retro_get_memory_size(2)).from_address(lib.retro_get_memory_data(2))) if lib.retro_get_memory_size(2) else np.array([],dtype='uint8')
def run(n=1,dx=0,dy=0,left=0,right=0,pad=0,port=0):
 mouse[port]=[dx,dy,left,right];buttons[port]=pad
 for _ in range(n):lib.retro_run()
 mouse[port]=[0,0,0,0];buttons[port]=0

def aim(x,y,n=5,port=0):
 import math
 axes[port]=[min(32767,math.ceil(x*65535/255)-32768),min(32767,math.ceil(y*65535/223)-32768)]
 run(n,port=port)
def click(port=0):
 run(2,pad=1,port=port);run(2,port=port)
def shot(name):Image.fromarray(frame).resize((512,448)).save(root/(name+'.png'))
def save(name):
 b=C.create_string_buffer(lib.retro_serialize_size());assert lib.retro_serialize(b,len(b));(root/(name+'.state')).write_bytes(b.raw)
def load(name):
 b=C.create_string_buffer((root/(name+'.state')).read_bytes());assert lib.retro_unserialize(b,len(b)-1)
def dump(name):(root/(name+'.ram')).write_bytes(ram.tobytes())
exec(pathlib.Path(sys.argv[2]).read_text())
lib.retro_unload_game();lib.retro_deinit()
