# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate console_error_panic_hook

Name:           rust-%{crate}
Version:        0.1.6
Release:        1%{?dist}
Summary:        Panic hook for WASM that logs panics to console.error

# Upstream license specification: Apache-2.0/MIT
# FIXME: missing license files
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/console_error_panic_hook
Source:         %{crates_source}
# Initial patched metadata
# * exclude screenshots from installed files
Patch0:         console_error_panic_hook-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Panic hook for `wasm32-unknown-unknown` that logs panics to `console.error`.}

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
# skip useless "is README up-to-date" test
%cargo_test -- -- --skip cargo_readme_up_to_date
%endif

%changelog
* Wed Apr 21 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.6-1
- Initial package
