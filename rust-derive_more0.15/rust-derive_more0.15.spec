# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate derive_more

Name:           rust-%{crate}0.15
Version:        0.15.0
Release:        1%{?dist}
Summary:        Adds #[derive(x)] macros for more traits

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/derive_more
Source:         %{crates_source}
# Initial patched metadata
# * bump rustc_version from 0.2 to 0.3 (WONTFIX for compat package)
Patch0:         derive_more-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Adds #[derive(x)] macros for more traits.}

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

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+no_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_std-devel %{_description}

This package contains library source intended for building other packages
which use "no_std" feature of "%{crate}" crate.

%files       -n %{name}+no_std-devel
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
* Fri Apr 23 2021 Fabio Valentini <decathorpe@gmail.com> - 0.15.0-1
- Initial package
