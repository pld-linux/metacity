# TODO:
# - something with %{_datadir}/themes/Theme dirs (some belong to gnome-themes,
#   some don't belong anywhere...)
Summary:	Metacity window manager
Summary(pl):	Zarz±dca okien metacity
Name:		metacity
Version:	2.6.1
Release:	4
License:	GPL
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	0380801dae821ff67b8c8cb3410ecb01
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-libtool.patch
URL:		http://people.redhat.com/~hp/metacity/
BuildRequires:	GConf2-devel >= 2.4.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.4
BuildRequires:	intltool >= 0.25
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.2.0
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	startup-notification-devel
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2 >= 2.4.0.1
Requires:	metacity-theme-base = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
Metacity is a simple window manager that integrates nicely with
GNOME2.

%description -l pl
Metacity jest prostym zarz±dc± okien ³adnie integruj±cym siê z GNOME2.

%package devel
Summary:	metacity - header files
Summary(pl):	metacity - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains header files for metcity window manager.

%description devel -l pl
Pakiet zawieraj±cy pliki nag³ówkowe zarz±dcy okien metacity.

%package static
Summary:	Static metacity library
Summary(pl):	Statyczna biblioteka metacity
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of metacity library.

%description static -l pl
Statyczna wersja biblioteki metacity.

%package themes-AgingGorilla
Summary:	AgingGorilla theme for metacity
Summary(pl):	Motyw AgingGorilla dla metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}
Provides:	metacity-theme-base = %{version}

%description themes-AgingGorilla
AgingGorilla theme for metacity.

%description themes-AgingGorilla -l pl
Motyw AgingGorilla dla metacity.

%package themes-Atlanta
Summary:	Atlanta theme for metacity
Summary(pl):	Motyw Atlanta dla metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}
Provides:	metacity-theme-base = %{version}

%description themes-Atlanta
Atlanta theme for metacity.

%description themes-Atlanta -l pl
Motyw Atlanta dla metacity.

%package themes-Bright
Summary:	Bright theme for metacity
Summary(pl):	Motyw Bright dla metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}
Provides:	metacity-theme-base = %{version}

%description themes-Bright
Bright theme for metacity.

%description themes-Bright -l pl
Motyw Bright dla metacity.

%package themes-Crux
Summary:	Crux theme for metacity
Summary(pl):	Motyw Crux dla metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}
Provides:	metacity-theme-base = %{version}

%description themes-Crux
Crux theme for metacity.

%description themes-Crux -l pl
Motyw Crux dla metacity.

%package themes-Esco
Summary:	Esco theme for metacity
Summary(pl):	Motyw Esco dla metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}
Provides:	metacity-theme-base = %{version}

%description themes-Esco
Esco theme for metacity.

%description themes-Esco -l pl
Motyw Esco dla metacity.

%package themes-Metabox
Summary:	Metabox theme for metacity
Summary(pl):	Motyw Metabox dla metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}
Provides:	metacity-theme-base = %{version}

%description themes-Metabox
Metabox theme for metacity.

%description themes-Metabox -l pl
Motyw Metabox dla metacity.

%package themes-Simple
Summary:	Simple theme for metacity
Summary(pl):	Motyw Simple dla metacity
Group:		Themes/Gtk
Requires:	%{name} = %{version}
Provides:	metacity-theme-base = %{version}

%description themes-Simple
Simple theme for metacity.

%description themes-Simple -l pl
Motyw Simple dla metacity.

%prep
%setup -q
%patch0 -p1

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
install -d $RPM_BUILD_ROOT%{_datadir}/{xml/metacity,xsessions}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopfilesdir=%{_wmpropsdir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

install doc/metacity-theme.dtd $RPM_BUILD_ROOT%{_datadir}/xml/metacity
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS doc/theme-format.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/metacity-dialog
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/metacity.desktop
%{_sysconfdir}/gconf/schemas/*
%{_pixmapsdir}/*
%{_datadir}/xml/metacity

%files themes-AgingGorilla
%defattr(644,root,root,755)
%{_datadir}/themes/AgingGorilla/*

%files themes-Atlanta
%defattr(644,root,root,755)
%{_datadir}/themes/Atlanta/*

%files themes-Bright
%defattr(644,root,root,755)
%{_datadir}/themes/Bright/*

%files themes-Crux
%defattr(644,root,root,755)
%{_datadir}/themes/Crux/*

%files themes-Esco
%defattr(644,root,root,755)
%{_datadir}/themes/Esco/*

%files themes-Metabox
%defattr(644,root,root,755)
%{_datadir}/themes/Metabox/*

%files themes-Simple
%defattr(644,root,root,755)
%{_datadir}/themes/Simple/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
