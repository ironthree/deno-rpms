# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate dprint-plugin-typescript

Name:           rust-%{crate}
Version:        0.45.0
Release:        1%{?dist}
Summary:        TypeScript and JavaScript code formatter

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/dprint-plugin-typescript
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
TypeScript and JavaScript code formatter.}

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

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages
which use "serde_json" feature of "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tracing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tracing-devel %{_description}

This package contains library source intended for building other packages
which use "tracing" feature of "%{crate}" crate.

%files       -n %{name}+tracing-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wasm-devel %{_description}

This package contains library source intended for building other packages
which use "wasm" feature of "%{crate}" crate.

%files       -n %{name}+wasm-devel
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
* Mon Jun 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.45.0-1
- Update to version 0.45.0.

* Fri Apr 23 2021 Fabio Valentini <decathorpe@gmail.com> - 0.44.0-1
- Initial package
