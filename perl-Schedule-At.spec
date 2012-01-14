#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# need access to working atd
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Schedule
%define		pnam	At
Summary:	Schedule::At - an OS independent interface to 'at' UNIX command
Summary(pl.UTF-8):	Schedule::At - niezależny od platformy interfejs do polecenia 'at'
Name:		perl-Schedule-At
Version:	1.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e85ec1a885939c8caa5f58ac65ca0dd8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules provides an OS independent interface to 'at', the UNIX
command that allows you to execute commands at a specified time.

%description -l pl.UTF-8
Schedule::At udostępnia niezależny od platformy interfejs do 'at',
uniksowego polecenia, które pozwala na wykonanie komendy o określonym
czasie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Schedule/At.pm
%{_mandir}/man3/*
