%define _empty_manifest_terminate_build 0

%define real_name pycountry

Name:           python-pycountry
Group:          Development/Python 
Version:        22.3.5
Release:        2
License:        LGPL v2.1
Summary:        Databases for iso standards 639 3166 3166-2 4217 15924
Source:          https://pypi.python.org/packages/source/p/pycountry/%{real_name}-%{version}.tar.gz
Requires:       python, python-lxml
BuildRequires:  python-setuptools
Url:            http://pypi.python.org/pypi/pycountry/

%description
pycountry provides the ISO databases for the standards 639 (Languages),
3166 (Countries), 3166-2 (Subdivisions of countries), 4217 (Currencies),
15924 (Scripts). The databases are imported from Debian's pkg-isocodes,
packaged into pycountry and made accessible through a Python API.
Translation files for the various strings are included as well.

%prep
%setup -q -n %{real_name}-%{version}

%build
python setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
#% {py_platsitedir}/*
%{python_sitelib}/*


%changelog
* Sun Dec 04 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.14.1-1
+ Revision: 737701
- files section fix hmmm...
- imported package python-pycountry

