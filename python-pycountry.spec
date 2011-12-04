#norootforbuild
#
%define real_name pycountry
#
#
Name:           python-pycountry
Group:          Development/Python 
Version:        0.14.1
Release:        1
License:        LGPL v2.1
Summary:        Databases for iso standards 639 3166 3166-2 4217 15924
Source:         %{real_name}-%{version}.tar.gz
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
%{py_platsitedir}/*

