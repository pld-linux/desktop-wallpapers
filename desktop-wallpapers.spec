%define  ver     1.0.0
%define  rel     6
%define  prefix  /usr

Summary: Desktop Background Images.
Name: desktop-backgrounds
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/Multimedia
Source: space-1.0.0.tar.gz
Source1: gnome-tiles-1.0.0.tar.gz
Source2: Propaganda-1.0.0.tar.gz
Source3: README.Propaganda
Source4: README.space
Source5: PHOTO_FAQ.ps

BuildRoot:	/tmp/%{name}-%{version}-root

Obsoletes: gnome-imglib

Docdir: %{prefix}/doc
BuildArchitectures: noarch

%description
If you use a desktop environment like GNOME you can use these images
to spruce up your background.

%prep
%setup -c desktop-backgrounds-%{ver} -T -D

cp %{SOURCE3} $RPM_BUILD_DIR/desktop-backgrounds-%{ver}
cp %{SOURCE4} $RPM_BUILD_DIR/desktop-backgrounds-%{ver}
cp %{SOURCE5} $RPM_BUILD_DIR/desktop-backgrounds-%{ver}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/pixmaps/backgrounds
cd $RPM_BUILD_ROOT%{prefix}/share/pixmaps/backgrounds
tar xzf %{SOURCE0}
tar xzf %{SOURCE1}
tar xzf %{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Apr  2 1999 Jonathan Blandford <jrb@redhat.com>
- added propaganda tiles.  Spruced it up a bit
- moved README files out of tarball, and into docs dir.

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- First attempt

%files
%defattr(-,root,root)
%doc README.space README.Propaganda PHOTO_FAQ.ps
%{prefix}/share/pixmaps/backgrounds/space
%{prefix}/share/pixmaps/backgrounds/tiles
%{prefix}/share/pixmaps/backgrounds/Propaganda
