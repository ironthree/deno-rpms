# Generated by rust2rpm 18
%bcond_without check
%global debug_package %{nil}

%global crate deno_core

Name:           rust-%{crate}
Version:        0.98.0
Release:        1%{?dist}
Summary:        Secure JavaScript/TypeScript runtime built with V8, Rust, and Tokio

# Upstream license specification: MIT
# FIXME: missing LICENSE file
# FIXME: bundled ICU data?
License:        MIT
URL:            https://crates.io/crates/deno_core
Source:         %{crates_source}
# Initial patched metadata
# * relax indexmap dependency
# * bump rusty_v8 from 0.26.0 to 0.27.0
# * bump serde_v8 from 0.9.3 to 0.10
#   https://github.com/denoland/deno/commit/0aa6b1e
Patch0:         deno_core-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Secure JavaScript/TypeScript runtime built with V8, Rust, and Tokio.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc examples README.md
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
* Mon Sep 06 2021 Fabio Valentini <decathorpe@gmail.com> - 0.98.0-1
- Update to version 0.98.0.

* Wed Jul 14 2021 Fabio Valentini <decathorpe@gmail.com> - 0.93.0-1
- Update to version 0.93.0.

* Sat Jun 05 2021 Fabio Valentini <decathorpe@gmail.com> - 0.88.1-1
- Update to version 0.88.1.

* Thu Apr 29 2021 Fabio Valentini <decathorpe@gmail.com> - 0.86.0-1
- Update to version 0.86.0.

* Wed Apr 21 2021 Fabio Valentini <decathorpe@gmail.com> - 0.85.0-1
- Initial package
