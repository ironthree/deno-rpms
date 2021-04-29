# Generated by rust2rpm 17
# * tests can only be run in-tree
%bcond_with check
%global __cargo_skip_build 0

%global crate deno

Name:           rust-%{crate}
Version:        1.9.1
Release:        1%{?dist}
Summary:        Provides the deno executable

# Upstream license specification: MIT
# FIXME: missing LICENSE file
License:        MIT
URL:            https://crates.io/crates/deno
Source:         %{crates_source}
# Initial patched metadata
# * drop windows-specific dependencies
Patch0:         deno-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Provides the deno executable.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# FIXME: binary license

%description -n %{crate} %{_description}

%files       -n %{crate}
%doc README.md
%{_bindir}/denort
%{_bindir}/deno

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
* Fri Apr 23 2021 Fabio Valentini <decathorpe@gmail.com> - 1.9.1-1
- Initial package
