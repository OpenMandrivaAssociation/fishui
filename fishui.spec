Name:           fishui
Version:        @SERVICE@
Release:        0
Summary:        Cutefish desktop interface library
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            https://github.com/cutefishos/fishui
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.15.2
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
 * ...

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other

%description devel
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
%cmake_install

%files
%doc README.md
%{_libqt5_archdatadir}/qml/FishUI
%dir %{_libqt5_archdatadir}/qml/QtQuick
%dir %{_libqt5_archdatadir}/qml/QtQuick/Controls.2
%{_libqt5_archdatadir}/qml/QtQuick/Controls.2/fish-style
%license LICENSE

%files devel
%dir %{_libdir}/cmake/
%{_libdir}/cmake/FishUI/
%{_libdir}/libFishUI.so
