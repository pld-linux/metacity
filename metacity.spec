#
# TODO:
# - something with %{_datadir}/themes/Theme dirs (some belong to gnome-themes,
#   some don't belong anywhere...)
# - metacity requires itself (links with installed libmetacity-private
#   instead of linking with built one?)
#
Summary:	Metacity window manager
Summary(pl):	Zarz±dca okien Metacity
Name:		metacity
Version:	2.8.2
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	4e37347f772f726e87d325f219da0ce8
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-swap-resize-button.patch
Patch3:		%{name}-disable-prevention-focus-stealing-logic.patch
BuildRequires:	GConf2-devel >= 2.6.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	intltool >= 0.25
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.4.0
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	startup-notification-devel >= 0.7
Requires(post):	GConf2 >= 2.6.1
Requires:	%{name}-libs = %{version}-%{release}
Requires:	metacity-theme-base = %{version}-%{release}
Provides:	gnome-wm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
Metacity is a simple window manager that integrates nicely with
GNOME2.

%description -l pl
Metacity jest prostym zarz±dc± okien ³adnie integruj±cym siê z GNOME2.

%package libs
Summary:	Metacity - libraries
Summary(pl):	Metacity - biblioteki
Group:		X11/Libraries
Conflicts:	metacity <= 2.6.3-4

%description libs
This package contains libraries for Metacity window manager.

%description libs -l pl
Pakiet zawieraj±cy biblioteki zarz±dcy okien Metacity.

%package devel
Summary:	Metacity - header files
Summary(pl):	Metacity - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains header files for Metacity window manager.

%description devel -l pl
Pakiet zawieraj±cy pliki nag³ówkowe zarz±dcy okien Metacity.

%package static
Summary:	Static Metacity library
Summary(pl):	Statyczna biblioteka Metacity
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of Metacity library.

%description static -l pl
Statyczna wersja biblioteki Metacity.

%package themes-AgingGorilla
Summary:	AgingGorilla theme for Metacity
Summary(pl):	Motyw AgingGorilla dla Metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}-%{release}
Provides:	metacity-theme-base = %{version}-%{release}

%description themes-AgingGorilla
AgingGorilla theme for Metacity.

%description themes-AgingGorilla -l pl
Motyw AgingGorilla dla Metacity.

%package themes-Atlanta
Summary:	Atlanta theme for Metacity
Summary(pl):	Motyw Atlanta dla Metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}-%{release}
Provides:	metacity-theme-base = %{version}-%{release}

%description themes-Atlanta
Atlanta theme for Metacity.

%description themes-Atlanta -l pl
Motyw Atlanta dla Metacity.

%package themes-Bright
Summary:	Bright theme for Metacity
Summary(pl):	Motyw Bright dla Metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}-%{release}
Provides:	metacity-theme-base = %{version}-%{release}

%description themes-Bright
Bright theme for Metacity.

%description themes-Bright -l pl
Motyw Bright dla Metacity.

%package themes-Crux
Summary:	Crux theme for Metacity
Summary(pl):	Motyw Crux dla Metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}-%{release}
Provides:	metacity-theme-base = %{version}-%{release}

%description themes-Crux
Crux theme for Metacity.

%description themes-Crux -l pl
Motyw Crux dla Metacity.

%package themes-Esco
Summary:	Esco theme for Metacity
Summary(pl):	Motyw Esco dla Metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}-%{release}
Provides:	metacity-theme-base = %{version}-%{release}

%description themes-Esco
Esco theme for Metacity.

%description themes-Esco -l pl
Motyw Esco dla Metacity.

%package themes-Metabox
Summary:	Metabox theme for Metacity
Summary(pl):	Motyw Metabox dla Metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}-%{release}
Provides:	metacity-theme-base = %{version}-%{release}

%description themes-Metabox
Metabox theme for Metacity.

%description themes-Metabox -l pl
Motyw Metabox dla Metacity.

%package themes-Simple
Summary:	Simple theme for Metacity
Summary(pl):	Motyw Simple dla Metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}-%{release}
Provides:	metacity-theme-base = %{version}-%{release}

%description themes-Simple
Simple theme for Metacity.

%description themes-Simple -l pl
Motyw Simple dla Metacity.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

mv po/{no,nb}.po

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xml/metacity

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopfilesdir=%{_wmpropsdir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

install doc/metacity-theme.dtd $RPM_BUILD_ROOT%{_datadir}/xml/metacity

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README rationales.txt doc/theme-format.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/metacity-dialog
%{_datadir}/%{name}
%{_wmpropsdir}/metacity.desktop
%{_sysconfdir}/gconf/schemas/*
%{_pixmapsdir}/*
%{_datadir}/xml/metacity

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
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog HACKING doc/dialogs.txt
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
