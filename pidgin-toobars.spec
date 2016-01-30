Name: pidgin-toobars
Version: 1.14
Release: 1%{?dist}
Summary: Adds toolbar and status bar to Pidgin buddy list

License: GPLv2+
Source0: http://vayurik.ru/wordpress/wp-content/uploads/toobars/%{version}/%{name}-%{version}.tar.gz
URL: http://vayurik.ru/wordpress/en/toobars/

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libpng-devel
BuildRequires: libtool
BuildRequires: pidgin-devel
BuildRequires: intltool

%description
Adds toolbar and status bar to Pidgin buddy list.

%prep
%setup -q -n %{name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake} --add-missing
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%find_lang toobars
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/toobars.la

%files -f toobars.lang
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/pidgin/toobars.so
%{_datarootdir}/pixmaps/pidgin/buttons/*.png

%changelog
* Mon Jul 29 2013 V1TSK <vitaly@easycoding.org> - 1.14-1
- Updated to v. 1.14. Fixed build under Fedora 19+.

