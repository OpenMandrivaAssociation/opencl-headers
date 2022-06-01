Name:           opencl-headers
Version:        2022.05.18
Release:        1
Summary:        OpenCL (Open Computing Language) header files
License:        MIT
URL:            https://www.khronos.org/registry/cl/
Source0:        https://github.com/KhronosGroup/OpenCL-Headers/archive/refs/tags/v%{version}/OpenCL-Headers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	cmake ninja

%description
%{summary}.

%prep
%autosetup -n OpenCL-Headers-%{version}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%check
cd build && ctest

%files
%{_includedir}/CL
%{_datadir}/cmake/OpenCLHeaders
