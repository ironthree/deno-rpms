# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate async_io_stream

Name:           rust-%{crate}
Version:        0.3.1
Release:        1%{?dist}
Summary:        IntoAsyncRead on steriods

# Upstream license specification: Unlicense
License:        Unlicense
URL:            https://crates.io/crates/async_io_stream
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
IntoAsyncRead on steriods.}

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

%package     -n %{name}+map_pharos-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+map_pharos-devel %{_description}

This package contains library source intended for building other packages
which use "map_pharos" feature of "%{crate}" crate.

%files       -n %{name}+map_pharos-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pharos-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pharos-devel %{_description}

This package contains library source intended for building other packages
which use "pharos" feature of "%{crate}" crate.

%files       -n %{name}+pharos-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages
which use "tokio" feature of "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio_io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio_io-devel %{_description}

This package contains library source intended for building other packages
which use "tokio_io" feature of "%{crate}" crate.

%files       -n %{name}+tokio_io-devel
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
* Thu Apr 29 2021 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Initial package
