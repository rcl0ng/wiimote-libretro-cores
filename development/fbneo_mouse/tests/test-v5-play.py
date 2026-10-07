load('pong-game');run(650);shot('pong-active')
def w(i):return int(ram[i])|int(ram[i+1])<<8
for k in range(1500):
 by=w(0x14);y=max(20,min(206,by-16));raw=max(-32768,min(32767,((y-20)*65536+186)//187-32768))
 axes[0]=[0,raw];axes[1]=[0,raw];run(1)
 if k%150==0:print('PLAY',k,'ball_y',by,'scores',w(8),w(10),'side',ram[4],ram[5],flush=True)
shot('pong-rally');save('pong-rally');print('PASS native gameplay ran 1500 frames',flush=True)
