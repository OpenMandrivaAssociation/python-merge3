%global           pypi_name merge3
%define debug_package %nil

Name:             python-%{pypi_name}
Version:          0.0.15
Release:          2

Summary:          Python implementation of 3-way merge of texts
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/tzlocal/
Source0:	https://files.pythonhosted.org/packages/source/%(echo %pypi_name | cut -c 1)/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
BuildRequires:	python3dist(setuptools-scm)

%description
A Python implementation of 3-way merge of texts.

Given BASE, OTHER, THIS, tries to produce a combined text
incorporating the changes from both BASE->OTHER and BASE->THIS.

All three will typically be sequences of lines.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
#rm -rf %{pypi_name}.egg-info

%build
%py3_build


%install
%py3_install

%files -n python-%{pypi_name}
%doc README.rst
%{_bindir}/merge3
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}.dist-info


