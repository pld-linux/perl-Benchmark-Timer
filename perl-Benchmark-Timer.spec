#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Benchmark
%define		pnam	Timer
Summary:	Benchmark::Timer - Perl code benchmarking tool
Summary(pl.UTF-8):	Benchmark::Timer - narzędzie do testowania wydajności kodu perlowego
Name:		perl-Benchmark-Timer
Version:	0.7102
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d79a85ebdd458a34b5e979b636f5128b
URL:		http://search.cpan.org/dist/Benchmark-Timer/
BuildRequires:	perl-Statistics-TTest
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Benchmark::Timer class allows you to time portions of code
conveniently, as well as benchmark code by allowing timings of
repeated trials. It is perfect for when you need more precise
information about the running time of portions of your code than the
Benchmark module will give you, but don't want to go all out and
profile your code.

%description -l pl.UTF-8
Klasa Benchmark::Timer pozwala wygodnie mierzyć czas wykonywania
fragmentów kodu, a także mierzyć wydajność kodu pozwalając na
mierzenie czasu w powtarzanych próbach. Jest to idealne jeśli
potrzebujemy bardziej precyzyjnej informacji o czasie działania
fragmentów kodu niż może dać moduł Benchmark, ale nie chcemy iść na
całość i profilować kodu.

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
%doc CHANGES README
%dir %{perl_vendorlib}/Benchmark
%{perl_vendorlib}/Benchmark/Timer.pm
%{_mandir}/man3/*
