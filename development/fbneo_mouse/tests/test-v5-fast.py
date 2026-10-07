import ctypes as C
load('pong-rally');axes[0]=[0,-32768];axes[1]=[0,32767];run(15)
def state():
 b=C.create_string_buffer(lib.retro_serialize_size());assert lib.retro_serialize(b,len(b));return b.raw
a=state();axes[0]=[0,32767];axes[1]=[0,-32768];run(1);b=state()
# Identify native graphics VRAM words by the already verified corner values.
# These are LE sprite Y registers at addresses 82f0 and 8300, 32 bytes apart.
pairs=[]
for i in range(len(a)-34):
 if a[i:i+2]==bytes.fromhex('02f6') and a[i+32:i+34]==bytes.fromhex('0299'):
  if b[i:i+2]==bytes.fromhex('0299') and b[i+32:i+34]==bytes.fromhex('02f6'):pairs.append(i)
assert pairs,pairs
print('PASS both paddles swap opposite edges in one game frame',pairs,flush=True)
