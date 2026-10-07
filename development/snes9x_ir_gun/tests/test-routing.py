from pathlib import Path
import re,subprocess
s=Path('macs-work/snes9x-gun-source/libretro/libretro.cpp').read_text()
def function(name):
 start=s.index('static ',s.index(name)-30);a=s.index('{',start);depth=1;i=a+1
 while depth:
  depth+=(s[i]=='{')-(s[i]=='}');i+=1
 return s[start:i]
head='''#include <cstdint>
#include <cassert>
#include <cstdio>
#include "libretro.h"
#define RETRO_DEVICE_IR_MACS RETRO_DEVICE_SUBCLASS(RETRO_DEVICE_JOYPAD,23)
#define MACS_RIFLE_TRIGGER 2
#define RETRO_DEVICE_IR_SCOPE RETRO_DEVICE_SUBCLASS(RETRO_DEVICE_JOYPAD,20)
#define RETRO_DEVICE_IR_JUSTIFIER RETRO_DEVICE_SUBCLASS(RETRO_DEVICE_JOYPAD,21)
#define RETRO_DEVICE_IR_JUSTIFIER2 RETRO_DEVICE_SUBCLASS(RETRO_DEVICE_JOYPAD,22)
#define MAKE_BUTTON(p,b) (((p)<<4)|(b))
#define PAD_2 2
#define RETRO_PAD_ID_COUNT 16
#define PAD_3 3
#define BTN_POINTER 0x90
#define BTN_POINTER2 0x91
#define JUSTIFIER_TRIGGER 2
#define JUSTIFIER_START 3
#define JUSTIFIER_OFFSCREEN 4
#define SUPER_SCOPE_TRIGGER 2
#define SUPER_SCOPE_CURSOR 3
#define SUPER_SCOPE_TURBO 4
#define SUPER_SCOPE_START 5
#define SUPER_SCOPE_OFFSCREEN 6
unsigned snes_devices[8];
int g_screen_gun_width=256,g_screen_gun_height=224;
bool snes_superscope_turbo_latch=false;
int axes[2][2],pads[2],px[256],py[256];bool b[256];
int16_t input_state_cb(unsigned p,unsigned d,unsigned i,unsigned id){return d==RETRO_DEVICE_ANALOG?axes[p][id]:((pads[p]>>id)&1);}
void S9xReportPointer(int id,int x,int y){px[id]=x;py[id]=y;}
void report_button(int id,bool v){b[id]=v;}
int snes_pad_mask(int v){return v;}
void S9xSetJoypadButtons(int p,int v){}
'''
body='\n'.join(function(n) for n in ['ir_button(','ir_gun_position(','ir_justifier(','report_ir_hybrid('])
test='''
int main(){
 snes_devices[0]=RETRO_DEVICE_IR_JUSTIFIER;snes_devices[1]=RETRO_DEVICE_IR_JUSTIFIER2;
 axes[0][0]=-32768;axes[0][1]=-32768;axes[1][0]=32767;axes[1][1]=32767;
 pads[0]=1<<RETRO_DEVICE_ID_JOYPAD_B;pads[1]=1<<RETRO_DEVICE_ID_JOYPAD_A;
 assert(report_ir_hybrid());assert(px[0x90]==0&&py[0x90]==0&&px[0x91]==255&&py[0x91]==223);
 assert(b[0x22]&&!b[0x24]&&b[0x32]&&b[0x34]);
 for(int k=0;k<1000;++k){axes[0][1]=(k%2)?32767:-32768;report_ir_hybrid();assert(py[0x91]==223);}
 axes[1][1]=-32768;report_ir_hybrid();assert(py[0x91]==0);
 snes_devices[0]=RETRO_DEVICE_IR_SCOPE;pads[0]=1<<RETRO_DEVICE_ID_JOYPAD_Y;
 report_ir_hybrid();assert(b[0x24]);report_ir_hybrid();assert(!b[0x24]);
 pads[0]=0;report_ir_hybrid();pads[0]=1<<RETRO_DEVICE_ID_JOYPAD_Y;report_ir_hybrid();assert(b[0x24]);
 snes_devices[0]=RETRO_DEVICE_IR_MACS;pads[0]=1<<RETRO_DEVICE_ID_JOYPAD_B;axes[0][0]=-32768;axes[0][1]=32767;report_ir_hybrid();assert(px[0x90]==0&&py[0x90]==223&&b[0x22]);pads[0]=0;report_ir_hybrid();assert(!b[0x22]);
 puts("PASS: M.A.C.S. endpoint and trigger press/release; independent gun endpoints, 1000 held-P2 frames, per-player reload, Scope turbo rising edge");
}
'''
Path('macs-work/routing-test.cpp').write_text(head+body+test)
subprocess.run(['g++','-I','macs-work/snes9x-gun-source/libretro','macs-work/routing-test.cpp','-o','macs-work/routing-test'],check=True)
subprocess.run(['macs-work/routing-test'],check=True)
