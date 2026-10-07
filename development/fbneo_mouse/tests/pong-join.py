load('pong-live');run(600);run(10,pad=8,port=1);run(300);shot('pong-joined');save('pong-game');print('MODES',int(ram[0x75]),int(ram[0x77]),flush=True)
