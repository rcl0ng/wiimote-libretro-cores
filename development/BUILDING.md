# Building the modified cores

Extract each core's full source tar.gz to a separate work directory. Keep its bundled headers, libretro-common/deps and all notices. Historical patches are for review or applying to the recorded upstream base; do not reapply them to the already-modified source archive. Consult the upstream Makefile platform options for a Windows x64 MinGW build. This release preserves the tested binaries and does not claim a fresh rebuild or reproducible binary hash.

| Core | Source build entry point |
|---|---|
| FCEUmm | Makefile.libretro |
| Snes9x gun and mouse | libretro/Makefile |
| Genesis Plus GX | Makefile.libretro |
| Beetle PSX / Saturn | Makefile (libretro-common and deps included) |
| FBNeo mouse | src/burner/libretro/Makefile, SUBSET=mouse |
| FBNeo shooter | src/burner/libretro/Makefile, SUBSET=galaga_ir |

FBNeo: enter src/burner/libretro, run `make SUBSET=mouse generate-files` then `make SUBSET=mouse` with the appropriate platform/compiler options. Makefile.mouse is in the archive; a reference copy is also outside it. For shooter use SUBSET=galaga_ir and rename its generated fbneo_galaga_ir_libretro.dll to fbneo_shooter_libretro.dll. Keep the new matching info basename. A future source change can update embedded strings; v1 preserves the tested binary identity.

Chihiro: development/chihiro/source/BUILD.txt has the recorded Windows x64 cross-build command, toolchain image and original flags. Modified source and Meson packagefiles/wraps are in Chihiro_Modified_Source.tar.gz. dependencies/ contains pinned wrap archives, wrap patches, GLib, gettext, iconv, PCRE2, libffi, pixman, libepoxy, samplerate, zlib and the pinned MXE source. download-manifest.json records source origins and hashes. Put wrap-file archives/patch ZIPs into the extracted core's subprojects/packagecache, or let Meson fetch the recorded revisions. Extract wrap-git snapshots into the corresponding subproject directory named by Meson (normally the wrap basename); retain packagefiles overlays and licenses. Meson can also fetch their pinned git revisions directly. Build external static libraries using the provided MXE recipes; the core's ubuntu-win64-cross directory contains recipe overrides. SDL3 is a Meson subproject; the older toolchain SDL2 recipe is not its source.

The included MXE pin specifies gettext 0.25 and iconv 1.18; the historical generated DLL notice leaves these version fields blank. Their association is derived from the recorded toolchain recipe, not from a new inspection of linker objects. The GNOME libepoxy 1.5.10 tar.xz source is included because the recipe's tar.gz release URL is unavailable; download-manifest records its separately computed hash. Rebuilding requires native build utilities, Windows cross compiler and potentially other optional upstream features' dependencies. Disable unused optional features or supply their upstream sources. Preserve static-library source and permit replacement/relinking when distributing modified builds. Bundled source does not supply a compiler executable.
