# Sega - MS/GG/MD/CD (Genesis Plus GX IR Gun) — public v1.0.0

Absolute left-stick Light Phaser, Menacer and Justifier inputs. Internal MD/CD gamepad and gun routing, independent second Justifier. Body Count gun detection remains unresolved.

MD/CD: on frontend Port 1 select **Wiimote IR Menacer + Gamepad** or **Wiimote IR Justifier + Gamepad**. For a second Justifier choose **Wiimote IR Justifier (Player 2)** on frontend Port 2; otherwise **Joypad Port Empty**. The core internally supplies a 3-button pad on console port 1 and gun(s) on console port 2. Remove old frontend Port 3 gun remaps and duplicate vJoy bindings.

Master System: use **Wiimote IR Light Phaser** on the required port, with a second only where the game supports it. B shoots, A reloads/offscreen shoots where supported; 1/2 are auxiliary buttons, Plus supplies Start, D-pad supplies hybrid menu controls. Minus does not synthesize reload. Enable **Show Light Gun Crosshair** as desired. Native gun input options do not select the custom IR source.

Menacer 6-in-1, Lethal Enforcers MD/CD and Master System gun play were reported successful, including independent two-player Justifier testing. **Body Count gun detection remains unresolved.** Gamepad-only and unsupported titles do not acquire gun support merely by selecting the device.

See `../INPUT-SETUP.md` for the required Lichtknarre/vJoy mapping. Historical sources and detailed build/test materials are under `development/genesis_plus_gx_analog/`.
