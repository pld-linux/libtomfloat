Summary:	LibTomFloat - multiple precision floating point arithmetic library
Summary(pl.UTF-8):	LibTomFloat - biblioteka arytmetyki zmiennoprzecinkowej wielokrotnej precyzji
Name:		libtomfloat
Version:	0.02
Release:	1
License:	Public Domain
Group:		Libraries
#Source0Download: https://github.com/libtom/libtomfloat/releases
Source0:	https://github.com/libtom/libtomfloat/releases/download/%{version}/ltf-%{version}.tar.bz2
# Source0-md5:	c0fe359add600b9a895d23ca410a7a90
Patch0:		%{name}-make.patch
URL:		http://www.libtom.net/LibTomFloat/
BuildRequires:	libtommath-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibTomFloat is a library of source code that provides multiple
precision floating point arithmetic. It allows developers to
manipulate floating point numbers of variable precision. The library
was written in portable ISO C source code and depends upon the public
domain LibTomMath package.

%description -l pl.UTF-8
LibTomFloat to mająca otwarte źródła biblioteka arytmetyki
zmiennoprzecinkowej wielokrotnej precyzji. Pozwala programistom
wykonywać operacje na liczbach zmiennoprzecinkowych o zmiennej
precyzji. Biblioteka została napisana w przenośnym ISO C i jest
zależna od pakietu LibTomMath, wydanego także jako public domain.

%package devel
Summary:	Header files for LibTomFloat library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LibTomFloat
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libtommath-devel

%description devel
Header files for LibTomFloat library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LibTomFloat.

%package static
Summary:	Static LibTomFloat library
Summary(pl.UTF-8):	Statyczna biblioteka LibTomFloat
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LibTomFloat library.

%description static -l pl.UTF-8
Statyczna biblioteka LibTomFloat.

%prep
%setup -q
%patch -P0 -p1

%build
CFLAGS="%{rpmcflags}" \
%{__make} -f makefile \
	GCC="%{__cc}" \
	LIBPATH=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -f makefile install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBPATH=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE TODO WARNING changes.txt
%attr(755,root,root) %{_libdir}/libtomfloat.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtomfloat.so.0

%files devel
%defattr(644,root,root,755)
%doc float.pdf
%attr(755,root,root) %{_libdir}/libtomfloat.so
%{_libdir}/libtomfloat.la
%{_includedir}/tomfloat.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libtomfloat.a
