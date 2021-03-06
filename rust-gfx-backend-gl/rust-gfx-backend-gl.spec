# Generated by rust2rpm 18
%bcond_without check
%global debug_package %{nil}

%global crate gfx-backend-gl

Name:           rust-%{crate}
Version:        0.9.0
Release:        1%{?dist}
Summary:        OpenGL backend for gfx-rs

# Upstream license specification: MIT OR Apache-2.0
# FIXME: missing LICENSE files
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/gfx-backend-gl
Source:         %{crates_source}
# Initial patched metadata
# * drop WASM-specific dependencies
Patch0:         gfx-backend-gl-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
OpenGL backend for gfx-rs.}

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

%package     -n %{name}+auxil-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+auxil-devel %{_description}

This package contains library source intended for building other packages
which use "auxil" feature of "%{crate}" crate.

%files       -n %{name}+auxil-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cross-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cross-devel %{_description}

This package contains library source intended for building other packages
which use "cross" feature of "%{crate}" crate.

%files       -n %{name}+cross-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+spirv_cross-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+spirv_cross-devel %{_description}

This package contains library source intended for building other packages
which use "spirv_cross" feature of "%{crate}" crate.

%files       -n %{name}+spirv_cross-devel
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
* Mon Sep 06 2021 Fabio Valentini <decathorpe@gmail.com> - 0.9.0-1
- Update to version 0.9.0.

* Mon Jun 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.8.1-1
- Update to version 0.8.1.

* Fri Apr 23 2021 Fabio Valentini <decathorpe@gmail.com> - 0.7.1-1
- Initial package
