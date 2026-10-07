#include <assert.h>
#include <stdarg.h>
#include <string.h>
#include "input.c"

static unsigned bind_calls;
static const char *bound[12];
static int16_t axes[12][2];
static uint16_t keys[12];
static unsigned info_seen;
int ActiveCartType = 0;
static void logger(enum retro_log_level l, const char *fmt, ...) {(void)l;(void)fmt;}
retro_log_printf_t log_cb = logger;
void SS_SetInput(unsigned port, const char *type, uint8_t *data)
{ assert(port < 12); assert(data); bound[port]=type; ++bind_calls; }
void SMPC_SetMultitap(unsigned port, bool enabled) {(void)port;(void)enabled;}
void STVIO_InsertCoin(void) { assert(!"unexpected STV coin"); }
static bool env(unsigned cmd, void *ptr)
{
 if(cmd==RETRO_ENVIRONMENT_SET_CONTROLLER_INFO) {
  struct retro_controller_info *info=ptr;
  for(unsigned p=0;p<2;p++) {
   bool found=false;
   for(unsigned d=0;d<info[p].num_types;d++)
    if(info[p].types[d].id==RETRO_DEVICE_SS_IR_GUN) found=true;
   assert(found);
  }
  ++info_seen;
 }
 return true;
}
static int16_t poll(unsigned p,unsigned device,unsigned index,unsigned id)
{
 assert(p<12);
 if(device==RETRO_DEVICE_ANALOG) {assert(index==0);assert(id<2);return axes[p][id];}
 if(device==RETRO_DEVICE_JOYPAD) return id==RETRO_DEVICE_ID_JOYPAD_MASK ? (int16_t)keys[p] : !!(keys[p] & (1u<<id));
 if(device==RETRO_DEVICE_LIGHTGUN) {
  if(id==RETRO_DEVICE_ID_LIGHTGUN_SCREEN_X) return 4000;
  if(id==RETRO_DEVICE_ID_LIGHTGUN_SCREEN_Y) return -3000;
  if(id==RETRO_DEVICE_ID_LIGHTGUN_TRIGGER) return 1;
  return 0;
 }
 return 0;
}
static void update(bool masks) { if(masks) input_update_with_bitmasks(poll);else input_update(poll); }
int main(void)
{
 input_init_env(env);input_set_env(env);assert(info_seen);
 retro_set_controller_port_device(0,RETRO_DEVICE_SS_IR_GUN);
 retro_set_controller_port_device(1,RETRO_DEVICE_SS_IR_GUN);
 assert(bind_calls==0); /* frontend assignment before content */
 input_init();assert(!strcmp(bound[0],"gun")&&!strcmp(bound[1],"gun"));
 input_set_geometry(352,240);
 for(int masks=0;masks<2;masks++) {
  axes[0][0]=-32768;axes[0][1]=-32768;
  axes[1][0]=32767;axes[1][1]=32767;
  keys[0]=keys[1]=0;update(masks);
  assert(input_data[0].gun_pos[0]==0&&input_data[0].gun_pos[1]==0);
  assert(input_data[1].gun_pos[0]==21471&&input_data[1].gun_pos[1]==239);
  assert(input_data[0].u8[4]==0);
  for(int i=0;i<1000;i++) {
   axes[0][0]=(int16_t)(i*61-32768);axes[0][1]=(int16_t)(i*37-32768);
   update(masks);assert(input_data[1].gun_pos[0]==21471&&input_data[1].gun_pos[1]==239);
  }
  keys[0]=(1u<<RETRO_DEVICE_ID_JOYPAD_B)|(1u<<RETRO_DEVICE_ID_JOYPAD_START);
  update(masks);assert(input_data[0].u8[4]==3&&input_data[1].u8[4]==0);
  keys[0]|=(1u<<RETRO_DEVICE_ID_JOYPAD_A);update(masks);
  assert(input_data[0].u8[4]==6);
  assert((int16_t)input_data[0].gun_pos[0]==-16384);
  keys[0]=(1u<<RETRO_DEVICE_ID_JOYPAD_SELECT);update(masks);
  assert(input_data[0].u8[4]==0); /* Minus no gun action */
  input_set_geometry(352,288);axes[0][0]=axes[0][1]=-32768;update(masks);
  assert(input_data[0].gun_pos[1]==48);
  axes[0][1]=32767;update(masks);assert(input_data[0].gun_pos[1]==335);
  input_set_geometry(352,240);
  setting_gun_input=SETTING_GUN_INPUT_POINTER;update(masks);
  assert(input_data[1].gun_pos[0]==21471); /* gun option does not replace IR */
  setting_gun_input=SETTING_GUN_INPUT_LIGHTGUN;
 }
 retro_set_controller_port_device(1,RETRO_DEVICE_NONE);assert(!strcmp(bound[1],"none"));
 retro_set_controller_port_device(0,RETRO_DEVICE_SS_GUN_US);update(false);
 assert(input_data[0].u8[4]==1); /* ordinary lightgun remains native */
 retro_set_controller_port_device(0,RETRO_DEVICE_JOYPAD);assert(!strcmp(bound[0],"gamepad"));
 retro_set_controller_port_device(0,RETRO_DEVICE_SS_IR_GUN);
 input_shutdown(false);unsigned old_calls=bind_calls;
 retro_set_controller_port_device(1,RETRO_DEVICE_SS_IR_GUN);assert(bind_calls==old_calls);
 input_init();assert(!strcmp(bound[0],"gun")&&!strcmp(bound[1],"gun"));
 input_shutdown(true);input_init();assert(!strcmp(bound[0],"gamepad"));
 puts("PASS: device advertisement, pre-load deferral/load restoration, both polling paths, two-player independence/1000 held frames, NTSC/PAL endpoints, trigger/reload/Start, Minus, pointer-option independence, native restoration, unload/deinit lifecycle.");
 return 0;
}
