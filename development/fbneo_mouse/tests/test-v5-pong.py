import re
def latest():
 rows=(save_directory/'fbneo-ir-mouse.log').read_text().splitlines()
 result={}
 for l in rows:
  m=re.match(r'PADDLE frame=(\d+) player=(\d+) target_y=(-?\d+) actual_y=(\d+)',l)
  if m:result[int(m[2])]=(int(m[3]),int(m[4]))
 return result
for k,(p1,p2) in enumerate([(-32768,32767),(32767,-32768),(0,0),(-18000,21000),(21000,-18000)]):
 load('pong-rally');axes[0]=[0,p1];axes[1]=[0,p2];run(15)
 pos=latest()
 assert all(target==actual for target,actual in pos.values()) and len(pos)==2,pos
 run(20);assert latest()==pos,(latest(),pos)
 print('PASS POINT',k,pos,flush=True)
load('pong-rally');axes[0]=[0,21000];axes[1]=[0,-18000];run(15)
lib.retro_set_controller_port_device(0,1);run(15,pad=1<<4);normal=latest()
assert normal[1][0]==-1 and normal[1][1]<173,normal
assert normal[2]==(62,62),normal
print('PASS mixed devices native P1 / IR P2',normal,flush=True)
lib.retro_set_controller_port_device(0,1285);axes[0]=[0,-32768];axes[1]=[0,32767];run(15)
assert latest()=={1:(20,20),2:(206,206)},latest()
print('PASS restore IR',latest(),flush=True)
axes[0]=[0,-18000];axes[1]=[0,21000];run(15)
lib.retro_set_controller_port_device(1,1);run(15,pad=1<<5,port=1)
assert latest()[1]==(62,62) and latest()[2][0]==-1 and latest()[2][1]>173,latest()
print('PASS mixed devices IR P1 / native P2',latest(),flush=True)
