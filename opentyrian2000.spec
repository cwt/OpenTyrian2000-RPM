Name:           opentyrian2000
Version:        2000.2025.04.08
Release:        2%{?dist}
Summary:        An open-source port of the DOS game Tyrian 2000

License:        GPL-2.0-or-later
URL:            https://github.com/KScl/opentyrian2000
Source0:        %{url}/archive/refs/tags/v2000.20250408.tar.gz
Source1:        https://www.camanis.net/tyrian/tyrian2000.zip
Patch0:         0000-hidpi-support.patch
Patch1:         0001-modern-scaling.patch
Patch2:         0002-security-fixes.patch
Patch3:         0003-bilinear-bounds-check.patch
Patch4:         0004-wide-screen-scaling.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_net-devel

Requires:       SDL2
Requires:       SDL2_net

Provides:       opentyrian2000 = %{version}

%description
OpenTyrian2000 is an open-source port of the DOS game Tyrian. It is a fork of
OpenTyrian, with the end goal being to replicate the experience of Tyrian 2000
as closely as possible.

Tyrian is an arcade-style vertical scrolling shooter. The story is set
in 20,031 where you play as Trent Hawkins, a skilled fighter-pilot employed
to fight MicroSol and save the galaxy.

Tyrian features a story mode, one- and two-player arcade modes, and networked
multiplayer.

%prep
%setup -n opentyrian2000-2000.20250408
%patch 0 -p1 -b .hidpi
%patch 1 -p1 -b .modern-scaling
%patch 2 -p1 -b .security-fixes
%patch 3 -p1 -b .bilinear-bounds
%patch 4 -p1 -b .wide-screen-scaling

%build
make prefix=/usr

%install
# Create buildroot directory
mkdir -p %{buildroot}

# Install the main application files using make install
# The Makefile sets TYRIAN_DIR to $(gamesdir)/opentyrian2000 by default
make install prefix=/usr DESTDIR=%{buildroot}

# Install the game data files in the TYRIAN_DIR directory that the game expects
mkdir -p %{buildroot}%{_datadir}/games/opentyrian2000/
cd %{buildroot}%{_datadir}/games/opentyrian2000/
unzip -qo %{SOURCE1} -d .
mv tyrian2000/* .
rmdir tyrian2000

%files
%{_bindir}/opentyrian2000
%dir %{_datadir}/games/opentyrian2000
%{_datadir}/games/opentyrian2000/*
%doc NEWS README
%{_mandir}/man6/opentyrian2000.6*
%{_datadir}/applications/opentyrian2000.desktop
%{_datadir}/icons/hicolor/22x22/apps/opentyrian2000.png
%{_datadir}/icons/hicolor/24x24/apps/opentyrian2000.png
%{_datadir}/icons/hicolor/32x32/apps/opentyrian2000.png
%{_datadir}/icons/hicolor/48x48/apps/opentyrian2000.png
%{_datadir}/icons/hicolor/128x128/apps/opentyrian2000.png

%changelog
* Thu Dec 18 2025 Chaiwat Suttipongsakul <cwt@bashell.com> - 2000.2025.04.08-1
- Add bounds checking to bilinear scaler to prevent out-of-bounds memory access
- Fix potential buffer overflow vulnerabilities
- Add modern scaling algorithms patch (bilinear, CRT scanline)
- Remove 2x scaling algorithms (too small for modern monitor)
- Add High DPI support patch
- Initial RPM package for OpenTyrian2000
