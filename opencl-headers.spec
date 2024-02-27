%global cl_hpp_ver 2023.12.14

Name:           opencl-headers
Version:        2023.12.14
Release:        2
Summary:        OpenCL (Open Computing Language) header files
License:        MIT
URL:            https://www.khronos.org/registry/cl/
Source0:        https://github.com/KhronosGroup/OpenCL-Headers/archive/refs/tags/v%{version}/OpenCL-Headers-%{version}.tar.gz
Source1:        https://github.com/KhronosGroup/OpenCL-CLHPP/archive/v%{cl_hpp_ver}/OpenCL-CLHPP-v%{cl_hpp_ver}.tar.gz
BuildArch:      noarch
BuildRequires:	cmake
BuildRequires:	ninja

%description
%{summary}.

%prep
%autosetup -n OpenCL-Headers-%{version}

tar -xf %{SOURCE1}
cp -p OpenCL-CLHPP-%{cl_hpp_ver}/include/CL/{cl2,opencl}.hpp .

%cmake -G Ninja

%build
%ninja_build -C build

%install

%ninja_install -C build

mkdir -p %{buildroot}%{_includedir}/CL/
install -p -m 0644 *hpp -t %{buildroot}%{_includedir}/CL/
sed -e 's|@CMAKE_INSTALL_PREFIX@|%{_prefix}|' -e 's|@OPENCLHPP_INCLUDEDIR_PC@|%{_includedir}|' OpenCL-CLHPP-%{cl_hpp_ver}/OpenCL-CLHPP.pc.in > %{buildroot}%{_datadir}/pkgconfig/OpenCL-CLHPP.pc

%check
cd build && ctest

%files
%{_includedir}/CL
%{_datadir}/cmake/OpenCLHeaders
%{_datadir}/pkgconfig/OpenCL-Headers.pc
%{_datadir}/pkgconfig/OpenCL-CLHPP.pc
