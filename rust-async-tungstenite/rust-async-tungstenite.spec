# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate async-tungstenite

Name:           rust-%{crate}
Version:        0.13.1
Release:        1%{?dist}
Summary:        Async binding for Tungstenite, the Lightweight stream-based WebSocket implementation

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/async-tungstenite
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Async binding for Tungstenite, the Lightweight stream-based WebSocket
implementation.}

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

%package     -n %{name}+async-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-native-tls-devel %{_description}

This package contains library source intended for building other packages
which use "async-native-tls" feature of "%{crate}" crate.

%files       -n %{name}+async-native-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-std-devel %{_description}

This package contains library source intended for building other packages
which use "async-std" feature of "%{crate}" crate.

%files       -n %{name}+async-std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-std-runtime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-std-runtime-devel %{_description}

This package contains library source intended for building other packages
which use "async-std-runtime" feature of "%{crate}" crate.

%files       -n %{name}+async-std-runtime-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-tls-devel %{_description}

This package contains library source intended for building other packages
which use "async-tls" feature of "%{crate}" crate.

%files       -n %{name}+async-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gio-devel %{_description}

This package contains library source intended for building other packages
which use "gio" feature of "%{crate}" crate.

%files       -n %{name}+gio-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gio-runtime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gio-runtime-devel %{_description}

This package contains library source intended for building other packages
which use "gio-runtime" feature of "%{crate}" crate.

%files       -n %{name}+gio-runtime-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+glib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glib-devel %{_description}

This package contains library source intended for building other packages
which use "glib" feature of "%{crate}" crate.

%files       -n %{name}+glib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-devel %{_description}

This package contains library source intended for building other packages
which use "openssl" feature of "%{crate}" crate.

%files       -n %{name}+openssl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+real-async-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+real-async-native-tls-devel %{_description}

This package contains library source intended for building other packages
which use "real-async-native-tls" feature of "%{crate}" crate.

%files       -n %{name}+real-async-native-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+real-async-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+real-async-tls-devel %{_description}

This package contains library source intended for building other packages
which use "real-async-tls" feature of "%{crate}" crate.

%files       -n %{name}+real-async-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+real-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+real-native-tls-devel %{_description}

This package contains library source intended for building other packages
which use "real-native-tls" feature of "%{crate}" crate.

%files       -n %{name}+real-native-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+real-tokio-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+real-tokio-native-tls-devel %{_description}

This package contains library source intended for building other packages
which use "real-tokio-native-tls" feature of "%{crate}" crate.

%files       -n %{name}+real-tokio-native-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+real-tokio-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+real-tokio-openssl-devel %{_description}

This package contains library source intended for building other packages
which use "real-tokio-openssl" feature of "%{crate}" crate.

%files       -n %{name}+real-tokio-openssl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+real-tokio-rustls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+real-tokio-rustls-devel %{_description}

This package contains library source intended for building other packages
which use "real-tokio-rustls" feature of "%{crate}" crate.

%files       -n %{name}+real-tokio-rustls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages
which use "tokio" feature of "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-native-tls-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-native-tls" feature of "%{crate}" crate.

%files       -n %{name}+tokio-native-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-openssl-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-openssl" feature of "%{crate}" crate.

%files       -n %{name}+tokio-openssl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-runtime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-runtime-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-runtime" feature of "%{crate}" crate.

%files       -n %{name}+tokio-runtime-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-rustls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-rustls-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-rustls" feature of "%{crate}" crate.

%files       -n %{name}+tokio-rustls-devel
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
* Thu Apr 29 2021 Fabio Valentini <decathorpe@gmail.com> - 0.13.1-1
- Initial package