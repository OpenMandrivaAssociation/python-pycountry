%define module pycountry

Name:		python-pycountry
Summary:	Databases for ISO standards 639 3166 3166-2 4217 15924
Version:	26.2.16
Release:	1
License:	LGPL-2.1-only
Group:		Development/Python
URL:		https://pypi.python.org/pypi/pycountry/
Source:		https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
pycountry provides the ISO databases for the standards 639 (Languages),
3166 (Countries), 3166-2 (Subdivisions of countries), 4217 (Currencies),
15924 (Scripts). The databases are imported from Debian's pkg-isocodes,
packaged into pycountry and made accessible through a Python API.
Translation files for the various strings are included as well.

%files
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
