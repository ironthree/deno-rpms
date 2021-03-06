# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate fancy-regex

Name:           rust-%{crate}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Implementation of regexes supporting a rich set of features

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/fancy-regex
Source:         %{crates_source}
# Initial patched metadata
# * relax quickcheck dependency
Patch0:         fancy-regex-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation of regexes, supporting a relatively rich set of features,
including backreferences and look-around.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOG.md PERFORMANCE.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+track_caller-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+track_caller-devel %{_description}

This package contains library source intended for building other packages
which use "track_caller" feature of "%{crate}" crate.

%files       -n %{name}+track_caller-devel
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
* Wed Apr 21 2021 Fabio Valentini <decathorpe@gmail.com> - 0.5.0-1
- Initial package
