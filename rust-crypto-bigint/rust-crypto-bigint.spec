# Generated by rust2rpm 18
%bcond_without check
%global debug_package %{nil}

%global crate crypto-bigint

Name:           rust-%{crate}
Version:        0.2.6
Release:        1%{?dist}
Summary:        Pure Rust bigint implementation for use in cryptographic applications

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/crypto-bigint
Source:         %{crates_source}
# Initial patched metadata
# * drop optional rlp dependency (not packaged yet)
# * relax zeroize dependency
Patch0:         crypto-bigint-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pure Rust implementation of a big integer library which has been designed from
the ground-up for use in cryptographic applications. Provides constant-time,
no_std-friendly implementations of modern formulas using const generics.}

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

%package     -n %{name}+generic-array-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generic-array-devel %{_description}

This package contains library source intended for building other packages
which use "generic-array" feature of "%{crate}" crate.

%files       -n %{name}+generic-array-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages
which use "rand" feature of "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rand_core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand_core-devel %{_description}

This package contains library source intended for building other packages
which use "rand_core" feature of "%{crate}" crate.

%files       -n %{name}+rand_core-devel
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
* Sat Sep 11 2021 Fabio Valentini <decathorpe@gmail.com> - 0.2.6-1
- Update to version 0.2.6.

* Tue Sep 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-1
- Initial package
