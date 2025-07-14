#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Parameterized testing with any Python test framework
Summary(pl.UTF-8):	Parametryzowane testowanie w dowolnym szkielecie testów pythonowych
Name:		python3-parameterized
Version:	0.9.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/parameterized/
Source0:	https://files.pythonhosted.org/packages/source/p/parameterized/parameterized-%{version}.tar.gz
# Source0-md5:	ed1bee2fb5d9044688d8503bdda9e6f3
Patch0:		tests.patch
Patch1:		parameterized-mock.patch
URL:		https://pypi.org/project/parameterized/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-setuptools >= 61.2
%if %{with tests}
BuildRequires:	python3-pynose
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parameterized testing with any Python test framework (nose, py.test,
unittest).

%description -l pl.UTF-8
Parametryzowane testowanie w dowolnym szkielecie testów pythonowych
(nose, py.test, unittest).

%prep
%setup -q -n parameterized-%{version}
%patch -P 0 -p1
%patch -P 1 -p1

%build
%py3_build_pyproject

%if %{with tests}
nosetests parameterized/test.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/parameterized/test.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/parameterized/__pycache__/test.*.py*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/parameterized
%{py3_sitescriptdir}/parameterized-%{version}.dist-info
