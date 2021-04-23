# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate spirv_cross

Name:           rust-%{crate}
Version:        0.23.1
Release:        1%{?dist}
Summary:        Safe wrapper around SPIRV-Cross

# Upstream license specification: MIT/Apache-2.0
# FIXME: missing license files
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/spirv_cross
Source:         %{crates_source}
# Initial patched metadata
# * drop WASM-specific dependencies
Patch0:         spirv_cross-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Safe wrapper around SPIRV-Cross.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license src/vendor/SPIRV-Cross/LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

License:        (MIT or ASL 2.0) and ASL 2.0
Provides:       bundled(SPIRV-Cross) = afcf45e

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+glsl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glsl-devel %{_description}

This package contains library source intended for building other packages
which use "glsl" feature of "%{crate}" crate.

%files       -n %{name}+glsl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+hlsl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hlsl-devel %{_description}

This package contains library source intended for building other packages
which use "hlsl" feature of "%{crate}" crate.

%files       -n %{name}+hlsl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+msl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+msl-devel %{_description}

This package contains library source intended for building other packages
which use "msl" feature of "%{crate}" crate.

%files       -n %{name}+msl-devel
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
# integration tests can only be run in-tree
%cargo_test -- --lib
%endif

%changelog
* Fri Apr 23 2021 Fabio Valentini <decathorpe@gmail.com> - 0.23.1-1
- Initial package