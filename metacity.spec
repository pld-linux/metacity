Summary:	Metacity window manager
Summary(pl):	Zarz±dca okien metacity
Name:		metacity
Version:	2.3.89
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://people.redhat.com/~hp/metacity/%{name}-%{version}.tar.gz
URL:		http://people.redhat.com/~hp/metacity/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1.3.10
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

%build
#rm -f missing
#aclocal
#autoconf
#automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS NEWS

%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
%{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/metacity.schemas > /dev/null 2>&1


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_datadir}/%{name}
%{_datadir}/gnome/wm-properties/metacity.desktop
%{_sysconfdir}/gconf/schemas/*
