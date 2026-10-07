# Sony - PlayStation (Beetle PSX IR Gun) — public v1.0.0

Absolute left-stick GunCon and Justifier aiming with independent player ports. Software renderer. Select a gun supported by the game and region; no generic hybrid pad routing.

Select **Wiimote IR GunCon** or **Wiimote IR Justifier** on each corresponding frontend port. Match the gun to the game's region; consult `PSX_Gun_Types.txt` in the historical archive for the collection mapping. Use normal regional Beetle PSX BIOS requirements. The DLL uses the software renderer.

B shoots; A provides an offscreen reload shot where supported. GunCon: Wiimote 1 = GunCon A (Time Crisis cover/action), Wiimote 2 and Plus = GunCon B. GunCon has no dedicated Start/Select. Justifier: Wiimote 1 = auxiliary, Plus = Start. Minus/Home have no synthetic gun action. Enable a visible Gun Cursor in core options and run game calibration after changing cropping/display settings.

GunCon/Justifier gameplay was reported successful across several games. No generic pad/gun hybrid routing is included. Game compatibility profiles can replace an incompatible requested device. Region-specific gun support must be checked; Galaxian 3, Extreme Ghostbusters and Resident Evil Survivor were not established as working gun configurations in this session. Do not present them as confirmed.

See `../INPUT-SETUP.md` for the required Lichtknarre/vJoy mapping. Historical sources and detailed build/test materials are under `development/beetle_psx_ir_gun/`.
