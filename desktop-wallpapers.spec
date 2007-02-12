Summary:	Desktop Background Images
Summary(pl.UTF-8):   Obrazki na tło pulpitu
Name:		desktop-wallpapers
Version:	1.0.0
Release:	7
License:	LGPL
Group:		X11/Applications/Multimedia
Source0:	space-%{version}.tar.gz
# Source0-md5:	fa40848b6f9377cecbbc9a8ade54cc20
Source1:	gnome-tiles-%{version}.tar.gz
# Source1-md5:	f754e713421bf2c38c4d318794a50c80
Source2:	Propaganda-%{version}.tar.gz
# Source2-md5:	9a41ff73a67967715010ed6703898aad
Source3:	README.Propaganda.gz
# Source3-md5:	93cc41eedf423557b3016af7e952fe42
Source4:	README.space.gz
# Source4-md5:	bf99dba5452a01cf7334a1a2d79c4ca4
Source5:	PHOTO_FAQ.ps.gz
# Source5-md5:	11e011110e96d43dcafaae9dc1bba80b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome-imglib
Obsoletes:	desktop-backgrounds
BuildArch:	noarch


%description
If you use a desktop environment like GNOME you can use these images
to spruce up your background.

%description -l pl.UTF-8
Jeśli używa się środowiska graficznego (np. GNOME), można wykorzystać
te pakiety by tło wyglądało bardziej estetycznie.

%prep
%setup -q -c %{name}-%{version} -T -D

cp -f %{SOURCE3} %{SOURCE4} %{SOURCE5} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/wallpapers
cd $RPM_BUILD_ROOT%{_datadir}/wallpapers
tar xzf %{SOURCE0}
tar xzf %{SOURCE1}
tar xzf %{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README.space,README.Propaganda,PHOTO_FAQ.ps}.gz
%{_datadir}/wallpapers/space
%{_datadir}/wallpapers/tiles
%{_datadir}/wallpapers/Propaganda
