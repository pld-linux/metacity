#
# Conditional build:
%bcond_without	vulkan		# Vulkan support
%bcond_without	static_libs	# static library

Summary:	Metacity window manager
Summary(pl.UTF-8):	Zarządca okien Metacity
Name:		metacity
Version:	3.38.0
Release:	1
Epoch:		2
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/metacity/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	7c32510bee1abcbc827cf4b90fc6af36
URL:		https://wiki.gnome.org/Projects/Metacity
%if %{with vulkan}
BuildRequires:	Vulkan-Headers
BuildRequires:	Vulkan-Loader-devel
%endif
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.14
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.3.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libgtop-devel >= 2.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pango-devel >= 1:1.2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.3
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xz >= 1:4.999.7
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	filesystem >= 3.0-20
Requires:	gsettings-desktop-schemas >= 3.3.0
Requires:	xorg-lib-libXcomposite >= 0.3
Requires:	zenity
Provides:	gdm-wm = 3.2.1-1
Provides:	gnome-wm
Obsoletes:	metacity-themes-Adwaita
Obsoletes:	metacity-themes-AgingGorilla
Obsoletes:	metacity-themes-Atlanta
Obsoletes:	metacity-themes-Bright
Obsoletes:	metacity-themes-Crux
Obsoletes:	metacity-themes-Esco
Obsoletes:	metacity-themes-HighContrast
Obsoletes:	metacity-themes-Metabox
Obsoletes:	metacity-themes-Simple
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metacity is a simple window manager that integrates nicely with GNOME.

%description -l pl.UTF-8
Metacity jest prostym zarządcą okien ładnie integrującym się z GNOME.

%package libs
Summary:	Metacity - libraries
Summary(pl.UTF-8):	Metacity - biblioteki
Group:		X11/Libraries
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.22.0
Requires:	pango >= 1:1.2.0
Conflicts:	metacity <= 2.6.3-4

%description libs
This package contains libraries for Metacity window manager.

%description libs -l pl.UTF-8
Pakiet zawierający biblioteki zarządcy okien Metacity.

%package devel
Summary:	Metacity - header files
Summary(pl.UTF-8):	Metacity - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.44.0
Requires:	gtk+3-devel >= 3.22.0

%description devel
This package contains header files for Metacity window manager.

%description devel -l pl.UTF-8
Pakiet zawierający pliki nagłówkowe zarządcy okien Metacity.

%package static
Summary:	Static Metacity library
Summary(pl.UTF-8):	Statyczna biblioteka Metacity
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static version of Metacity library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki Metacity.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ZENITY=/usr/bin/zenity \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	%{!?with_vulkan:--disable-vulkan}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmetacity.la

# "metacity" gettext domain, "creating-metacity-themes" help
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README rationales.txt
%attr(755,root,root) %{_bindir}/metacity
%attr(755,root,root) %{_bindir}/metacity-message
%attr(755,root,root) %{_bindir}/metacity-theme-viewer
%{_datadir}/glib-2.0/schemas/org.gnome.metacity.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.metacity.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.metacity.keybindings.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.metacity.theme.gschema.xml
# package keybindings dir, not to pull optional gnome-control-center dependency
%dir %{_datadir}/gnome-control-center
%dir %{_datadir}/gnome-control-center/keybindings
%{_datadir}/gnome-control-center/keybindings/50-metacity-*.xml
%{_desktopdir}/metacity.desktop
%{_mandir}/man1/metacity*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmetacity.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmetacity.so.3

%files devel
%defattr(644,root,root,755)
%doc ChangeLog HACKING doc/dialogs.txt
%attr(755,root,root) %{_libdir}/libmetacity.so
%{_includedir}/metacity
%{_pkgconfigdir}/libmetacity.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmetacity.a
%endif
