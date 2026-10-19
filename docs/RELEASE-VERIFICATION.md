# Release verification — v1.2.0

**Packaging:** The release ZIPs were assembled from provided binaries and sources and archive/manifest-checked. This does not constitute a fresh compilation or an emulator/gameplay certification.

**Core set (11):** Beetle PSX IR Gun, Beetle Saturn IR Gun, FBNeo IR Mouse, FBNeo Shooter IR (`fbneo_shooter` naming retained), FCEUmm IR Gun, Flycast Hybrid IR, Genesis Plus GX hybrid, PCSX2 GunCon2 hybrid, SNES9x Analog Mouse v10, SNES9x IR Gun, and VICE x64 Analog Gun.

**New reported capability:** SNES9x Analog Mouse v10 adds two-player Arkanoid: Doh It Again dual-paddle support; test on the target system before making universal compatibility claims.

**Out of scope:** Zeus, xemu, 3DO and Chihiro (separate project). Preserve old v1.0.0 validation records under historical sources where available; they do not verify newer DLLs.

RetroBat reference XML files are examples copied from specific environments, **not safe drop-in replacements**. Verify XML structure, system-specific overrides, and core names before merging with active configuration files.
