Name: pidgin-toobars
Version: 1.14
Release: 2%{?dist}
Summary: Adds toolbar and status bar to Pidgin buddy list

License: GPLv2+
Source0: http://vayurik.ru/wordpress/wp-content/uploads/toobars/%{version}/%{name}-%{version}.tar.gz
URL: http://vayurik.ru/wordpress/en/toobars/

BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(pidgin)

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: intltool
BuildRequires: gcc

%description
Adds toolbar and status bar to Pidgin buddy list.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%find_lang toobars
rm -f %{buildroot}%{_libdir}/pidgin/toobars.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f toobars.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/pidgin/toobars.so
%{_datadir}/pixmaps/pidgin/buttons/*.png

%changelog
* Thu Jan 30 2016 V1TSK <vitaly@easycoding.org> - 1.14-2
- Fixed SPEC. Added support of Fedora 22+.

* Mon Jul 29 2013 V1TSK <vitaly@easycoding.org> - 1.14-1
- Updated to v. 1.14. Fixed build under Fedora 19+.

