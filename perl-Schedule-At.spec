%include	/usr/lib/rpm/macros.perl
Summary:	Schedule-At perl module
Summary(pl):	Modu³ perla Schedule-At
Name:		perl-Schedule-At
Version:	1.02
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Schedule/Schedule-At-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Schedule-At provides an OS independent interface to 'at' Unix command.

%description -l pl
Schedule-At udostêpnia niezale¿ny od platformy interfejs do polecenia
'at'.

%prep
%setup -q -n Schedule-At-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Schedule/At.pm
%{perl_sitelib}/auto/Schedule/At
%{_mandir}/man3/*
