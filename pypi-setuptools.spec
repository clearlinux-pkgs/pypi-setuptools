#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-setuptools
Version  : 67.6.1
Release  : 298
URL      : https://files.pythonhosted.org/packages/cb/46/22ec35f286a77e6b94adf81b4f0d59f402ed981d4251df0ba7b992299146/setuptools-67.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/46/22ec35f286a77e6b94adf81b4f0d59f402ed981d4251df0ba7b992299146/setuptools-67.6.1.tar.gz
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
.. image:: https://img.shields.io/pypi/v/setuptools.svg
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
%setup -q -n setuptools-67.6.1
cd %{_builddir}/setuptools-67.6.1
pushd ..
cp -a setuptools-67.6.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680050081
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-setuptools
cp %{_builddir}/setuptools-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-setuptools/8e6689d37f82d5617b7f7f7232c94024d41066d1 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
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
/usr/share/package-licenses/pypi-setuptools/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
