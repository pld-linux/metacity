Summary:	Metacity window manager
Summary(pl):	Zarz±dca okien metacity
Name:		metacity
Version:	2.4.0
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://people.redhat.com/~hp/metacity/%{name}-%{version}.tar.gz
Patch0:		%{name}-gconf.patch
URL:		http://people.redhat.com/~hp/metacity/
BuildRequires:	GConf2-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libtool
BuildRequires:	intltool >= 0.22
BuildRequires:	libglade2-devel >= 2.0.0
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2

%description
Metacity is a simple window manager that integrates nicely with
GNOME2.

%description -l pl
Metacity jest prostym zarz±dc± okien ³adnie integruj±cym siê z GNOME2.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%find_lang %{name}

%post
GCONF_CONFIG_SOURCE="" \
%{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

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
%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/themes/Atlanta/metacity-1
%{_datadir}/themes/Bright/metacity-1
%{_datadir}/themes/Crux/metacity-1
%{_datadir}/themes/Esco/metacity-1
%{_datadir}/themes/Gorilla/metacity-1
%{_datadir}/themes/Metabox/metacity-1
