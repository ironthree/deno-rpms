# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate async-std

Name:           rust-%{crate}
Version:        1.9.0
Release:        1%{?dist}
Summary:        Async version of the Rust standard library

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/async-std
Source:         %{crates_source}
# Initial patched metadata
# * drop windows-specific dependencies and features
# * drop WASM-specific dependencies and features
# * drop tokio 0.3 features
Patch0:         async-std-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Async version of the Rust standard library.}

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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-attributes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-attributes-devel %{_description}

This package contains library source intended for building other packages
which use "async-attributes" feature of "%{crate}" crate.

%files       -n %{name}+async-attributes-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-channel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-channel-devel %{_description}

This package contains library source intended for building other packages
which use "async-channel" feature of "%{crate}" crate.

%files       -n %{name}+async-channel-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-global-executor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-global-executor-devel %{_description}

This package contains library source intended for building other packages
which use "async-global-executor" feature of "%{crate}" crate.

%files       -n %{name}+async-global-executor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-io-devel %{_description}

This package contains library source intended for building other packages
which use "async-io" feature of "%{crate}" crate.

%files       -n %{name}+async-io-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-lock-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-lock-devel %{_description}

This package contains library source intended for building other packages
which use "async-lock" feature of "%{crate}" crate.

%files       -n %{name}+async-lock-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-process-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-process-devel %{_description}

This package contains library source intended for building other packages
which use "async-process" feature of "%{crate}" crate.

%files       -n %{name}+async-process-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+attributes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+attributes-devel %{_description}

This package contains library source intended for building other packages
which use "attributes" feature of "%{crate}" crate.

%files       -n %{name}+attributes-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+crossbeam-utils-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crossbeam-utils-devel %{_description}

This package contains library source intended for building other packages
which use "crossbeam-utils" feature of "%{crate}" crate.

%files       -n %{name}+crossbeam-utils-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+docs-devel %{_description}

This package contains library source intended for building other packages
which use "docs" feature of "%{crate}" crate.

%files       -n %{name}+docs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-core-devel %{_description}

This package contains library source intended for building other packages
which use "futures-core" feature of "%{crate}" crate.

%files       -n %{name}+futures-core-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-io-devel %{_description}

This package contains library source intended for building other packages
which use "futures-io" feature of "%{crate}" crate.

%files       -n %{name}+futures-io-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-lite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-lite-devel %{_description}

This package contains library source intended for building other packages
which use "futures-lite" feature of "%{crate}" crate.

%files       -n %{name}+futures-lite-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+kv-log-macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kv-log-macro-devel %{_description}

This package contains library source intended for building other packages
which use "kv-log-macro" feature of "%{crate}" crate.

%files       -n %{name}+kv-log-macro-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages
which use "log" feature of "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+memchr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memchr-devel %{_description}

This package contains library source intended for building other packages
which use "memchr" feature of "%{crate}" crate.

%files       -n %{name}+memchr-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+num_cpus-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+num_cpus-devel %{_description}

This package contains library source intended for building other packages
which use "num_cpus" feature of "%{crate}" crate.

%files       -n %{name}+num_cpus-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+once_cell-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+once_cell-devel %{_description}

This package contains library source intended for building other packages
which use "once_cell" feature of "%{crate}" crate.

%files       -n %{name}+once_cell-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pin-project-lite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pin-project-lite-devel %{_description}

This package contains library source intended for building other packages
which use "pin-project-lite" feature of "%{crate}" crate.

%files       -n %{name}+pin-project-lite-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pin-utils-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pin-utils-devel %{_description}

This package contains library source intended for building other packages
which use "pin-utils" feature of "%{crate}" crate.

%files       -n %{name}+pin-utils-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+slab-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+slab-devel %{_description}

This package contains library source intended for building other packages
which use "slab" feature of "%{crate}" crate.

%files       -n %{name}+slab-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+surf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+surf-devel %{_description}

This package contains library source intended for building other packages
which use "surf" feature of "%{crate}" crate.

%files       -n %{name}+surf-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio02-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio02-devel %{_description}

This package contains library source intended for building other packages
which use "tokio02" feature of "%{crate}" crate.

%files       -n %{name}+tokio02-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio1-devel %{_description}

This package contains library source intended for building other packages
which use "tokio1" feature of "%{crate}" crate.

%files       -n %{name}+tokio1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
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
# skip one failing test (probably related to mock environment)
%cargo_test -- -- --skip io_timeout_timedout
%endif

%changelog
* Thu Apr 29 2021 Fabio Valentini <decathorpe@gmail.com> - 1.9.0-1
- Initial package