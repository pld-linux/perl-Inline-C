#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Inline
%define		pnam	C
Summary:	Inline::C - C Language Support for Inline
Summary(pl.UTF-8):	Inline::C - obsługa języka C dla Inline
Name:		perl-Inline-C
Version:	0.76
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Inline/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c0fbfdd058075c9271a1384c822c9a87
URL:		http://search.cpan.org/dist/Inline-C/
BuildRequires:	perl-File-ShareDir-Install
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Copy-Recursive
BuildRequires:	perl-IO-All
BuildRequires:	perl-Inline >= 1:0.79
BuildRequires:	perl-Parse-RecDescent >= 1.967009
BuildRequires:	perl-Pegex >= 0.58
BuildRequires:	perl-Test-Warn >= 0.23
BuildRequires:	perl-YAML-LibYAML
%endif
Requires:	gcc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::C is a module that allows you to write Perl subroutines in C.
Since version 0.30 the Inline module supports multiple programming
languages and each language has its own support module.

%description -l pl.UTF-8
Inline::C to moduł pozwalający na pisanie funkcji Perla w języku C. Od
wersji 0.30 moduł Inline obsługuje wiele języków programowania, a
każdy język ma własny moduł obsługujący.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Inline/C.pod

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Inline/C.pm
%{perl_vendorlib}/Inline/C
%{perl_vendorlib}/auto/share/dist/Inline-C
%{_mandir}/man3/Inline::C.3pm*
%{_mandir}/man3/Inline::C::Cookbook.3pm*
%{_mandir}/man3/Inline::C::ParsePegex.3pm*
%{_mandir}/man3/Inline::C::ParseRecDescent.3pm*
%{_mandir}/man3/Inline::C::ParseRegExp.3pm*
%{_examplesdir}/%{name}-%{version}
