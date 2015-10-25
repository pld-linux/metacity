#
# TODO:
# - something with %{_datadir}/themes/Theme dirs (some belong to gnome-themes,
#   some don't belong anywhere...)
# - metacity requires itself (links with installed libmetacity-private
#   instead of linking with built one?)
#
# Conditional build:
%bcond_with	gnome2		# build with support for GNOME2 wm-properties
#
Summary:	Metacity window manager
Summary(pl.UTF-8):	Zarządca okien Metacity
Name:		metacity
Version:	3.18.1
Release:	1
Epoch:		2
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/metacity/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	f81a6c687dde4ff567a35c7daf2e23f9
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.13
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.3.0
BuildRequires:	gtk+3-devel >= 3.15.2
BuildRequires:	intltool >= 0.40.0
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
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xz >= 1:4.999.7
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.36.0
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gsettings-desktop-schemas >= 3.3.0
Requires:	metacity-theme-base = %{epoch}:%{version}-%{release}
Requires:	zenity
Provides:	gnome-wm
Provides:	gdm-wm = 3.2.1-1
# sr@Latn vs. sr@latin
Conflicts:	filesystem < 3.0-20
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metacity is a simple window manager that integrates nicely with
GNOME2.

%description -l pl.UTF-8
Metacity jest prostym zarządcą okien ładnie integrującym się z GNOME2.

%package libs
Summary:	Metacity - libraries
Summary(pl.UTF-8):	Metacity - biblioteki
Group:		X11/Libraries
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.15.2
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
Requires:	gtk+3-devel >= 3.15.2

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

%package themes-AgingGorilla
Summary:	AgingGorilla theme for Metacity
Summary(pl.UTF-8):	Motyw AgingGorilla dla Metacity
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	metacity-theme-base = %{epoch}:%{version}-%{release}

%description themes-AgingGorilla
AgingGorilla theme for Metacity.

%description themes-AgingGorilla -l pl.UTF-8
Motyw AgingGorilla dla Metacity.

%package themes-Adwaita
Summary:	Adwaita theme for Metacity
Summary(pl.UTF-8):	Motyw Adwaita dla Metacity
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	metacity-theme-base = %{epoch}:%{version}-%{release}

%description themes-Adwaita
Adwaita theme for Metacity.

%description themes-Adwaita -l pl.UTF-8
Motyw Adwaita dla Metacity.

%package themes-Atlanta
Summary:	Atlanta theme for Metacity
Summary(pl.UTF-8):	Motyw Atlanta dla Metacity
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	metacity-theme-base = %{epoch}:%{version}-%{release}

%description themes-Atlanta
Atlanta theme for Metacity.

%description themes-Atlanta -l pl.UTF-8
Motyw Atlanta dla Metacity.

%package themes-Bright
Summary:	Bright theme for Metacity
Summary(pl.UTF-8):	Motyw Bright dla Metacity
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	metacity-theme-base = %{epoch}:%{version}-%{release}

%description themes-Bright
Bright theme for Metacity.

%description themes-Bright -l pl.UTF-8
Motyw Bright dla Metacity.

%package themes-Crux
Summary:	Crux theme for Metacity
Summary(pl.UTF-8):	Motyw Crux dla Metacity
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	metacity-theme-base = %{epoch}:%{version}-%{release}

%description themes-Crux
Crux theme for Metacity.

%description themes-Crux -l pl.UTF-8
Motyw Crux dla Metacity.

%package themes-Esco
Summary:	Esco theme for Metacity
Summary(pl.UTF-8):	Motyw Esco dla Metacity
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	metacity-theme-base = %{epoch}:%{version}-%{release}

%description themes-Esco
Esco theme for Metacity.

%description themes-Esco -l pl.UTF-8
Motyw Esco dla Metacity.

%package themes-HighContrast
Summary:	HighContrast theme for Metacity
Summary(pl.UTF-8):	Motyw HighContrast dla Metacity
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	metacity-theme-base = %{epoch}:%{version}-%{release}

%description themes-HighContrast
HighContrast theme for Metacity.

%description themes-HighContrast -l pl.UTF-8
Motyw HighContrast dla Metacity.

%package themes-Metabox
Summary:	Metabox theme for Metacity
Summary(pl.UTF-8):	Motyw Metabox dla Metacity
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	metacity-theme-base = %{epoch}:%{version}-%{release}

%description themes-Metabox
Metabox theme for Metacity.

%description themes-Metabox -l pl.UTF-8
Motyw Metabox dla Metacity.

%package themes-Simple
Summary:	Simple theme for Metacity
Summary(pl.UTF-8):	Motyw Simple dla Metacity
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	metacity-theme-base = %{epoch}:%{version}-%{release}

%description themes-Simple
Simple theme for Metacity.

%description themes-Simple -l pl.UTF-8
Motyw Simple dla Metacity.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ZENITY=/usr/bin/zenity \
	--enable-compositor \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xml/metacity

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

install doc/metacity-theme.dtd $RPM_BUILD_ROOT%{_datadir}/xml/metacity

%{!?with_gnome2:%{__rm} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties/metacity-wm.desktop}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmetacity-private.la

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
%doc AUTHORS NEWS README rationales.txt doc/theme-format.txt
%attr(755,root,root) %{_bindir}/metacity
%attr(755,root,root) %{_bindir}/metacity-message
%attr(755,root,root) %{_bindir}/metacity-theme-viewer
%attr(755,root,root) %{_bindir}/metacity-window-demo
%{_datadir}/GConf/gsettings/metacity-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.metacity.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-metacity-*.xml
%{?with_gnome2:%{_datadir}/gnome/wm-properties/metacity-wm.desktop}
%{_datadir}/xml/metacity
%{_datadir}/%{name}
%{_desktopdir}/metacity.desktop
%{_mandir}/man1/metacity*.1*

%files themes-Adwaita
%defattr(644,root,root,755)
%{_datadir}/themes/Adwaita

%files themes-AgingGorilla
%defattr(644,root,root,755)
%{_datadir}/themes/AgingGorilla

%files themes-Atlanta
%defattr(644,root,root,755)
%{_datadir}/themes/Atlanta

%files themes-Bright
%defattr(644,root,root,755)
%{_datadir}/themes/Bright

%files themes-Crux
%defattr(644,root,root,755)
%{_datadir}/themes/Crux

%files themes-Esco
%defattr(644,root,root,755)
%{_datadir}/themes/Esco

%files themes-HighContrast
%defattr(644,root,root,755)
%{_datadir}/themes/HighContrast

%files themes-Metabox
%defattr(644,root,root,755)
%{_datadir}/themes/Metabox

%files themes-Simple
%defattr(644,root,root,755)
%{_datadir}/themes/Simple

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmetacity-private.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmetacity-private.so.3

%files devel
%defattr(644,root,root,755)
%doc ChangeLog HACKING doc/dialogs.txt
%attr(755,root,root) %{_libdir}/libmetacity-private.so
%{_includedir}/metacity
%{_pkgconfigdir}/libmetacity-private.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmetacity-private.a
