# Generated by rust2rpm 18
# * testing and testing_macros rely on unstable proc-macro2 features
%bcond_with check
%global debug_package %{nil}

%global crate swc_ecma_transforms

Name:           rust-%{crate}
Version:        0.63.0
Release:        1%{?dist}
Summary:        Rust port of babel and closure compiler

# Upstream license specification: Apache-2.0/MIT
# FIXME: missing LICENSE files
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/swc_ecma_transforms
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust port of babel and closure compiler.}

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

%package     -n %{name}+compat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compat-devel %{_description}

This package contains library source intended for building other packages
which use "compat" feature of "%{crate}" crate.

%files       -n %{name}+compat-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+module-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+module-devel %{_description}

This package contains library source intended for building other packages
which use "module" feature of "%{crate}" crate.

%files       -n %{name}+module-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+multi-module-decorator-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+multi-module-decorator-devel %{_description}

This package contains library source intended for building other packages
which use "multi-module-decorator" feature of "%{crate}" crate.

%files       -n %{name}+multi-module-decorator-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+optimization-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+optimization-devel %{_description}

This package contains library source intended for building other packages
which use "optimization" feature of "%{crate}" crate.

%files       -n %{name}+optimization-devel
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

%package     -n %{name}+swc_ecma_transforms_compat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_transforms_compat-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_transforms_compat" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_transforms_compat-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_transforms_module-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_transforms_module-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_transforms_module" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_transforms_module-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_transforms_optimization-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_transforms_optimization-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_transforms_optimization" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_transforms_optimization-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_transforms_proposal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_transforms_proposal-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_transforms_proposal" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_transforms_proposal-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_transforms_react-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_transforms_react-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_transforms_react" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_transforms_react-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+swc_ecma_transforms_typescript-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+swc_ecma_transforms_typescript-devel %{_description}

This package contains library source intended for building other packages
which use "swc_ecma_transforms_typescript" feature of "%{crate}" crate.

%files       -n %{name}+swc_ecma_transforms_typescript-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+typescript-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+typescript-devel %{_description}

This package contains library source intended for building other packages
which use "typescript" feature of "%{crate}" crate.

%files       -n %{name}+typescript-devel
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
* Tue Sep 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.63.0-1
- Update to version 0.63.0.

* Mon Jun 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.47.0-1
- Update to version 0.47.0.

* Tue Apr 20 2021 Fabio Valentini <decathorpe@gmail.com> - 0.45.3-1
- Initial package
