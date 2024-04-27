# TODO: use common system stb package (stb_image.h, stb_image_write.h)
Summary:	Tiny glTF library (loader/saver)
Summary(pl.UTF-8):	Mała biblioteka glTF (ładująca/zapisująca)
Name:		tinygltf
Version:	2.8.21
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/syoyo/tinygltf/releases
Source0:	https://github.com/syoyo/tinygltf/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	268fa79521795f4e067e5df34d898533
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/syoyo/tinygltf
BuildRequires:	cmake >= 3.6
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	nlohmann-json-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinyGLTF is a header only C++11 glTF 2.0
(<https://github.com/KhronosGroup/glTF>) library.

%description -l pl.UTF-8
TinyGLTF to składająca się z samych nagłówków, napisana w C++11
bibliotek glTF 2.0 (<https://github.com/KhronosGroup/glTF>).

%package devel
Summary:	Header files for TinyGLTF library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki TinyGLTF
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.7
Requires:	nlohmann-json-devel
# no base dependency: prebuilt library is optional (can be used as header-only)

%description devel
Header files for TinyGLTF library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki TinyGLTF.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# nlohmann-json
%{__rm} $RPM_BUILD_ROOT%{_includedir}/json.hpp

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libtinygltf.so

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
# TODO: common system stb_image
%{_includedir}/stb_image.h
%{_includedir}/stb_image_write.h
%{_includedir}/tiny_gltf.h
%{_libdir}/cmake/TinyGLTF*.cmake
