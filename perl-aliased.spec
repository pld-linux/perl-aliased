#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	aliased
Summary:	aliased - use shorter versions of class names
Summary(pl.UTF-8):	aliased - używanie krótszych wersji nazw klas
Name:		perl-aliased
Version:	0.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/O/OV/OVID/%{pdir}-%{version}.tar.gz
# Source0-md5:	8c2ee486901dae7d1c31e9a2d69c6c8f
URL:		http://search.cpan.org/dist/aliased/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/aliased.pm
%{_mandir}/man3/aliased.3pm*
