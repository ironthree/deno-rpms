# Generated by rust2rpm 17
# * resolve dependency loop with insta
%bcond_with check
%global debug_package %{nil}

%global crate similar

Name:           rust-%{crate}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Diff library for Rust

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/similar
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Diff library for Rust.}

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

%package     -n %{name}+inline-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+inline-devel %{_description}

This package contains library source intended for building other packages
which use "inline" feature of "%{crate}" crate.

%files       -n %{name}+inline-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+text-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+text-devel %{_description}

This package contains library source intended for building other packages
which use "text" feature of "%{crate}" crate.

%files       -n %{name}+text-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-devel %{_description}

This package contains library source intended for building other packages
which use "unicode" feature of "%{crate}" crate.

%files       -n %{name}+unicode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-segmentation-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-segmentation-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-segmentation" feature of "%{crate}" crate.

%files       -n %{name}+unicode-segmentation-devel
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
* Tue Apr 20 2021 Fabio Valentini <decathorpe@gmail.com> - 0.5.0-1
- Initial package
