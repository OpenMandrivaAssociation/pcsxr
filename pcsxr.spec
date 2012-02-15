%define svn	73976

Summary:	Open Source Sony PlayStation emulator
Name:		pcsxr
Version:	1.9.93
Release:	%mkrel 0.%{svn}
URL:		http://www.codeplex.com/pcsxr
License:	GPLv2
Group:		Emulators
Source:		%{name}-%{svn}.zip
Patch0:		pcsxr-fix-undefined-operations.patch
Provides:	pcsx = %{version}
Obsoletes:	pcsx-df <= 1.10

BuildRequires:	nasm
BuildRequires:	intltool
BuildRequires:	SDL-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gettext
BuildRequires:	bzip2-devel
BuildRequires:	libglade2-devel
BuildRequires:	mesagl-devel
BuildRequires:	libxv-devel
BuildRequires:	libxext-devel
BuildRequires:	libxtst-devel
BuildRequires:	dos2unix

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
%setup -q -n pcsxr
dos2unix plugins/peopsxgl/*.c
%patch0 -p1

%build
%__sed -i s,Game\;,Game\;Emulator\;,g data/pcsxr.desktop

sh ./autogen.sh

export CFLAGS="%{optflags} -fno-strict-aliasing -pthread -w"
%configure2_5x --enable-opengl
%make

%install
%__rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS ChangeLog INSTALL NEWS README doc/*.txt
%{_bindir}/pcsxr
%{_libdir}/games/psemu
%{_desktopdir}/*.desktop
%{_datadir}/pcsxr
%{_datadir}/psemu
%{_datadir}/pixmaps/*
%{_mandir}/man1/*

