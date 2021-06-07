# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate swc_common

Name:           rust-%{crate}
Version:        0.10.20
Release:        1%{?dist}
Summary:        Common utilities for the swc project

# Upstream license specification: Apache-2.0/MIT
# FIXME: missing LICENSE files
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/swc_common
Source:         %{crates_source}
# Initial patched metadata
# * bump parking_lot from 0.7.1 to 0.11 (FIXME)
Patch0:         swc_common-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Common utilities for the swc project.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+arbitrary-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary-devel %{_description}

This package contains library source intended for building other packages
which use "arbitrary" feature of "%{crate}" crate.

%files       -n %{name}+arbitrary-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+atty-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+atty-devel %{_description}

This package contains library source intended for building other packages
which use "atty" feature of "%{crate}" crate.

%files       -n %{name}+atty-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+concurrent-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+concurrent-devel %{_description}

This package contains library source intended for building other packages
which use "concurrent" feature of "%{crate}" crate.

%files       -n %{name}+concurrent-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+parking_lot-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parking_lot-devel %{_description}

This package contains library source intended for building other packages
which use "parking_lot" feature of "%{crate}" crate.

%files       -n %{name}+parking_lot-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sourcemap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sourcemap-devel %{_description}

This package contains library source intended for building other packages
which use "sourcemap" feature of "%{crate}" crate.

%files       -n %{name}+sourcemap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+termcolor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+termcolor-devel %{_description}

This package contains library source intended for building other packages
which use "termcolor" feature of "%{crate}" crate.

%files       -n %{name}+termcolor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tty-emitter-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tty-emitter-devel %{_description}

This package contains library source intended for building other packages
which use "tty-emitter" feature of "%{crate}" crate.

%files       -n %{name}+tty-emitter-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
* Mon Jun 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.10.20-1
- Update to version 0.10.20.

* Mon Apr 19 2021 Fabio Valentini <decathorpe@gmail.com> - 0.10.17-1
- Initial package
