Base: https://github.com/flyinghead/flycast
Commit: 6bb0fc3e18dac4b01694f488c7a71f5930e8a648
Apply hybrid-v1.patch after checking out the pinned commit. All submodules
remain at the revisions referenced by that commit (see SUBMODULES.txt).
The patch includes all changes and the complete new policy header. It changes
only libretro input/device registration, the core's displayed identity, and
bundled-zlib CMake discovery for a MinGW cross-build without system zlib.
No ROM, game CPU, renderer, NVRAM format or state serialization is patched.

build-linux-mingw.sh provides the equivalent portable rebuild process with
system-installed tools. toolchain-used.cmake records the actual relocated
compiler paths in the build environment; those paths are historical and
should not be copied unchanged to another PC. The compiler packages were
extracted locally because system package installation was unavailable.

Native test build:
 cmake -S TREE -B build-native -G Ninja -DLIBRETRO=ON -DUSE_HOST_LIBZIP=OFF -DCMAKE_BUILD_TYPE=Release
 cmake --build build-native -j4
Native test compile from a workspace with source in flycast and build-native:
 g++ -std=c++17 -DLIBRETRO -Iflycast/core -Iflycast/core/deps -Iflycast/core/deps/nowide/include -Iflycast/core/deps/libretro-common/include -Iflycast/shell/libretro tests/input-integration.cpp -Lbuild-native -l:flycast_libretro.so -Wl,-rpath,'$ORIGIN/../build-native' -o tests/input-integration
 ./tests/input-integration
The integration harness polls the real built core through libretro callbacks;
it needs no ROM, rendering context or BIOS. It does not run a game.
