PS2 GunCon2 Hybrid v0.9 — Windows x64 TEST BUILD

Includes the existing v0.5 gun controls and widescreen profiles, expanded
Time Crisis vertical scaling, optional cheats, and a savestate load-order fix
candidate. Windows gameplay and the reported RetroBat freeze need your test.

INSTALL
1. Close RetroArch and RetroBat.
2. Back up your current pcee2_analog_gun_libretro.dll.
3. Copy cores\pcee2_analog_gun_libretro.dll from this package into:
   D:\RetroBatGun\emulators\retroarch\cores\
4. Copy info\pcee2_analog_gun_libretro.info into RetroArch's info folder.
   Existing BIOS/resources, controller remaps and memory cards stay in place.
5. Core Information / the core version should show RC-v0.9.

TIME CRISIS II / 3 VERTICAL SCALE
Quick Menu > Core Options > Graphics >
Time Crisis II / 3: Split Vertical Scale = 200% to start.

IMPORTANT: RetroArch retains your old 115% choice. Select 200% manually.
The range is now 100–220%, including 195/200/205%. 200% is a starting point to
compare, not a precisely calibrated measurement. Resume gameplay to apply it.
The same value adjusts vertical gun compensation. Check center, top and bottom
shots on both sides. Width, bars, shared screens and single-player behavior
follow the existing v0.5 layout logic. Keep your working layout and widescreen
settings; no new vJoy axis remapping is needed.

CREDITS / LIVES
Quick Menu > Core Options > System:
  Gun Games: Infinite Credits / Continues
  Gun Games: Infinite Lives / Health
Both switches default to Disabled and apply independently. In v0.9 you can
leave them Enabled when launching a state from RetroBat: their writes pause
through boot/restoration and the first three resumed emulated frames, then
resume automatically. No manual off/load/on sequence is needed for this test.
This is a test candidate based on the successful cheats-off v0.8 load; it still
needs validation with your enabled settings.

USA revisions only:
  Time Crisis II  — credits + P1/P2 health
  Time Crisis 3   — shared continues + player-relative health-decrement patch
  Ninja Assault  — credits + P1/P2 health
  Vampire Night  — credits + P1/P2 health
  Endgame        — main-game health only; no credit or training-mode patch
Dead Aim and Dino Stalker have no new cheats.

Enable health before losing the last life; counter profiles do not resurrect
a dead/inactive player. Disabling stops replenishment, but already granted
credits/health remain until used. TC3/Endgame instruction patches restore their
original instruction when disabled. No ammo, timer or unlock cheats are added.
Profiles require matching disc serial, executable CRC and code signatures.
Both-player and mode coverage need gameplay testing.

SAVESTATE TEST
Keep backups of your existing states and memory cards.
1. For this v0.9 test, leave the desired credits/health options ENABLED.
   Keep MTVU off as in your latest successful cheats-off test.
2. Launch TC2 normally and try Quick Menu > Load State. Confirm play, aiming,
   audio and menu access continue, rather than checking only the first image.
3. Close the game and launch its state tile directly from RetroBat.
4. Make a fresh state in a separate slot and repeat both load methods.

v0.9 queues a requested state until the game executable has started and the
following CPU frame boundary has been reached. VM initialization alone no longer
permits a restore. Boot frames keep running while the request waits. Restoration
then takes place outside the CPU execution/event callback.

RetroBat/RetroArch may say "load successful" when the early request is accepted.
The later v0.9 completion notification and diagnostic log show when restoration
actually finishes. You may briefly see the normal boot before the saved scene.
If the game never starts, the request stays pending until reset or unload cancels
it. Manual loads after game startup retain the v0.6 completion path and 15-second
wait. This is a targeted Windows test candidate, not a confirmed black-screen
fix. State files, vertical scale, cheats, and controls retain v0.6 behavior.

LOG THAT DOES NOT DEPEND ON RETROARCH'S LOG-TO-FILE SWITCH
With the system directory shown in your diagnostic, the new file is:
  D:\RetroBatGun\bios\pcsx2\logs\rc-gun-v09.log

Generally: <RetroArch system directory>\pcsx2\logs\rc-gun-v09.log.
It appends across runs, and flushes each diagnostic line. The launch header
also reports its actual path. The folder must be writable. If the new file is
missing, check the active core/version and the configured System/BIOS directory.

If loading still fails, send this file and say manual load or RetroBat tile.
Useful milestones are:
  Queued ... startup=...
  VM initialized; entry-state restore still waits for game startup
  Waiting for game executable startup and following frame boundary
  Game executable started; following frame boundary reached
  Cheat writes suspended for restore and first three resumed frames
  Three resumed frames completed; enabled cheats may resume next frame
  Restore begin outside Execute
  Restore completed ... OR Restore failed ...
  First emulated frame reached after restore
  Frontend image handoff after restored CPU frame
The handoff line records delivery to the frontend; it cannot verify visible
pixels or that the game remains responsive. A full RetroArch verbose log is
still useful for graphics-driver details.

CONTROLS
Hold Select / menu, Home / vJoy button 6 calibration, per-port gun devices,
trigger/cover/action remaps, and Wiimote-safe input backends follow v0.5.
Keep your working native Offscreen Reload remap choice.

VALIDATION AND SOURCE
source\Test_Results.txt lists native checks and supplied-state RAM checks.
source\PE_Verification.json describes the Windows DLL exports/imports.
source\CHEAT_RESEARCH.md records addresses, executable checks and attribution.
Native checks are not a substitute for running the Windows games.
The custom changes are GPL-3.0+; licenses and complete source delta are included.
See source\BUILDING.txt to reproduce the DLL from the pinned upstream source.
