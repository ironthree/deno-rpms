# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate async-codec-lite

Name:           rust-%{crate}
Version:        0.0.0
Release:        1%{?dist}
Summary:        Adaptors from AsyncRead/AsyncWrite to Stream/Sink using futures

# Upstream license specification: Apache-2.0 WITH LLVM-exception AND MIT
License:        ASL 2.0 with exceptions and MIT
URL:            https://crates.io/crates/async-codec-lite
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Adaptors from AsyncRead/AsyncWrite to Stream/Sink using futures.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-Apache LICENSE-MIT
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

%package     -n %{name}+cbor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cbor-devel %{_description}

This package contains library source intended for building other packages
which use "cbor" feature of "%{crate}" crate.

%files       -n %{name}+cbor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages
which use "json" feature of "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lines-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lines-devel %{_description}

This package contains library source intended for building other packages
which use "lines" feature of "%{crate}" crate.

%files       -n %{name}+lines-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+memchr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memchr-devel %{_description}

This package contains library source intended for building other packages
which use "memchr" feature of "%{crate}" crate.

%files       -n %{name}+memchr-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_cbor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_cbor-devel %{_description}

This package contains library source intended for building other packages
which use "serde_cbor" feature of "%{crate}" crate.

%files       -n %{name}+serde_cbor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages
which use "serde_json" feature of "%{crate}" crate.

%files       -n %{name}+serde_json-devel
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
* Thu Apr 29 2021 Fabio Valentini <decathorpe@gmail.com> - 0.0.0-1
- Initial package