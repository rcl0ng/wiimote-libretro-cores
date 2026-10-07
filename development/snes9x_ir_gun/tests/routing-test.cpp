#include <cstdint>
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
static bool ir_button(unsigned port, unsigned id)
{
    return input_state_cb(port, RETRO_DEVICE_JOYPAD, 0, id) != 0;
}
static void ir_gun_position(unsigned port, int pointer)
{
    int x = input_state_cb(port, RETRO_DEVICE_ANALOG, RETRO_DEVICE_INDEX_ANALOG_LEFT, RETRO_DEVICE_ID_ANALOG_X);
    int y = input_state_cb(port, RETRO_DEVICE_ANALOG, RETRO_DEVICE_INDEX_ANALOG_LEFT, RETRO_DEVICE_ID_ANALOG_Y);
    x = ((x + 32768) * (g_screen_gun_width - 1)) / 65535;
    y = ((y + 32768) * (g_screen_gun_height - 1)) / 65535;
    S9xReportPointer(pointer, x, y);
}
static void ir_justifier(unsigned port, int pad, int pointer)
{
    bool reload = ir_button(port, RETRO_DEVICE_ID_JOYPAD_A);
    ir_gun_position(port, pointer);
    report_button(MAKE_BUTTON(pad, JUSTIFIER_TRIGGER), ir_button(port, RETRO_DEVICE_ID_JOYPAD_B) || reload);
    report_button(MAKE_BUTTON(pad, JUSTIFIER_START), ir_button(port, RETRO_DEVICE_ID_JOYPAD_START));
    report_button(MAKE_BUTTON(pad, JUSTIFIER_OFFSCREEN), reload);
}
static bool report_ir_hybrid()
{
    unsigned device = snes_devices[0];
    if (device != RETRO_DEVICE_IR_MACS && device != RETRO_DEVICE_IR_SCOPE && device != RETRO_DEVICE_IR_JUSTIFIER)
        return false;
    int16_t bits = 0;
    for (int i = 0; i < RETRO_PAD_ID_COUNT; ++i)
        if (ir_button(0, i)) bits |= 1 << i;
    S9xSetJoypadButtons(0, snes_pad_mask(bits));
    if (device == RETRO_DEVICE_IR_MACS)
    {
        ir_gun_position(0, BTN_POINTER);
        report_button(MAKE_BUTTON(PAD_2, MACS_RIFLE_TRIGGER), ir_button(0, RETRO_DEVICE_ID_JOYPAD_B));
    }
    else if (device == RETRO_DEVICE_IR_SCOPE)
    {
        ir_gun_position(0, BTN_POINTER);
        bool turbo = ir_button(0, RETRO_DEVICE_ID_JOYPAD_Y);
        report_button(MAKE_BUTTON(PAD_2, SUPER_SCOPE_TRIGGER), ir_button(0, RETRO_DEVICE_ID_JOYPAD_B));
        report_button(MAKE_BUTTON(PAD_2, SUPER_SCOPE_CURSOR), ir_button(0, RETRO_DEVICE_ID_JOYPAD_X));
        report_button(MAKE_BUTTON(PAD_2, SUPER_SCOPE_TURBO), turbo && !snes_superscope_turbo_latch);
        snes_superscope_turbo_latch = turbo;
        report_button(MAKE_BUTTON(PAD_2, SUPER_SCOPE_START), ir_button(0, RETRO_DEVICE_ID_JOYPAD_START));
        report_button(MAKE_BUTTON(PAD_2, SUPER_SCOPE_OFFSCREEN), ir_button(0, RETRO_DEVICE_ID_JOYPAD_A));
    }
    else
    {
        ir_justifier(0, PAD_2, BTN_POINTER);
        if (snes_devices[1] == RETRO_DEVICE_IR_JUSTIFIER2)
            ir_justifier(1, PAD_3, BTN_POINTER2);
    }
    return true;
}
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
