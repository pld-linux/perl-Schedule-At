%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Schedule-At perl module
Summary(pl):	Modu� perla Schedule-At
Name:		perl-Schedule-At
Version:	1.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Schedule/Schedule-At-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Schedule-At provides an OS independent interface to 'at' Unix command. 

%description -l pl
Schedule-At udost�pnia niezale�ny od platformy interfejs do polecenia 'at'.

%prep
%setup -q -n Schedule-At-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Schedule/At
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Schedule/At.pm
%{perl_sitelib}/auto/Schedule/At
%{perl_sitearch}/auto/Schedule/At

%{_mandir}/man3/*
