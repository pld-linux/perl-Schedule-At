#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Schedule
%define		pnam	At
Summary:	Schedule::At - an OS independent interface to 'at' Unix command
Summary(pl):	Schedule::At - niezale¿ny od platformy interfejs do polecenia 'at'
Name:		perl-Schedule-At
Version:	1.04
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules provides an OS independent interface to 'at', the Unix
command that allows you to execute commands at a specified time.

%description -l pl
Schedule::At udostêpnia niezale¿ny od platformy interfejs do 'at',
Uniksowego polecenia, które pozwala Ci na wykonanie komendy o okre¶lonym
czasie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

# You need access to working atd to perform the tests...
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Schedule/At.pm
%{_mandir}/man3/*
