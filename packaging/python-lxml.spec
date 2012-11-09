Name:           python-lxml
Version:        2.3.4
Release:        0
Summary:        Powerful and Pythonic XML processing library
License:        BSD-3-Clause and GPL-2.0+
Group:          Development/Languages/Python
Url:            http://lxml.de/
Source:         http://pypi.python.org/packages/source/l/lxml/lxml-%{version}.tar.gz
BuildRequires:  libxslt-devel
#BuildRequires:  python-Cython
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libxml-2.0)

%description
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries. It
provides safe and convenient access to these libraries using the ElementTree
API. It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.


%prep
%setup -q -n lxml-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%doc LICENSES.txt 
%{python_sitearch}/lxml/
%{python_sitearch}/lxml-%{version}-py%{py_ver}.egg-info
%exclude %{python_sitearch}/lxml/etree_defs.h


%changelog
