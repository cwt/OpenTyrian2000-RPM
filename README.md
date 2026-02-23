# OpenTyrian2000-RPM

This project provides RPM packaging for [OpenTyrian2000](https://github.com/KScl/opentyrian2000), an open-source port of the classic DOS game Tyrian 2000.

## Components and Licenses

This project includes several components with different licenses:

- **OpenTyrian2000 source code**: Licensed under GPL-2.0-or-later. Downloaded from the official repository.
- **Patches** (`patches/` directory): Licensed under MIT. These include improvements for HiDPI support, modern scaling, security fixes, bounds checking, and wide-screen scaling.
- **RPM spec file** (`opentyrian2000.spec`): Licensed under MIT.
- **Game data files**: The Tyrian 2000 assets (graphics, music, etc.) are freeware, released by the original developer. They are copyrighted but freely distributable for non-commercial use.

## Building the Package

To build the RPM package:

1. Install build dependencies: `sudo dnf install gcc make pkgconf-pkg-config SDL2-devel SDL2_net-devel rpm-build`
2. Run: `rpmbuild -ba opentyrian2000.spec`

The package will download the source and data files automatically during the build process.

## Installation

After building, install the RPM with: `sudo dnf install opentyrian2000-*.rpm`

## Contributing

Patches and improvements are welcome. Please ensure new contributions follow the appropriate license (MIT for packaging, GPL for code changes).

## Legal Note

While the data files are freeware and can be distributed, the copyright remains with the original creators (Eclipse Productions / Epic MegaGames / Jason Emery). This package is provided as-is for educational and entertainment purposes.