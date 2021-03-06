# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate insta

Name:           rust-%{crate}0.16
Version:        0.16.1
Release:        1%{?dist}
Summary:        Snapshot testing library for Rust

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/insta
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

# https://github.com/mitsuhiko/insta/issues/126
%if %{with check}
BuildRequires:  rustfmt
%endif

%global _description %{expand:
Snapshot testing library for Rust.}

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

%package     -n %{name}+backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-devel %{_description}

This package contains library source intended for building other packages
which use "backtrace" feature of "%{crate}" crate.

%files       -n %{name}+backtrace-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+glob-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glob-devel %{_description}

This package contains library source intended for building other packages
which use "glob" feature of "%{crate}" crate.

%files       -n %{name}+glob-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+globwalk-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+globwalk-devel %{_description}

This package contains library source intended for building other packages
which use "globwalk" feature of "%{crate}" crate.

%files       -n %{name}+globwalk-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pest-devel %{_description}

This package contains library source intended for building other packages
which use "pest" feature of "%{crate}" crate.

%files       -n %{name}+pest-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pest_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pest_derive-devel %{_description}

This package contains library source intended for building other packages
which use "pest_derive" feature of "%{crate}" crate.

%files       -n %{name}+pest_derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+redactions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+redactions-devel %{_description}

This package contains library source intended for building other packages
which use "redactions" feature of "%{crate}" crate.

%files       -n %{name}+redactions-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ron-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ron-devel %{_description}

This package contains library source intended for building other packages
which use "ron" feature of "%{crate}" crate.

%files       -n %{name}+ron-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serialization-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialization-devel %{_description}

This package contains library source intended for building other packages
which use "serialization" feature of "%{crate}" crate.

%files       -n %{name}+serialization-devel
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
* Fri Apr 23 2021 Fabio Valentini <decathorpe@gmail.com> - 0.16.1-1
- Initial compat package for insta 0.16
