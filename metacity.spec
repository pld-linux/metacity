#
# TODO:
# - something with %{_datadir}/themes/Theme dirs (some belong to gnome-themes,
#   some don't belong anywhere...)
# - metacity requires itself (links with installed libmetacity-private
#   instead of linking with built one?)
#
#
# Conditional build:
%bcond_with	gnome2		# build with support for GNOME2 wm-properties
#
Summary:	Metacity window manager
Summary(pl.UTF-8):	Zarządca okien Metacity
Name:		metacity
Version:	2.34.2
Release:	1
Epoch:		2
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/metacity/2.34/%{name}-%{version}.tar.xz
# Source0-md5:	c8d661a9f232d826c5f21bc0bff0a3e6
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.11.1
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.6.0
BuildRequires:	gnome-doc-utils >= 0.9.0
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libgtop-devel
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libSM-devel
# do we want to patch it?
BuildRequires:	zenity
BuildRequires:	xz >= 1:4.999.7
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
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
Requires:	gtk+2-devel >= 2:2.20.0

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
	--disable-schemas-install \
	--enable-compositor
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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install metacity.schemas

%preun
%gconf_schema_uninstall metacity.schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README rationales.txt doc/theme-format.txt
%attr(755,root,root) %{_bindir}/metacity
%attr(755,root,root) %{_bindir}/metacity-message
%attr(755,root,root) %{_bindir}/metacity-theme-viewer
%attr(755,root,root) %{_bindir}/metacity-window-demo
%{_datadir}/%{name}
%{_desktopdir}/metacity.desktop
%{_sysconfdir}/gconf/schemas/metacity.schemas
%{_datadir}/gnome-control-center/keybindings/*.xml
%{?with_gnome2:%{_datadir}/gnome/wm-properties/metacity-wm.desktop}
%{_datadir}/xml/metacity
%{_mandir}/man1/metacity*.1*

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

%files themes-Metabox
%defattr(644,root,root,755)
%{_datadir}/themes/Metabox

%files themes-Simple
%defattr(644,root,root,755)
%{_datadir}/themes/Simple

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmetacity-private.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmetacity-private.so.0

%files devel
%defattr(644,root,root,755)
%doc ChangeLog HACKING doc/dialogs.txt
%attr(755,root,root) %{_libdir}/libmetacity-private.so
%{_includedir}/metacity-1
%{_pkgconfigdir}/libmetacity-private.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmetacity-private.a
