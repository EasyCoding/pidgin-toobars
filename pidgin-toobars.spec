Name: pidgin-toobars
Version: 1.14
Release: 4%{?dist}
Summary: Adds toolbar and status bar to Pidgin buddy list

License: GPLv2+
Source0: http://vayurik.ru/wordpress/wp-content/uploads/toobars/%{version}/%{name}-%{version}.tar.gz
URL: http://vayurik.ru/wordpress/en/toobars/

BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(pidgin)
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

%files -f toobars.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/pidgin/toobars.so
%{_datadir}/pixmaps/pidgin/buttons/*.png

%changelog
* Mon Mar 27 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.14-4
- Added missing BR: gcc.

* Thu Nov 24 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.14-3
- Build against new Pidgin releases.

* Sat Jan 30 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.14-2
- Fixed SPEC. Added support of Fedora 22+.

* Mon Jul 29 2013 Vitaly Zaitsev <vitaly@easycoding.org> - 1.14-1
- Updated to v. 1.14. Fixed build under Fedora 19+.

