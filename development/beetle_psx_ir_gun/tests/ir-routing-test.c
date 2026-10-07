#include "input.c"
#include <assert.h>
#include <stdio.h>
static int ax[2][2],bt[2];
static int16_t cb(unsigned p,unsigned d,unsigned idx,unsigned id)
{
 if(p>1)return 0;
 if(d==RETRO_DEVICE_ANALOG)return ax[p][id];
 if(d==RETRO_DEVICE_JOYPAD)return id==RETRO_DEVICE_ID_JOYPAD_MASK?bt[p]:((bt[p]>>id)&1);
 if(d==RETRO_DEVICE_LIGHTGUN)return id==RETRO_DEVICE_ID_LIGHTGUN_TRIGGER;
 return 0;
}
int main(void)
{
 int mode,k;
 for(mode=0;mode<2;mode++){
  FIO=NULL;
  retro_set_controller_port_device(0,RETRO_DEVICE_PS_IR_GUNCON);
  retro_set_controller_port_device(1,RETRO_DEVICE_PS_IR_JUSTIFIER);
  assert(input_type[0]==RETRO_DEVICE_PS_GUNCON&&input_type[1]==RETRO_DEVICE_PS_JUSTIFIER);
  crop_overscan=false;content_is_pal=false;ax[0][0]=-32768;ax[0][1]=-32768;ax[1][0]=32767;ax[1][1]=32767;
  bt[0]=1<<RETRO_DEVICE_ID_JOYPAD_B;bt[1]=1<<RETRO_DEVICE_ID_JOYPAD_START;gun_input_mode=SETTING_GUN_INPUT_POINTER;
  input_update(mode,cb);assert(input_data[0].gun_pos[0]==0&&input_data[0].gun_pos[1]==0&&input_data[1].gun_pos[0]==2800&&input_data[1].gun_pos[1]==240);
  assert(input_data[0].u8[4]==1&&input_data[1].u8[4]==4);
  for(k=0;k<1000;k++){ax[0][1]=(k%2)?32767:-32768;input_update(mode,cb);assert(input_data[1].gun_pos[1]==240);}
  bt[0]=(1<<RETRO_DEVICE_ID_JOYPAD_A);input_update(mode,cb);assert(input_data[0].u8[4]==8&&input_data[0].gun_pos[0]==(uint16_t)-16384&&input_data[1].u8[4]==4);
  bt[0]=(1<<RETRO_DEVICE_ID_JOYPAD_X)|(1<<RETRO_DEVICE_ID_JOYPAD_Y);bt[1]=(1<<RETRO_DEVICE_ID_JOYPAD_X);input_update(mode,cb);assert(input_data[0].u8[4]==6&&input_data[1].u8[4]==2);
  bt[0]=1<<RETRO_DEVICE_ID_JOYPAD_START;input_update(mode,cb);assert(input_data[0].u8[4]==4);
  bt[0]=1<<RETRO_DEVICE_ID_JOYPAD_SELECT;bt[1]=0;input_update(mode,cb);assert(input_data[0].u8[4]==0&&input_data[1].u8[4]==0);
  crop_overscan=true;content_is_pal=true;ax[0][0]=32767;ax[0][1]=32767;input_update(mode,cb);assert(input_data[0].gun_pos[0]==2680&&input_data[0].gun_pos[1]==292);
  input_set_controller_port_compatibility(0,BEETLE_DB_CTRL_GUNCON);assert(input_type[0]==RETRO_DEVICE_PS_GUNCON);
  input_set_controller_port_compatibility(0,BEETLE_DB_CTRL_DIGITAL);assert(input_type[0]==RETRO_DEVICE_JOYPAD);
  input_set_controller_port_compatibility(0,BEETLE_DB_CTRL_NONE);assert(input_type[0]==RETRO_DEVICE_PS_GUNCON);
  retro_set_controller_port_device(0,RETRO_DEVICE_JOYPAD);assert(!ir_gun_enabled[0]);
  retro_set_controller_port_device(0,RETRO_DEVICE_PS_GUNCON);gun_input_mode=SETTING_GUN_INPUT_LIGHTGUN;input_update(mode,cb);assert(input_data[0].u8[4]==1);
 }
 puts("PASS: both polling settings, pre-content device normalization, independent GunCon/Justifier, 1000 held-P2 frames, reload/aux/start, NTSC/PAL/crop endpoints, native restore and compatibility profiles.");return 0;
}
