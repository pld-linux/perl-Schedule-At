%include	/usr/lib/rpm/macros.perl
%define	pdir	Schedule
%define	pnam	At
Summary:	Schedule::At perl module
Summary(pl):	Modu³ perla Schedule::At
Name:		perl-Schedule-At
Version:	1.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Schedule::At provides an OS independent interface to 'at' Unix command.

%description -l pl
Schedule::At udostêpnia niezale¿ny od platformy interfejs do polecenia
'at'.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_mandir}/man3/*
%{perl_sitelib}/Schedule/At.pm
