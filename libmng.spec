Summary:	A library of functions for manipulating MNG format files
Name:		libmng
Version:	2.0.2
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libmng/%{name}-%{version}.tar.xz
# Source0-md5:	3804bf2523af9b4e0670b5982b3bf984
URL:		http://www.libmng.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmng - library for reading, writing, displaying and examing
Multiple-Image Network Graphics. MNG is the animation extension to the
popular PNG image-format.

%package devel
Summary:	Development tools for programs to manipulate MNG format files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libmng-devel package contains the header files necessary for
developing programs using the MNG (Multiple-Image Network Graphics)
library.

If you want to develop programs which will manipulate MNG image format
files, you should install libmng-devel. You'll also need to install
the libmng package.

%prep
%setup -q

%{__sed} -i "/AM_C_PROTOTYPES/d" makefiles/configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static	\
	--with-jpeg		\
	--with-zlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.2
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc doc/{doc.readme,libmng.txt,Plan*.png}
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*

