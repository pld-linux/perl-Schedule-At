#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Schedule
%define		pnam	At
Summary:	Schedule::At - an OS independent interface to 'at' Unix command
Summary(pl):	Schedule::At - niezale�ny od platformy interfejs do polecenia 'at'
Name:		perl-Schedule-At
Version:	1.04
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	531e72d6b5cb3c69926135998348fa83
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules provides an OS independent interface to 'at', the Unix
command that allows you to execute commands at a specified time.

%description -l pl
Schedule::At udost�pnia niezale�ny od platformy interfejs do 'at',
Uniksowego polecenia, kt�re pozwala Ci na wykonanie komendy o okre�lonym
czasie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

# You need access to working atd to perform the tests...
%{?with_tests:%{__make} test}

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
