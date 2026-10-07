name=rom.stem
if name=='arkanoid':
 run(4000);run(10,pad=1<<2);run(30);run(10,pad=1<<3);run(650)
elif name=='missile':
 run(300);run(30,pad=1<<2);run(30);run(30,pad=1<<3);run(240)
else:
 run(600);run(30,pad=1<<2);run(30);run(30,pad=1<<3);run(120);run(20,pad=1);run(40)
save('test_'+name)
for k,(x,y) in enumerate([(0,0),(24000,18000),(-24000,-18000),(30000,-18000),(-30000,18000),(0,0)]):
 load('test_'+name)
 axes[0]=[x,y];run(80,pad=(1 if name in ('centiped','milliped') else 0))
 if name=='missile':pos=tuple(ram[:2]);target=(max(8,min(247,(x+32768)*256//65536)),max(53,min(214,25+(y+32768)*231//65536)))
 elif name=='arkanoid':
  print('ARKCOORD',int(ram[0x445]),int(ram[0x447]),int(ram[0x47e]),int(ram[0x482]))
  pos=(int(ram[0x47e])-4,);target=(38+(x+32768)*180//65536,)
 else:
  cent=name=='centiped';pos=(int(ram[0x63 if cent else 0x2f]),int(ram[0x73 if cent else 0x3f]));target=(244-(x+32768)*234//65536,max(8,min(48,48-(y+32768)*41//65536)))
 Image.fromarray(frame).rotate(90,expand=True).resize((480,512)).save(root/('normal_'+name+'_'+str(k)+'.png'))
 print('POINT',name,k,'actual',pos,'target',target,flush=True)
 if not all(abs(a-b)<=1 for a,b in zip(pos,target)):
  assert name=='milliped',(name,k,pos,target)
  save('blocked_'+name)
  lib.retro_set_controller_port_device(0,773)
  dx=8 if pos[0]>target[0] else -8
  run(10,dx=dx,pad=1)
  native=(int(ram[0x2f]),int(ram[0x3f]))
  print('NATIVE_COLLISION',pos,native,flush=True)
  assert abs(native[0]-pos[0])<=3 and native[1]==pos[1],(name,k,'not a native collision',pos,native)
  lib.retro_set_controller_port_device(0,1285)
  load('blocked_'+name)
 shot('v2_'+name+'_'+str(k))
print('PASS',name,flush=True)
