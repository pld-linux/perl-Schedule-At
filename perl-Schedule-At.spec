%include	/usr/lib/rpm/macros.perl
%define		pdir	Schedule
%define		pnam	At
Summary:	Schedule::At Perl module
Summary(cs):	Modul Schedule::At pro Perl
Summary(da):	Perlmodul Schedule::At
Summary(de):	Schedule::At Perl Modul
Summary(es):	Módulo de Perl Schedule::At
Summary(fr):	Module Perl Schedule::At
Summary(it):	Modulo di Perl Schedule::At
Summary(ja):	Schedule::At Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Schedule::At ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Schedule::At
Summary(pl):	Modu³ Perla Schedule::At
Summary(pt):	Módulo de Perl Schedule::At
Summary(pt_BR):	Módulo Perl Schedule::At
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Schedule::At
Summary(sv):	Schedule::At Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Schedule::At
Summary(zh_CN):	Schedule::At Perl Ä£¿é
Name:		perl-Schedule-At
Version:	1.03
Release:	2
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
%{perl_sitelib}/Schedule
%{_mandir}/man3/*
