%define _empty_manifest_terminate_build 0

%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Name:           fishui
Version:        0.8
Release:        1
Summary:        Cutefish desktop interface library
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            https://github.com/cutefishos/fishui
Source:         https://github.com/cutefishos/fishui/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(ECM)
#BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-shape)

%description
FishUI is a GUI library based on QQC2 (Qt Quick Controls 2), every Cutefish
application uses it.
Features:
 * Light and Dark Mode
 * Borderless window (XCB Window move & resize)
 * Blurred window
 * Window shadow
 * Desktop-level menu
 * The style of the Qt Quick control
 
%package -n %{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries
Provides:       fishui

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:        %{libname} = %{version}-%{release}
Provides:        %{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name} including headers and libraries

%prep
%autosetup -p1
sed -i '/QtQuick.Layout 1/s/Layout /Layouts /' src/controls/Dialog.qml

%build
#%%cmake
mkdir -p build
pushd ./build
# FIXME: you should use the %%cmake macros
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build
popd

%install
%make_install -C build

%files -n %{libname}
%doc README.md
%license LICENSE
%{_libdir}/qt5/qml/QtQuick/Controls.2/fish-style
%{_libdir}/qt5/qml/FishUI

%files -n %{devname}
%dir %{_libdir}/cmake/
%{_libdir}/cmake/FishUI/
%{_libdir}/libFishUI.so
