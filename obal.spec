%global pypi_name obal

Name:           %{pypi_name}
Version:        0.8.0
Release:        1%{?dist}
Summary:        packaging wrapper using ansible

License:        GPLv2
URL:            https://github.com/theforeman/obal
Source0:        %{pypi_source}
BuildArch:      noarch

%if 0%{?fedora}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?python_enable_dependency_generator}
Requires:       %{py3_dist argcomplete}
%else
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       ansible >= 2.5

%{?python_provide:%python_provide python-%{pypi_name}}
%endif

Requires: git-annex
Requires: koji
Requires: rpm-build
Requires: rpmlint
Requires: scl-utils
Requires: scl-utils-build
Requires: tito
Requires: yum-utils

Obsoletes:      python2-obal
Conflicts:      python2-obal
%if 0%{?fedora}
Obsoletes:      python3-obal
Conflicts:      python3-obal
%endif

%description
Obal is an Ansible wrapper with a set of Ansible playbooks to ease maintanance
of packaging repositories like foreman-packaging and pulp-packaging.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?fedora}
%py3_build
%else
%py2_build
%endif

%install
%if 0%{?fedora}
%py3_install
%else
%py2_install
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/obal
%if 0%{?fedora}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%else
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Wed Feb 24 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.8.0-1
- Update to 0.8.0

* Thu Feb 28 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.3.0-1
- Update to 0.3.0
- Use current Fedora Python RPM packaging macros

* Tue Dec 18 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.2.0-1
- Update to 0.2.0

* Wed Oct 24 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.1.0-1
- Update to 0.1.0

* Fri Sep 14 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.6-2
- Add runtime dependencies

