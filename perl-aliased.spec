#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	aliased
Summary:	aliased - Use shorter versions of class names.
Summary(pl.UTF-8):	aliased - używaj krótszej wersji nazw klas.
Name:		perl-aliased
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/O/OV/OVID/%{pdir}-%{version}.tar.gz
# Source0-md5:	06cace025aa108fe4a9af3ae26bb297e
URL:		http://search.cpan.org/dist/aliased/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aliased is simple in concept but is a rather handy module.  It loads the
class you specify and exports into your namespace a subroutine that returns
the class name.  You can explicitly alias the class to another name or, if you
prefer, you can do so implicitly.  In the latter case, the name of the
subroutine is the last part of the class name.  Thus, it does something
similar to the following:

  #use aliased 'Some::Annoyingly::Long::Module::Name::Customer';

  use Some::Annoyingly::Long::Module::Name::Customer;
  sub Customer {
    return 'Some::Annoyingly::Long::Module::Name::Customer';
  }
  my $cust = Customer->new;

This module is useful if you prefer a shorter name for a class.  It's also
handy if a class has been renamed.

(Some may object to the term "aliasing" because we're not aliasing one
namespace to another, but it's a handy term.  Just keep in mind that this is
done with a subroutine and not with typeglobs and weird namespace munging.)

Note that this is only for useing OO modules.  You cannot use this to
load procedural modules.  See the Why OO Only? section.  Also,
don't let the version number fool you.  This code is ridiculously simple and
is just fine for most use.



%description -l pl.UTF-8
aliased jest prostym w założeniach, ale raczej poręcznym modułem. Ładuje klasy
które zostały wymienione i eksportuje je do przestrzeni nazw.

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
%{perl_vendorlib}//*.pm
%{_mandir}/man3/*
