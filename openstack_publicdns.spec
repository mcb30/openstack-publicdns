%global srcname openstack_publicdns

%define with_py2 1
%define with_py3 1

%if 0%{?rhel}
%define with_py3 0
%endif

Name:		python-%{srcname}
Version:	0.0.2
Release:	1%{?dist}
Summary:	OpenStack public DNS plugins
License:	GPLv2+
URL:		https://github.com/unipartdigital/openstack_publicdns
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
%if 0%{?with_py2}
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
%endif
%if 0%{?with_py3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif

%description
OpenStack plugins to simplify the use of public DNS names for virtual
machine instances.

%if 0%{?with_py2}
%package -n	python2-%{srcname}
Summary:	%{summary}
%if 0%{?rhel}
Requires:	python-neutron
%else
Requires:	python2-neutron
%endif
Requires:	python2-setuptools
%if ! 0%{?with_py3}
Provides:	%{srcname} = %{version}-%{release}
%endif

%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
OpenStack plugins to simplify the use of public DNS names for virtual
machine instances.
%endif

%if 0%{?with_py3}
%package -n	python3-%{srcname}
Summary:	%{summary}
Requires:	python3-neutron
Provides:	%{srcname} = %{version}-%{release}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
OpenStack plugins to simplify the use of public DNS names for virtual
machine instances.
%endif

%prep
%autosetup

%build
%if 0%{?with_py2}
%py2_build
%endif
%if 0%{?with_py3}
%py3_build
%endif

%install
%if 0%{?with_py2}
%py2_install
%endif
%if 0%{?with_py3}
%py3_install
%endif

%if 0%{?with_py2}
%files -n python2-%{srcname}
%doc README.md
%license COPYING
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}-%{version}-*.egg-info/
%endif

%if 0%{?with_py3}
%files -n python3-%{srcname}
%doc README.md
%license COPYING
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info/
%endif

%changelog
* Mon Jul 29 2019 Michael Brown <mbrown@fensystems.co.uk> 0.0.2-1
- Switched to setuptools and added RPM spec file

* Mon Jul 29 2019 Michael Brown <mbrown@fensystems.co.uk> - 0.0.1-1
- Initial package
