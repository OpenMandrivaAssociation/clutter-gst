%define name clutter-gst
%define version 0.6.1
%define release %mkrel 4

%define api 0.6
%define major 0
%define libname %mklibname %name %api %major
%define libnamedevel %mklibname -d %name %api

Summary:       GST video texture actor and audio player object for Clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       %{name}-%{version}.tar.bz2
License:       LGPL
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: gtk-doc

%description
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

#----------------------------------------------------------------------------

%package -n %libname
Summary:       GST video texture actor and audio player object for Clutter
Group:         Graphics
Requires:      gstreamer0.10-plugins-base

%description -n %libname
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

#----------------------------------------------------------------------------

%package -n %libnamedevel
Summary:       Development headers/libraries for %name
Group:         Development/X11
Provides:      %name-devel = %version-%release
Requires:      %libname = %version-%release

%description -n %libnamedevel
Development headers/libraries for %name (see %libname package)

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %buildroot

%makeinstall

%clean
rm -rf %buildroot

%files -n %libname
%defattr(-,root,root)
%_libdir/lib%{name}-%{api}.so.*

%files -n %libnamedevel
%_libdir/pkgconfig/%{name}-%{api}.pc
%_libdir/lib%{name}-%{api}.la
%_libdir/lib%{name}-%{api}.so
%dir %_includedir/clutter-%{api}/%{name}
%_includedir/clutter-%{api}/%{name}/*.h
%dir %_datadir/gtk-doc/html/%name
%doc %_datadir/gtk-doc/html/%name/*
