Summary:	Desktop Background Images.
Name:		desktop-backgrounds
Version:	1.0.0
Release:	6
Copyright:	LGPL
Group:		Applications/Multimedia
Source:		space-1.0.0.tar.gz
Source1:	gnome-tiles-1.0.0.tar.gz
Source2:	Propaganda-1.0.0.tar.gz
Source3:	README.Propaganda.gz
Source4:	README.space.gz
Source5:	PHOTO_FAQ.ps.gz
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome-imglib
BuildArchitectures:	noarch

%define		_prefix	/usr/X11R6

%description
If you use a desktop environment like GNOME you can use these images
to spruce up your background.

%description -l pl
Je¶li u¿ywa siê ¶rodowiska graficznego (np. GNOME), mo¿na wykorzystaæ 
te pakiety by t³o wygl±da³o bardziej estetycznie.

%prep
%setup -c %{name}-%{version} -T -D

cp %{SOURCE3} $RPM_BUILD_DIR/%{name}-%{version}
cp %{SOURCE4} $RPM_BUILD_DIR/%{name}-%{version}
cp %{SOURCE5} $RPM_BUILD_DIR/%{name}-%{version}

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
%{_datadir}/pixmaps/backgrounds/space
%{_datadir}/pixmaps/backgrounds/tiles
%{_datadir}/pixmaps/backgrounds/Propaganda
