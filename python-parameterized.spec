#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Parameterized testing with any Python test framework
Summary(pl.UTF-8):	Parametryzowane testowanie w dowolnym szkielecie testów pythonowych
Name:		python-parameterized
Version:	0.8.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/parameterized/
Source0:	https://files.pythonhosted.org/packages/source/p/parameterized/parameterized-%{version}.tar.gz
# Source0-md5:	30e34da8db0b31bbc5c0ed86cfa9e7c1
Patch0:		%{name}-mock.patch
URL:		https://pypi.org/project/parameterized/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parameterized testing with any Python test framework (nose, py.test,
unittest).

%description -l pl.UTF-8
Parametryzowane testowanie w dowolnym szkielecie testów pythonowych
(nose, py.test, unittest).

%package -n python3-parameterized
Summary:	Parameterized testing with any Python test framework
Summary(pl.UTF-8):	Parametryzowane testowanie w dowolnym szkielecie testów pythonowych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-parameterized
Parameterized testing with any Python test framework (nose, py.test,
unittest).

%description -n python3-parameterized -l pl.UTF-8
Parametryzowane testowanie w dowolnym szkielecie testów pythonowych
(nose, py.test, unittest).

%prep
%setup -q -n parameterized-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} parameterized/test.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} parameterized/test.py
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
%doc CHANGELOG.txt LICENSE.txt README.rst
%{py_sitescriptdir}/parameterized
%{py_sitescriptdir}/parameterized-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-parameterized
%defattr(644,root,root,755)
%doc CHANGELOG.txt LICENSE.txt README.rst
%{py3_sitescriptdir}/parameterized
%{py3_sitescriptdir}/parameterized-%{version}-py*.egg-info
%endif
