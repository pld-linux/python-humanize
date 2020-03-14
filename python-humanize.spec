# NOTE: for 1.1.0+ (for python3.5+) see python3-humanize.spec
#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-humanize now)

Summary:	Python 2 humanize utilities
Summary(pl.UTF-8):	Narzędzia Pythona 2 humanize
Name:		python-humanize
# keep 1.0.x here (last version that supports Python 2.7)
Version:	1.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/humanize/
Source0:	https://files.pythonhosted.org/packages/source/h/humanize/humanize-%{version}.tar.gz
# Source0-md5:	9f1eecc0ef17f4eecc60a29e3889d72a
URL:		https://pypi.org/project/humanize/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-freezegun
BuildRequires:	python-mock
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-freezegun
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modest package contains various common humanization utilities,
like turning a number into a fuzzy human readable duration ('3 minutes
ago') or into a human readable size or throughput.

%description -l pl.UTF-8
Ten skromny pakiet zawiera różne narzędzia do ogólnej poprawy
interakcji z ludźmi - jak zamiana liczby na przybliżoną formę czytelną
dla człowieka ("3 minuty temu") albo czytelny dla człowieka rozmiar
czy przepustowość.

%package -n python3-humanize
Summary:	Python 3 humanize utilities
Summary(pl.UTF-8):	Narzędzia Pythona 3 humanize
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-humanize
This modest package contains various common humanization utilities,
like turning a number into a fuzzy human readable duration ('3 minutes
ago') or into a human readable size or throughput.

%description -n python3-humanize -l pl.UTF-8
Ten skromny pakiet zawiera różne narzędzia do ogólnej poprawy
interakcji z ludźmi - jak zamiana liczby na przybliżoną formę czytelną
dla człowieka ("3 minuty temu") albo czytelny dla człowieka rozmiar
czy przepustowość.

%prep
%setup -q -n humanize-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENCE README.md
%{py_sitescriptdir}/humanize
%{py_sitescriptdir}/humanize-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-humanize
%defattr(644,root,root,755)
%doc LICENCE README.md
%{py3_sitescriptdir}/humanize
%{py3_sitescriptdir}/humanize-%{version}-py*.egg-info
%endif
