Summary:	GPE IRC client
Summary(pl.UTF-8):	Klient IRC GPE
Name:		gpe-irc
Version:	0.08
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	0f934a03d8c4d18a9a977ff704a741c5
URL:		http://gpe.linuxtogo.org/
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libgpewidget-devel
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE IRC client, for embedded devices.

%description -l pl.UTF-8
Klient IRC GPE dla urządzeń wbudowanych.

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	STRIP=/bin/true \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpe-irc
%{_desktopdir}/gpe-irc.desktop
%dir %{_datadir}/gpe/pixmaps/default/irc
%{_datadir}/gpe/pixmaps/default/irc/*.png
%dir %{_datadir}/gpe/pixmaps/default/irc/colors
%{_datadir}/gpe/pixmaps/default/irc/colors/*.png
%dir %{_datadir}/gpe/pixmaps/default/irc/smileys
%{_datadir}/gpe/pixmaps/default/irc/smileys/*.png
%{_pixmapsdir}/*.png
