#include "libretro.c"
#include <assert.h>
static int axes_test[2][2],buttons_test[2],bad_axis_reads;
static int16_t test_input(unsigned p,unsigned d,unsigned idx,unsigned id)
{
 if(d==RETRO_DEVICE_ANALOG){if(p>1){bad_axis_reads++;return 0;}return axes_test[p][id];}
 if(p>1)return 0;
 if(d==RETRO_DEVICE_JOYPAD)return id==RETRO_DEVICE_ID_JOYPAD_MASK ? buttons_test[p] : ((buttons_test[p]>>id)&1);
 if(d==RETRO_DEVICE_LIGHTGUN){if(id==RETRO_DEVICE_ID_LIGHTGUN_TRIGGER)return 1;return 0;}
 return 0;
}
static void check_poll(void (*poller)(void))
{
 int k;
 input_state_cb=test_input;bitmap.viewport.w=320;bitmap.viewport.h=224;
 system_hw=SYSTEM_MD;
 retro_set_controller_port_device(0,RETRO_DEVICE_IR_JUSTIFIER);
 retro_set_controller_port_device(1,RETRO_DEVICE_IR_JUSTIFIER2);
 assert(input.system[0]==SYSTEM_GAMEPAD && input.system[1]==SYSTEM_JUSTIFIER);
 assert(input.dev[0]==DEVICE_PAD3B&&input.dev[4]==DEVICE_LIGHTGUN&&input.dev[5]==DEVICE_LIGHTGUN);
 axes_test[0][0]=-32768;axes_test[0][1]=-32768;axes_test[1][0]=32767;axes_test[1][1]=32767;
 buttons_test[0]=(1<<RETRO_DEVICE_ID_JOYPAD_START)|(1<<RETRO_DEVICE_ID_JOYPAD_B)|(1<<RETRO_DEVICE_ID_JOYPAD_LEFT);
 buttons_test[1]=1<<RETRO_DEVICE_ID_JOYPAD_X;
 retro_gun_mode=RetroPointer; /* Native core option must not alter IR devices. */
 poller();
 assert(input.analog[4][0]==0&&input.analog[4][1]==0&&input.analog[5][0]==319&&input.analog[5][1]==223);
 assert((input.pad[0]&(INPUT_START|INPUT_LEFT|INPUT_B))==(INPUT_START|INPUT_LEFT|INPUT_B));
 assert(input.pad[4]==(INPUT_A|INPUT_START)&&input.pad[5]==INPUT_B);
 for(k=0;k<1000;k++){axes_test[0][1]=(k%2)?32767:-32768;poller();assert(input.analog[5][1]==223);}
 buttons_test[1]=1<<RETRO_DEVICE_ID_JOYPAD_A;poller();assert(input.analog[5][0]==-1000&&input.pad[5]==INPUT_A);assert(input.analog[4][0]==0);
 buttons_test[1]=0;buttons_test[0]=1<<RETRO_DEVICE_ID_JOYPAD_SELECT;poller();assert(input.analog[4][0]==0&&input.pad[4]==0);
 retro_set_controller_port_device(1,RETRO_DEVICE_NONE);poller();assert(input.pad[5]==0&&input.analog[5][0]==-1000);assert(input.analog[4][0]==0);
 retro_set_controller_port_device(0,RETRO_DEVICE_IR_MENACER);retro_set_controller_port_device(1,RETRO_DEVICE_JOYPAD);
 assert(input.system[0]==SYSTEM_GAMEPAD&&input.system[1]==SYSTEM_MENACER&&input.dev[5]==NO_DEVICE);poller();assert(input.analog[4][0]==0);
 retro_set_controller_port_device(0,RETRO_DEVICE_MDPAD_6B);assert(input.system[0]==SYSTEM_GAMEPAD&&input.system[1]==SYSTEM_GAMEPAD&&input.dev[0]==DEVICE_PAD6B&&input.dev[4]!=DEVICE_LIGHTGUN);
 system_hw=SYSTEM_SMS;
 retro_set_controller_port_device(0,RETRO_DEVICE_IR_PHASER);retro_set_controller_port_device(1,RETRO_DEVICE_IR_PHASER);
 buttons_test[0]=1<<RETRO_DEVICE_ID_JOYPAD_B;buttons_test[1]=0;poller();assert(input.analog[0][0]==0&&input.analog[4][0]==319&&input.pad[0]==INPUT_A&&input.pad[4]==0);
 retro_set_controller_port_device(0,RETRO_DEVICE_NONE);poller();assert(input.dev[0]==NO_DEVICE&&input.analog[4][0]==319);
 retro_set_controller_port_device(0,RETRO_DEVICE_MSPAD_2B);retro_set_controller_port_device(1,RETRO_DEVICE_PHASER);retro_gun_mode=RetroLightgun;poller();assert(input.pad[4]==INPUT_A);assert(input.analog[4][0]>0);
 assert(bad_axis_reads==0);
}
int main(void){check_poll(osd_input_update_internal);check_poll(osd_input_update_internal_bitmasks);puts("PASS: both polling paths, hybrid Start/menu, independent Justifiers, 1000 stationary-P2 frames, reload/aux, minus no reload, disabled P2, Menacer, dual Phaser, disabled P1, native restore and native lightgun regression.");return 0;}
