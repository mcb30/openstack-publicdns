%global pkgname neutron_dnscurrent
%global eggname neutron_dnscurrent_plugin

%define with_py2 1
%define with_py3 1

%if 0%{?rhel}
%define with_py3 0
%endif

Name:		python-%{pkgname}
Version:	0.0.2
Release:	1%{?dist}
Summary:	Use dns_current_name as machine hostname
License:	GPLv2+
URL:		https://github.com/unipartdigital/neutron-dnscurrent-plugin
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
OpenStack Neutron plugin to allow machine's external DNS name to be
used as the DHCP hostname.

%if 0%{?with_py2}
%package -n	python2-%{pkgname}
Summary:	%{summary}
%if 0%{?rhel}
Requires:	python-neutron
%else
Requires:	python2-neutron
%endif
Requires:	python2-setuptools
%if ! 0%{?with_py3}
Provides:	%{pkgname} = %{version}-%{release}
%endif

%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname}
OpenStack Neutron plugin to allow machine's external DNS name to be
used as the DHCP hostname.
%endif

%if 0%{?with_py3}
%package -n	python3-%{pkgname}
Summary:	%{summary}
Requires:	python3-neutron
Provides:	%{pkgname} = %{version}-%{release}

%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
OpenStack Neutron plugin to allow machine's external DNS name to be
used as the DHCP hostname.
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
%files -n python2-%{pkgname}
%doc README.md
%license COPYING
%{python2_sitelib}/%{pkgname}/
%{python2_sitelib}/%{eggname}-%{version}-*.egg-info/
%endif

%if 0%{?with_py3}
%files -n python3-%{pkgname}
%doc README.md
%license COPYING
%{python3_sitelib}/%{pkgname}/
%{python3_sitelib}/%{eggname}-%{version}-*.egg-info/
%endif

%changelog
* Mon Jul 29 2019 Michael Brown <mbrown@fensystems.co.uk> 0.0.2-1
- Switched to setuptools and added RPM spec file

* Mon Jul 29 2019 Michael Brown <mbrown@fensystems.co.uk> - 0.0.1-1
- Initial package
