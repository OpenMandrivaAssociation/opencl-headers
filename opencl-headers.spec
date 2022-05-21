
%global date 2022.01.04
%global cl_hpp_ver 2.0.16

Name:           opencl-headers
Version:        2022.01.04
Release:        1
Summary:        OpenCL (Open Computing Language) header files

License:        MIT
URL:            https://www.khronos.org/registry/cl/

Source0:        https://github.com/KhronosGroup/OpenCL-Headers/archive/refs/tags/v%{version}/OpenCL-Headers-%{version}.tar.gz
Source1:        https://github.com/KhronosGroup/OpenCL-CLHPP/archive/refs/tags/v%{cl_hpp_ver}/OpenCL-CLHPP%{cl_hpp_ver}.tar.gz
# OCL 1.2 compatibility
Source2:        https://www.khronos.org/registry/cl/api/2.1/cl.hpp

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n OpenCL-Headers-%{version}

tar -xf %{SOURCE1}
cp -p OpenCL-CLHPP-%{cl_hpp_ver}/include/CL/{cl2,opencl}.hpp %{SOURCE2} .

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_includedir}/CL/
install -p -m 0644 *hpp CL/* -t %{buildroot}%{_includedir}/CL/
# We're not interested in Direct3D things
rm -vf %{buildroot}%{_includedir}/CL/cl_{dx9,d3d}*

%files
%dir %{_includedir}/CL
%{_includedir}/CL/cl2.hpp
%{_includedir}/CL/cl_egl.h
%{_includedir}/CL/cl_ext.h
%{_includedir}/CL/cl_ext_intel.h
%{_includedir}/CL/cl_gl_ext.h
%{_includedir}/CL/cl_gl.h
%{_includedir}/CL/cl.h
%{_includedir}/CL/cl_half.h
%{_includedir}/CL/cl.hpp
%{_includedir}/CL/cl_icd.h
%{_includedir}/CL/cl_layer.h
%{_includedir}/CL/cl_platform.h
%{_includedir}/CL/cl_va_api_media_sharing_intel.h
%{_includedir}/CL/cl_version.h
%{_includedir}/CL/opencl.h
%{_includedir}/CL/opencl.hpp
