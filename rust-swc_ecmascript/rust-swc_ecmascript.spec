# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate swc_ecmascript

Name:           rust-%{crate}
Version:        0.31.3
Release:        1%{?dist}
Summary:        Ecmascript

# Upstream license specification: Apache-2.0/MIT
# FIXME: missing license files
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/swc_ecmascript
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Ecmascript.}

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

%package     -n %{name}+codegen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+codegen-devel %{_description}

This package contains library source intended for building other packages
which use "codegen" feature of "%{crate}" crate.

%files       -n %{name}+codegen-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+compat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compat-devel %{_description}

This package contains library source intended for building other packages
which use "compat" feature of "%{crate}" crate.

%files       -n %{name}+compat-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dep_graph-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dep_graph-devel %{_description}

This package contains library source intended for building other packages
which use "dep_graph" feature of "%{crate}" crate.

%files       -n %{name}+dep_graph-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+module-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+module-devel %{_description}

This package contains library source intended for building other packages
which use "module" feature of "%{crate}" crate.

%files       -n %{name}+module-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+optimization-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+optimization-devel %{_description}

This package contains library source intended for building other packages
which use "optimization" feature of "%{crate}" crate.

%files       -n %{name}+optimization-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+parser-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parser-devel %{_description}

This package contains library source intended for building other packages
which use "parser" feature of "%{crate}" crate.

%files       -n %{name}+parser-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+proposal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proposal-devel %{_description}

This package contains library source intended for building other packages
which use "proposal" feature of "%{crate}" crate.

%files       -n %{name}+proposal-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+react-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+react-devel %{_description}

This package contains library source intended for building other packages
which use "react" feature of "%{crate}" crate.

%files       -n %{name}+react-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_codegen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_codegen-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_codegen" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_codegen-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_dep_graph-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_dep_graph-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_dep_graph" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_dep_graph-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_parser-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_parser-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_parser" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_parser-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_transforms-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_transforms-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_transforms" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_transforms-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_utils-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_utils-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_utils" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_utils-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_visit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_visit-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_visit" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_visit-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+transforms-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+transforms-devel %{_description}

This package contains library source intended for building other packages
which use "transforms" feature of "%{crate}" crate.

%files       -n %{name}+transforms-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+typescript-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+typescript-devel %{_description}

This package contains library source intended for building other packages
which use "typescript" feature of "%{crate}" crate.

%files       -n %{name}+typescript-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+utils-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+utils-devel %{_description}

This package contains library source intended for building other packages
which use "utils" feature of "%{crate}" crate.

%files       -n %{name}+utils-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+visit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+visit-devel %{_description}

This package contains library source intended for building other packages
which use "visit" feature of "%{crate}" crate.

%files       -n %{name}+visit-devel
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
* Tue Apr 20 2021 Fabio Valentini <decathorpe@gmail.com> - 0.31.3-1
- Initial package