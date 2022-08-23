#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pandocfilters
Version  : 1.5.0
Release  : 48
URL      : https://files.pythonhosted.org/packages/62/42/c32476b110a2d25277be875b82b5669f2cdda7897c165bd22b78f366b3cb/pandocfilters-1.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/42/c32476b110a2d25277be875b82b5669f2cdda7897c165bd22b78f366b3cb/pandocfilters-1.5.0.tar.gz
Summary  : Utilities for writing pandoc filters in python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pandocfilters-license = %{version}-%{release}
Requires: pypi-pandocfilters-python = %{version}-%{release}
Requires: pypi-pandocfilters-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
pandocfilters
=============
A python module for writing `pandoc <http://pandoc.org/>`_ filters

%package license
Summary: license components for the pypi-pandocfilters package.
Group: Default

%description license
license components for the pypi-pandocfilters package.


%package python
Summary: python components for the pypi-pandocfilters package.
Group: Default
Requires: pypi-pandocfilters-python3 = %{version}-%{release}

%description python
python components for the pypi-pandocfilters package.


%package python3
Summary: python3 components for the pypi-pandocfilters package.
Group: Default
Requires: python3-core
Provides: pypi(pandocfilters)

%description python3
python3 components for the pypi-pandocfilters package.


%prep
%setup -q -n pandocfilters-1.5.0
cd %{_builddir}/pandocfilters-1.5.0
pushd ..
cp -a pandocfilters-1.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656392647
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pandocfilters
cp %{_builddir}/pandocfilters-1.5.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pandocfilters/9990e0fc59b210f7995dbe22caeb082cae511080
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pandocfilters/9990e0fc59b210f7995dbe22caeb082cae511080

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
