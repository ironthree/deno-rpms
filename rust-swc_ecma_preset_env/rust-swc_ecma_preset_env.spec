# Generated by rust2rpm 18
# * testing and testing_macros rely on unstable proc-macro2 features
%bcond_with check
%global debug_package %{nil}

%global crate swc_ecma_preset_env

Name:           rust-%{crate}
Version:        0.33.0
Release:        1%{?dist}
Summary:        Preset-env for the swc

# Upstream license specification: Apache-2.0/MIT
# FIXME: missing LICENSE files
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/swc_ecma_preset_env
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Preset-env for the swc.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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
* Tue Sep 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.33.0-1
- Initial package
