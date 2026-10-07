#include "libretro.c"
#include <assert.h>
static int test_axes[2],test_buttons[2],bad_aim_reads;
static void test_poll(void){}
static bool test_env(unsigned cmd, void *data){return false;}
static int16_t test_input(unsigned p,unsigned d,unsigned idx,unsigned id)
{
 if(d==RETRO_DEVICE_ANALOG){if(p){bad_aim_reads++;return 0;}return test_axes[id];}
 if(d==RETRO_DEVICE_JOYPAD && p<2)return id==RETRO_DEVICE_ID_JOYPAD_MASK?test_buttons[p]:((test_buttons[p]>>id)&1);
 return 0;
}
int main(void)
{
 int mode,k;FCEUGI game={0};game.type=GIT_CART;game.input[0]=game.input[1]=SI_GAMEPAD;game.inputfc=SIFC_NONE;
 environ_cb=test_env;log_cb.log=default_logger;GameInfo=&game;input_cb=test_input;poll_cb=test_poll;
 for(mode=0;mode<2;mode++){
  libretro_supports_bitmasks=mode;
  retro_set_controller_port_device(0,RETRO_DEVICE_IR_ZAPPER);
  retro_set_controller_port_device(1,RETRO_DEVICE_NONE);
  assert(nes_input.type[0]==RETRO_DEVICE_GAMEPAD&&nes_input.type[1]==RETRO_DEVICE_ZAPPER);
  crop_overscan_h_left=crop_overscan_h_right=crop_overscan_v_top=crop_overscan_v_bottom=0;
  test_axes[0]=-32768;test_axes[1]=32767;test_buttons[0]=(1<<RETRO_DEVICE_ID_JOYPAD_START)|(1<<RETRO_DEVICE_ID_JOYPAD_SELECT)|(1<<RETRO_DEVICE_ID_JOYPAD_B);test_buttons[1]=0;
  zappermode=RetroSTLightgun;switchZapper=1;FCEUD_UpdateInput();
  assert(switchZapper==0);assert(nes_input.MouseData[1][0]==0&&nes_input.MouseData[1][1]==239&&nes_input.MouseData[1][2]==1);
  assert((nes_input.JSReturn&(JOY_START|JOY_SELECT|JOY_B))==(JOY_START|JOY_SELECT|JOY_B));
  for(k=0;k<1000;k++){FCEUD_UpdateInput();assert(nes_input.MouseData[1][0]==0&&nes_input.MouseData[1][1]==239);}
  test_axes[0]=32767;test_axes[1]=-32768;FCEUD_UpdateInput();assert(nes_input.MouseData[1][0]==255&&nes_input.MouseData[1][1]==0);
  crop_overscan_h_left=8;crop_overscan_h_right=12;crop_overscan_v_top=10;crop_overscan_v_bottom=14;
  FCEUD_UpdateInput();assert(nes_input.MouseData[1][0]==243&&nes_input.MouseData[1][1]==10);
  test_axes[0]=-32768;test_axes[1]=32767;FCEUD_UpdateInput();assert(nes_input.MouseData[1][0]==8&&nes_input.MouseData[1][1]==225);
  test_buttons[0]=1<<RETRO_DEVICE_ID_JOYPAD_A;FCEUD_UpdateInput();assert(nes_input.MouseData[1][2]==2&&nes_input.MouseData[1][0]==256&&nes_input.MouseData[1][1]==240);assert(nes_input.JSReturn&JOY_A);
  test_buttons[0]=0;FCEUD_UpdateInput();assert(nes_input.MouseData[1][2]==0&&nes_input.MouseData[1][0]==8);
  retro_set_controller_port_device(1,RETRO_DEVICE_GAMEPAD);assert(nes_input.type[1]==RETRO_DEVICE_ZAPPER);
  retro_set_controller_port_device(0,RETRO_DEVICE_GAMEPAD);assert(nes_input.type[0]==RETRO_DEVICE_GAMEPAD&&nes_input.type[1]==RETRO_DEVICE_GAMEPAD);
 }
 assert(bad_aim_reads==0);puts("PASS both polling modes, endpoints/cropped viewport, 1000 held frames, trigger/away/release, Start/Select/gamepad, frontend assignment order, native restoration.");return 0;
}
