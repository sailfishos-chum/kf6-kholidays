%global  kf_version 6.6.0

Name: kf6-kholidays
Version: 6.6.0
Release: 0%{?dist}
Summary: KDE Frameworks Library to assist determining when holidays occur
License: LGPLv2+
URL:     https://invent.kde.org/frameworks/kcalendarcore
Source0: %{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  kf6-extra-cmake-modules >= %{majmin_ver_kf6}
BuildRequires:  kf6-rpm-macros
BuildRequires:  make

BuildRequires: kf6-kconfig-devel >= %{majmin_ver_kf6}

#BuildRequires: pkgconfig(libcanberra)

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qtdeclarative-devel


%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang_kf6 libkholidays6_qt

%files -f libkholidays6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Holidays.so.*
%{_kf6_qmldir}/org/kde/kholidays/

%files devel
%{_kf6_includedir}/KHolidays/
%{_kf6_libdir}/libKF6Holidays.so
%{_kf6_libdir}/cmake/KF6Holidays/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
