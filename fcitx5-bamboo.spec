#
# spec file for package fcitx5-bamboo
#

Name:           fcitx5-bamboo
Version:        1.0.2
Release:        0
Summary:        Typing Vietnamese on Fcitx5 by Bamboo engine
License:        GPLv2.0+;  LGPLv2.0+
URL:            https://github.com/fcitx/fcitx5-bamboo
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gcc-c++
BuildRequires:  golang
BuildRequires:  hicolor-icon-theme
Requires:       fcitx5
Provides:       fcitx5-bamboo = %{version}

%description
Bamboo (Vietnamese Input Method) engine support for Fcitx
Based on https://github.com/BambooEngine/bamboo-core

%prep
%setup -q

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%find_lang %{name}

%files -f %{name}.lang
%license LICENSES
%doc README
%{_datadir}/locale
%{_libdir}/fcitx5/libbamboo.so
%{_datadir}/fcitx5
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Bamboo.metainfo.xml

%changelog
* Sun Nov 20 2022 1.0.2
- update to upstream release 1.0.2
