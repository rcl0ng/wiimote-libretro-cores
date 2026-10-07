# Arcade - FBNeo (IR Mouse) — public v1.0.0

Custom pointing profiles for Arkanoid, Centipede, Millipede and Missile Command, plus independent NeoPong v1.1 paddles using guarded in-memory patches. Reduced game subset; matching ROM sets required.

This reduced subset recommends **arkanoid.zip, centiped.zip, milliped.zip, missile.zip, neopong.zip**. Select **Wiimote IR Mouse (left analog)** on each participating port. Matching FBNeo sets are required. Other trial drivers were removed; Arkanoid II, bowling, horseshoes and Marble Madness are outside this build.

Arkanoid: Plus = 1P Start, Wiimote 1 = 2P Start, Minus = coin, B = launch/fire. Earlier Start trouble was reported; the final guide/code specifies this mapping, so include a fresh-remap Start check in RC testing. Missile Command: D-pad Left/Down/Right fires the left/center/right bases. Centipede and Millipede use two-axis pointing. All four were reported working.

NeoPong uses **homebrew v1.1**, program CRC **9f35e29d**, and matching Neo Geo BIOS. Each Wiimote's Y directly positions its own paddle. B/A retain native buttons; Minus inserts coin, Plus starts that player. P2 may need to press Plus again after the Ready sequence to join. NeoPong was reported satisfying and independent after correcting duplicate vJoy assignments. The guarded patch changes emulated RAM, not the ROM ZIP. Only v1.1 is patched, not neoponga v1.0 or other Neo Geo games. Native ball, scoring and AI behavior remain.

**IR Mouse Diagnostics defaults to enabled in the retained binary.** Disable it under Core Options → Input for routine play; the log `fbneo-ir-mouse.log` is written in the save directory and replaced by a subsequent launch. The original diagnostics/test scripts are in the source materials.

See `../INPUT-SETUP.md` for the required Lichtknarre/vJoy mapping. Historical sources and detailed build/test materials are under `development/fbneo_mouse/`.
