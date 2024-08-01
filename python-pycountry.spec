%define real_name pycountry

Name:           python-pycountry
Group:          Development/Python 
Version:        24.6.1
Release:        1
License:        LGPL v2.1
Summary:        Databases for iso standards 639 3166 3166-2 4217 15924
Source:         https://pypi.python.org/packages/source/p/pycountry/%{real_name}-%{version}.tar.gz
Requires:       python, python-lxml
BuildRequires:	python
BuildRequires:	python%{pyver}dist(poetry)
Url:            http://pypi.python.org/pypi/pycountry/
BuildArch:	noarch

%description
pycountry provides the ISO databases for the standards 639 (Languages),
3166 (Countries), 3166-2 (Subdivisions of countries), 4217 (Currencies),
15924 (Scripts). The databases are imported from Debian's pkg-isocodes,
packaged into pycountry and made accessible through a Python API.
Translation files for the various strings are included as well.

%prep
%autosetup -p1 -n pycountry-%{version}

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/*
