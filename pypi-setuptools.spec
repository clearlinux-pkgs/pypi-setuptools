#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v12
# autospec commit: f9eab48
#
Name     : pypi-setuptools
Version  : 70.1.0
Release  : 324
URL      : https://files.pythonhosted.org/packages/1c/1c/8a56622f2fc9ebb0df743373ef1a96c8e20410350d12f44ef03c588318c3/setuptools-70.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1c/1c/8a56622f2fc9ebb0df743373ef1a96c8e20410350d12f44ef03c588318c3/setuptools-70.1.0.tar.gz
Summary  : Easily download, build, install, upgrade, and uninstall Python packages
Group    : Development/Tools
License  : MIT Python-2.0 ZPL-2.0
Requires: pypi-setuptools-bin = %{version}-%{release}
Requires: pypi-setuptools-license = %{version}-%{release}
Requires: pypi-setuptools-python = %{version}-%{release}
Requires: pypi-setuptools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. |pypi-version| image:: https://img.shields.io/pypi/v/setuptools.svg
:target: https://pypi.org/project/setuptools

%package bin
Summary: bin components for the pypi-setuptools package.
Group: Binaries
Requires: pypi-setuptools-license = %{version}-%{release}

%description bin
bin components for the pypi-setuptools package.


%package license
Summary: license components for the pypi-setuptools package.
Group: Default

%description license
license components for the pypi-setuptools package.


%package python
Summary: python components for the pypi-setuptools package.
Group: Default
Requires: pypi-setuptools-python3 = %{version}-%{release}

%description python
python components for the pypi-setuptools package.


%package python3
Summary: python3 components for the pypi-setuptools package.
Group: Default
Requires: python3-core
Provides: pypi(setuptools)

%description python3
python3 components for the pypi-setuptools package.


%prep
%setup -q -n setuptools-70.1.0
cd %{_builddir}/setuptools-70.1.0
pushd ..
cp -a setuptools-70.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718824219
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-setuptools
cp %{_builddir}/setuptools-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-setuptools/0445ed0f69910eeaee036f09a39a13c6e1f37e12 || :
cp %{_builddir}/setuptools-%{version}/setuptools/_vendor/wheel-0.43.0.dist-info/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-setuptools/5b39c45a91a556e5f1599604f1799e4027fa0e60 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/setuptools/cli-32.exe
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/setuptools/cli-64.exe
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/setuptools/cli-arm64.exe
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/setuptools/cli.exe
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/setuptools/gui-32.exe
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/setuptools/gui-64.exe
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/setuptools/gui-arm64.exe
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/setuptools/gui.exe
## install_append content
mkdir -p %{buildroot}/usr/bin
echo "#!/bin/sh" > %{buildroot}/usr/bin/easy_install_is_deprecated
chmod 755 %{buildroot}/usr/bin/easy_install_is_deprecated
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/easy_install_is_deprecated

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-setuptools/0445ed0f69910eeaee036f09a39a13c6e1f37e12
/usr/share/package-licenses/pypi-setuptools/5b39c45a91a556e5f1599604f1799e4027fa0e60

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
