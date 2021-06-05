# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate deno_console

Name:           rust-%{crate}
Version:        0.7.1
Release:        1%{?dist}
Summary:        Implementation of Console API for Deno

# Upstream license specification: MIT
# FIXME: missing LICENSE file
License:        MIT
URL:            https://crates.io/crates/deno_console
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation of Console API for Deno.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Sat Jun 05 2021 Fabio Valentini <decathorpe@gmail.com> - 0.7.1-1
- Update to version 0.7.1.

* Thu Apr 29 2021 Fabio Valentini <decathorpe@gmail.com> - 0.5.0-1
- Update to version 0.5.0.

* Fri Apr 23 2021 Fabio Valentini <decathorpe@gmail.com> - 0.4.0-1
- Initial package
