%define _debugsource_template %{nil}
%define module merge3

Name:		python-merge3
Version:	0.0.16
Release:	1
Summary:	Python implementation of 3-way merge of texts
License:	GPL-2.0-or-later
Group:		Development/Python
URL:		https://github.com/breezy-team/merge3
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
A Python implementation of 3-way merge of texts.

Given BASE, OTHER, THIS, tries to produce a combined text
incorporating the changes from both BASE->OTHER and BASE->THIS.

All three will typically be sequences of lines.

%files
%doc README.rst
%{_bindir}/merge3
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
