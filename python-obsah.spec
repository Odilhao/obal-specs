%global pypi_name obsah

%if 0%{?rhel} == 7
%bcond_without python2
%bcond_with python3
%else
%bcond_with python2
%bcond_without python3
%endif

Name:           python-%{pypi_name}
Version:        0.0.2
Release:        1%{?dist}
Summary:        packaging wrapper using ansible

License:        None
URL:            https://github.com/theforeman/obsah
Source0:        %{pypi_source}
BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%endif

%description
Easily build CLI applications using ansible playbooks.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-ansible >= 2.5
Requires:       python2-argcomplete
Requires:       python2-setuptools
%description -n python2-%{pypi_name}
Easily build CLI applications using ansible playbooks.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(ansible) >= 2.5
Requires:       python3dist(argcomplete)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
Easily build CLI applications using ansible playbooks.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/obsah
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/obsah
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%endif

%changelog
* Sun Oct 25 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.2-1
- Update to 0.0.2

* Wed May 13 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.1-2
- Allow building with Python 2 on EPEL7

* Thu Nov 28 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.1-1
- Initial package.
