# Generated by rust2rpm 18
%bcond_without check
%global debug_package %{nil}

%global crate lspower

Name:           rust-%{crate}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Lightweight framework for implementing LSP servers

# Upstream license specification: FIXME
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/lspower
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Lightweight framework for implementing LSP servers.}

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

%package     -n %{name}+async-codec-lite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-codec-lite-devel %{_description}

This package contains library source intended for building other packages
which use "async-codec-lite" feature of "%{crate}" crate.

%files       -n %{name}+async-codec-lite-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+runtime-agnostic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-agnostic-devel %{_description}

This package contains library source intended for building other packages
which use "runtime-agnostic" feature of "%{crate}" crate.

%files       -n %{name}+runtime-agnostic-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+runtime-tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-tokio-devel %{_description}

This package contains library source intended for building other packages
which use "runtime-tokio" feature of "%{crate}" crate.

%files       -n %{name}+runtime-tokio-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages
which use "tokio" feature of "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-util-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-util" feature of "%{crate}" crate.

%files       -n %{name}+tokio-util-devel
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
* Tue Sep 07 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Fri Apr 23 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- Initial package
