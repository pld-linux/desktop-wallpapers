Summary:	Desktop Background Images
Summary(pl):	Obrazki na t³o pulpitu
Name:		desktop-backgrounds
Version:	1.0.0
Release:	6
License:	LGPL
Group:		X11/Applications/Multimedia
Source0:	space-%{version}.tar.gz
Source1:	gnome-tiles-%{version}.tar.gz
Source2:	Propaganda-%{version}.tar.gz
Source3:	README.Propaganda.gz
Source4:	README.space.gz
Source5:	PHOTO_FAQ.ps.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome-imglib
BuildArch:	noarch


%description
If you use a desktop environment like GNOME you can use these images
to spruce up your background.

%description -l pl
Je¶li u¿ywa siê ¶rodowiska graficznego (np. GNOME), mo¿na wykorzystaæ
te pakiety by t³o wygl±da³o bardziej estetycznie.

%prep
%setup -q -c %{name}-%{version} -T -D

cp -f %{SOURCE3} %{SOURCE4} %{SOURCE5} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps/backgrounds
cd $RPM_BUILD_ROOT%{_datadir}/pixmaps/backgrounds
tar xzf %{SOURCE0}
tar xzf %{SOURCE1}
tar xzf %{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README.space,README.Propaganda,PHOTO_FAQ.ps}.gz
%{_pixmapsdir}/backgrounds/space
%{_pixmapsdir}/backgrounds/tiles
%{_pixmapsdir}/backgrounds/Propaganda
