Summary:	Metacity window manager
Summary(pl):	Zarz±dca okien metacity
Name:		metacity
Version:	2.4.34
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.4/%{name}-%{version}.tar.bz2
Patch0:		%{name}-gconf.patch
Patch1:		%{name}-libtool.patch
URL:		http://people.redhat.com/~hp/metacity/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	startup-notification-devel
BuildRequires:	Xft-devel >= 2.1
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
	pkgconfigdir=%{_pkgconfigdir}

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/themes
for i in `ls $RPM_BUILD_ROOT%{_datadir}/themes/`
do
	ln -s %{_datadir}/themes/$i/metacity-1 $RPM_BUILD_ROOT%{_datadir}/%{name}/themes/$i
done

%find_lang %{name}

%post
umask 022
%gconf_schema_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_datadir}/%{name}
%{_datadir}/gnome/wm-properties/metacity.desktop
%{_sysconfdir}/gconf/schemas/*
%{_pixmapsdir}/*
#%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/themes/Atlanta/metacity-1
%{_datadir}/themes/Bright/metacity-1
%{_datadir}/themes/Crux/metacity-1
%{_datadir}/themes/Esco/metacity-1
%{_datadir}/themes/AgingGorilla/metacity-1
%{_datadir}/themes/Metabox/metacity-1

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*
%{_includedir}/*
