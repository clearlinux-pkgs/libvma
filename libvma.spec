#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvma
Version  : 8.9.5
Release  : 8
URL      : https://github.com/Mellanox/libvma/archive/8.9.5/libvma-8.9.5.tar.gz
Source0  : https://github.com/Mellanox/libvma/archive/8.9.5/libvma-8.9.5.tar.gz
Summary  : A library for boosting TCP and UDP traffic (over RDMA hardware)
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: libvma-bin = %{version}-%{release}
Requires: libvma-lib = %{version}-%{release}
Requires: libvma-license = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
BuildRequires : glibc-bin
BuildRequires : libcap-dev
BuildRequires : libnl-dev
BuildRequires : rdma-core-dev
BuildRequires : valgrind
Patch1: 0001-Work-around-build-failure-on-recvmmsg-redefined.patch

%description
libvma is a LD_PRELOAD-able library that boosts performance
of TCP and UDP traffic.
It allows application written over standard socket API to handle 
fast path data traffic from user space over Ethernet and/or 
Infiniband with full network stack bypass and get better throughput, 
latency and packets/sec rate.
No application binary change is required for that.
libvma is supported by RDMA capable devices that support
"verbs" IBV_QPT_RAW_PACKET QP for Ethernet and/or IBV_QPT_UD QP for IPoIB.

%package bin
Summary: bin components for the libvma package.
Group: Binaries
Requires: libvma-license = %{version}-%{release}

%description bin
bin components for the libvma package.


%package dev
Summary: dev components for the libvma package.
Group: Development
Requires: libvma-lib = %{version}-%{release}
Requires: libvma-bin = %{version}-%{release}
Provides: libvma-devel = %{version}-%{release}
Requires: libvma = %{version}-%{release}

%description dev
dev components for the libvma package.


%package doc
Summary: doc components for the libvma package.
Group: Documentation

%description doc
doc components for the libvma package.


%package lib
Summary: lib components for the libvma package.
Group: Libraries
Requires: libvma-license = %{version}-%{release}

%description lib
lib components for the libvma package.


%package license
Summary: license components for the libvma package.
Group: Default

%description license
license components for the libvma package.


%prep
%setup -q -n libvma-8.9.5
cd %{_builddir}/libvma-8.9.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573499256
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1573499256
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libvma
cp %{_builddir}/libvma-8.9.5/COPYING %{buildroot}/usr/share/package-licenses/libvma/58d2b9d325c8b15fdd743be2040c275350091bf4
cp %{_builddir}/libvma-8.9.5/LICENSE %{buildroot}/usr/share/package-licenses/libvma/00ce6a8dfee21965deebb42fe9a54bed81866afa
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vma_stats
/usr/bin/vmad

%files dev
%defattr(-,root,root,-)
/usr/include/mellanox/vma_extra.h
/usr/lib64/libvma.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libvma/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvma.so.8
/usr/lib64/libvma.so.8.9.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvma/00ce6a8dfee21965deebb42fe9a54bed81866afa
/usr/share/package-licenses/libvma/58d2b9d325c8b15fdd743be2040c275350091bf4
