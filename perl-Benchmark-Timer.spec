#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Benchmark
%define	pnam	Timer
Summary:	Benchmark::Timer - Perl code benchmarking tool
Summary(pl):	Benchmark::Timer - narz�dzie do testowania wydajno�ci kodu perlowego
Name:		perl-Benchmark-Timer
Version:	0.5
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	798b37903b9a8ae1624e9c745123f2eb
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

%description -l pl
Klasa Benchmark::Timer pozwala wygodnie mierzy� czas wykonywania
fragment�w kodu, a tak�e mierzy� wydajno�� kodu pozwalaj�c na
mierzenie czasu w powtarzanych pr�bach. Jest to idealne je�li
potrzebujemy bardziej precyzyjnej informacji o czasie dzia�ania
fragment�w kodu ni� mo�e da� modu� Benchmark, ale nie chcemy i�� na
ca�o�� i profilowa� kodu.

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
%dir %{perl_vendorlib}/Benchmark
%{perl_vendorlib}/Benchmark/Timer.pm
%{_mandir}/man3/*
