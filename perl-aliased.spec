#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	aliased
Summary:	aliased - use shorter versions of class names
Summary(pl.UTF-8):	aliased - używanie krótszych wersji nazw klas
Name:		perl-aliased
Version:	0.34
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/E/ET/ETHER/%{pdir}-%{version}.tar.gz
# Source0-md5:	f7f659f689699a87115da1262eb6edc6
URL:		https://metacpan.org/dist/aliased
BuildRequires:	perl-Module-Build-Tiny >= 0.039
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aliased is simple in concept but is a rather handy module. It loads
the class you specify and exports into your namespace a subroutine
that returns the class name. You can explicitly alias the class to
another name or, if you prefer, you can do so implicitly. In the
latter case, the name of the subroutine is the last part of the class
name. Thus, it does something similar to the following:

  #use aliased 'Some::Annoyingly::Long::Module::Name::Customer';

  use Some::Annoyingly::Long::Module::Name::Customer;
  sub Customer {
    return 'Some::Annoyingly::Long::Module::Name::Customer';
  }
  my $cust = Customer->new;

This module is useful if you prefer a shorter name for a class. It's
also handy if a class has been renamed.

%description -l pl.UTF-8
aliased jest prostym w założeniach, ale dosyć poręcznym modułem.
Ładuje podaną klasę i eksportuje do przestrzeni nazw funkcję
zwracającą nazwę tej klasy. Można nadać klasie alias jawnie lub
domyślnie - w drugim przypadku nazwa funkcji będzie ostatnią częścią
nazwy klasy. Czyli robi to coś podobnego do:

  #use aliased 'Jakas::Strasznie::Dluga::Nazwa::Modulu::Customer';

  use Jakas::Strasznie::Dluga::Nazwa::Modulu::Customer;
  sub Customer {
    return 'Jakas::Strasznie::Dluga::Nazwa::Modulu::Customer';
  }
  my $cust = Customer->new;

Ten moduł jest przydatny, kiedy wolimy mieć klasę dostępną pod krótszą
nazwą, a także w przypadku, kiedy nazwa klasy została zmieniona.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/aliased.pm
%{_mandir}/man3/aliased.3pm*
