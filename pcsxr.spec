Summary:	Open Source Sony PlayStation emulator
Name:		pcsxr
Version:	1.9.93
Release:	2
License:	GPLv2+
Group:		Emulators
Url:		http://www.codeplex.com/pcsxr
Source:		%{name}-%{version}.tar.bz2
Patch0:		pcsxr-fix-undefined-operations.patch
Provides:	pcsx = %{version}
Obsoletes:	pcsx-df < 1.10-100

BuildRequires:	dos2unix
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	nasm
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xv)

%description
Most advanced fork of PCSX.

This application emulates all components of a Sony PlayStation on
regular PC hardware. It features a sophisticated plugin system allowing
for easy extension and is highly configurable.

To be able to play commercial games on this emulator you need an image
of a Sony PlayStation BIOS ROM. The BIOS is copyrighted by Sony
Computer Entertainment and can therefore not be included in this
package.

BIOS images can be placed in ~/.pcsx/bios or %{_datadir}/psemu/bios.

%prep
%setup -q -n %{name}
dos2unix plugins/peopsxgl/*.c
%patch0 -p1

%build
sed -i s,Game\;,Game\;Emulator\;,g data/pcsxr.desktop

sh ./autogen.sh

export CFLAGS="%{optflags} -fno-strict-aliasing -pthread -w"
%configure2_5x --enable-opengl
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog INSTALL NEWS README doc/*.txt
%{_bindir}/pcsxr
%{_libdir}/games/psemu
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pcsxr
%{_datadir}/psemu
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/%{name}.1.*

