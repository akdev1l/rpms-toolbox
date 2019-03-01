Name:          toolbox
Version:       0.0.6
Release:       1%{?dist}
Summary:       Unprivileged development environment

License:       ASL 2.0
URL:           https://github.com/debarshiray/toolbox
Source0:       https://github.com/debarshiray/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildArch:     noarch
# buildah and podman only work on the following architectures:
ExclusiveArch: aarch64 %{arm} ppc64le s390x x86_64

BuildRequires: meson

Requires:      buildah
Requires:      podman

# To be removed in Fedora 33
Provides:      fedora-toolbox = %{version}-%{release}
Obsoletes:     fedora-toolbox < 0.0.5-2


%description
Toolbox is offers a familiar RPM based environment for developing and
debugging software that runs fully unprivileged using Podman.


%prep
%autosetup


%build
%meson --buildtype=plain
%meson_build


%check
# https://github.com/debarshiray/toolbox/issues/68
# %%meson_test


%install
%meson_install


%files
%doc NEWS README.md
%license COPYING
%{_bindir}/%{name}


%changelog
* Fri Feb 22 2019 Debarshi Ray <rishi@fedoraproject.org> - 0.0.6-1
- Initial build after rename from fedora-toolbox
