Summary:	Metacity window manager
Summary(pl):	Zarz±dca okien metacity
Name:		metacity
Version:	2.5.1
Release:	2
License:	GPL
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
Patch0:		%{name}-gconf.patch
Patch1:		%{name}-libtool.patch
URL:		http://people.redhat.com/~hp/metacity/
BuildRequires:	GConf2-devel >= 2.3.0
BuildRequires:	Xft-devel >= 2.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.2.0
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	startup-notification-devel
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2 >= 2.3.0
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
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
                                                                                
%description static
Static version of metacity library.
                                                                                
%description static -l pl
Statyczna wersja biblioteki metacity.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-startup-notification
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	desktopfilesdir=%{_wmpropsdir}

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/themes
for i in `ls $RPM_BUILD_ROOT%{_datadir}/themes/`
do
	ln -s %{_datadir}/themes/$i/metacity-1 $RPM_BUILD_ROOT%{_datadir}/%{name}/themes/$i
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/metacity-dialog
%{_datadir}/%{name}
%{_wmpropsdir}/metacity.desktop
%{_sysconfdir}/gconf/schemas/*
%{_pixmapsdir}/*
#%%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/themes/Atlanta/metacity-1
%{_datadir}/themes/Bright/metacity-1
%{_datadir}/themes/Crux/metacity-1
%{_datadir}/themes/Esco/metacity-1
%{_datadir}/themes/AgingGorilla/metacity-1
%{_datadir}/themes/Metabox/metacity-1
%{_datadir}/themes/Simple/metacity-1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
