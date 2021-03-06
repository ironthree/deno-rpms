# Generated by rust2rpm 18
%bcond_without check
%global debug_package %{nil}

%global crate lsp-types

Name:           rust-%{crate}
Version:        0.89.2
Release:        1%{?dist}
Summary:        Types for interaction with a language server, using VSCode's Language Server Protocol

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/lsp-types
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Types for interaction with a language server, using VSCode's Language Server
Protocol.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+proposed-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proposed-devel %{_description}

This package contains library source intended for building other packages
which use "proposed" feature of "%{crate}" crate.

%files       -n %{name}+proposed-devel
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
* Tue Sep 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.89.2-1
- Update to version 0.89.2.

* Thu Apr 29 2021 Fabio Valentini <decathorpe@gmail.com> - 0.88.0-1
- Initial package
