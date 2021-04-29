# Generated by rust2rpm 17
# * missing dev-dependencies
%bcond_with check
%global debug_package %{nil}

%global crate dlopen

Name:           rust-%{crate}
Version:        0.1.8
Release:        1%{?dist}
Summary:        Library for opening and operating on dynamic link libraries

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/dlopen
Source:         %{crates_source}
# Initial patched metadata
# * drop windows-specific dependencies
Patch0:         dlopen-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library for opening and operating on dynamic link libraries (also known as
shared objects or shared libraries). This is a modern and more flexible
alternative to the already existing libraries like libloading or sharedlib.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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
* Thu Apr 29 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.8-1
- Initial package
