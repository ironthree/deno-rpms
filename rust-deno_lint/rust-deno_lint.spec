# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

# mangling executable typescript files seems to be broken (FIXME)
%global __brp_mangle_shebangs_exclude_from %{cargo_registry}/%{crate}-%{version_no_tilde}/tools/

%global crate deno_lint

Name:           rust-%{crate}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Lint for deno

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/deno_lint
Source:         %{crates_source}
# Initial patched metadata
# * bump deno_core from 0.84 to 0.85 (FIXME)
Patch0:         deno_lint-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Lint for deno.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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
* Tue Apr 20 2021 Fabio Valentini <decathorpe@gmail.com> - 0.4.0-1
- Initial package