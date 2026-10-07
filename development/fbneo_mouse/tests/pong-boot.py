run(1800);shot('pong-attract')
for _ in range(4):run(10,pad=4);run(30)
run(10,pad=8);run(100);shot('pong-start');dump('pong-start')
run(10,pad=8,port=1);run(200);shot('pong-two');dump('pong-two');save('pong-live')
