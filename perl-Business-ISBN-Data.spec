Name:           perl-Business-ISBN-Data
Version:        20081208
Release:        2%{?dist}
Summary:        The data pack for Business::ISBN

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Business-ISBN-Data/
Source0:        http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/Business-ISBN-Data-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Prereq)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is a data pack for Business::ISBN.  You can update
the ISBN data without changing the version of Business::ISBN.
Most of the interesting stuff is in Business::ISBN.


%prep
%setup -q -n Business-ISBN-Data-%{version}

# Filter unwanted Provides:
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
  sed -e '/perl(Business::ISBN)/d'
EOF

%define __perl_provides %{_builddir}/Business-ISBN-Data-%{version}/%{name}-prov
chmod +x %{__perl_provides}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README LICENSE examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 20081208-2
- rebuild against perl 5.10.1

* Mon Oct  5 2009 Stepan Kasal <skasal@redhat.com> - 20081208-1
- new upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Stepan Kasal <skasal@redhat.com> - 20081020-1
- new upstream version

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.15-4
- rebuild for new perl

* Thu Nov 15 2007 Robin Norwood <rnorwood@redhat.com> - 1.15-3
- Should not provide perl(Business::ISBN)

* Thu Oct 25 2007 Robin Norwood <rnorwood@redhat.com> - 1.15-2
- Fix BuildRequires

* Thu Oct 25 2007 Robin Norwood <rnorwood@redhat.com> - 1.15-1
- Initial build
