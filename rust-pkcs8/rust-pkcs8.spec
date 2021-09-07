# Generated by rust2rpm 18
%bcond_without check
%global debug_package %{nil}

%global crate pkcs8

Name:           rust-%{crate}
Version:        0.7.5
Release:        1%{?dist}
Summary:        Pure Rust implementation of PKCS#8 (RFC 5208 and RFC 5958)

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/pkcs8
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #8:
Private-Key Information Syntax Specification (RFC 5208), with additional
support for PKCS#8v2 asymmetric key packages (RFC 5958).}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+encryption-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+encryption-devel %{_description}

This package contains library source intended for building other packages
which use "encryption" feature of "%{crate}" crate.

%files       -n %{name}+encryption-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pem-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pem-devel %{_description}

This package contains library source intended for building other packages
which use "pem" feature of "%{crate}" crate.

%files       -n %{name}+pem-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pem-rfc7468-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pem-rfc7468-devel %{_description}

This package contains library source intended for building other packages
which use "pem-rfc7468" feature of "%{crate}" crate.

%files       -n %{name}+pem-rfc7468-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pkcs1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pkcs1-devel %{_description}

This package contains library source intended for building other packages
which use "pkcs1" feature of "%{crate}" crate.

%files       -n %{name}+pkcs1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pkcs5-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pkcs5-devel %{_description}

This package contains library source intended for building other packages
which use "pkcs5" feature of "%{crate}" crate.

%files       -n %{name}+pkcs5-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rand_core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand_core-devel %{_description}

This package contains library source intended for building other packages
which use "rand_core" feature of "%{crate}" crate.

%files       -n %{name}+rand_core-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+zeroize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zeroize-devel %{_description}

This package contains library source intended for building other packages
which use "zeroize" feature of "%{crate}" crate.

%files       -n %{name}+zeroize-devel
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
* Tue Sep 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.7.5-1
- Initial package
