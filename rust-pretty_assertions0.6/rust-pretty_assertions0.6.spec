# Generated by rust2rpm 17
# * tests fail with cosmetic string differences
%bcond_with check
%global debug_package %{nil}

%global crate pretty_assertions

Name:           rust-%{crate}0.6
Version:        0.6.1
Release:        1%{?dist}
Summary:        Overwrite assert_eq! and assert_ne! with colorful replacements

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/pretty_assertions
Source:         %{crates_source}
# Initial patched metadata
# * drop windows-specific dependencies
Patch0:         pretty_assertions-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Overwrite `assert_eq!` and `assert_ne!` with drop-in replacements, adding
colorful diffs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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
* Tue Apr 20 2021 Fabio Valentini <decathorpe@gmail.com> - 0.6.1-1
- Initial compat package for pretty_assertions 0.6
