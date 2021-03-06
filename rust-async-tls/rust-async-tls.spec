# Generated by rust2rpm 17
# * tests fail to compile
%bcond_with check
%global debug_package %{nil}

%global crate async-tls

Name:           rust-%{crate}
Version:        0.11.0
Release:        1%{?dist}
Summary:        Asynchronous TLS/SSL streams using Rustls

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/async-tls
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Asynchronous TLS/SSL streams using Rustls.}

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

%package     -n %{name}+client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+client-devel %{_description}

This package contains library source intended for building other packages
which use "client" feature of "%{crate}" crate.

%files       -n %{name}+client-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+early-data-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+early-data-devel %{_description}

This package contains library source intended for building other packages
which use "early-data" feature of "%{crate}" crate.

%files       -n %{name}+early-data-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+server-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+server-devel %{_description}

This package contains library source intended for building other packages
which use "server" feature of "%{crate}" crate.

%files       -n %{name}+server-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+webpki-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+webpki-devel %{_description}

This package contains library source intended for building other packages
which use "webpki" feature of "%{crate}" crate.

%files       -n %{name}+webpki-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+webpki-roots-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+webpki-roots-devel %{_description}

This package contains library source intended for building other packages
which use "webpki-roots" feature of "%{crate}" crate.

%files       -n %{name}+webpki-roots-devel
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
* Thu Apr 29 2021 Fabio Valentini <decathorpe@gmail.com> - 0.11.0-1
- Initial package
