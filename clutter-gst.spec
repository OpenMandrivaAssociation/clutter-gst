%define name clutter-gst
%define version 1.3.6
%define release %mkrel 1

%define api 1.0
%define clutterapi 1.0
%define major 0
%define libname %mklibname %name %api %major
%define libnamedevel %mklibname -d %name %api

Summary:       GST video texture actor and audio player object for Clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       http://www.clutter-project.org/sources/clutter-gst/%api/%{name}-%{version}.tar.bz2
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel >= 1.4.0
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: gobject-introspection-devel >= 0.6.8
BuildRequires: gtk-doc
BuildRequires: docbook-dtd412-xml

%description
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

%package -n %libname
Summary:       GST video texture actor and audio player object for Clutter
Group:         Graphics
Requires:      gstreamer0.10-plugins-base

%description -n %libname
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

%package -n %libnamedevel
Summary:       Development headers/libraries for %name
Group:         Development/X11
Provides:      %{name}-devel = %{version}-%{release}
Requires:      %libname = %{version}-%{release}

%description -n %libnamedevel
Development headers/libraries for %name (see %libname package)

%package doc
Summary:       API reference for clutter-gst
Group:         Documentation

%description doc
Documentation for Clutter-Gst

%prep
%setup -q

%build
%configure2_5x \
  --disable-static \
  --enable-gtk-doc \
  --enable-introspection
%make

%install
rm -Rf %{buildroot}

%makeinstall_std

%clean
rm -Rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/ClutterGst-1.0.typelib

%files -n %libnamedevel
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/lib%{name}-%{api}.la
%{_libdir}/lib%{name}-%{api}.so
%dir %{_includedir}/clutter-%{clutterapi}/%{name}
%{_includedir}/clutter-%{clutterapi}/%{name}/*.h
%{_datadir}/gir-1.0/ClutterGst-1.0.gir

%files doc
%defattr(-,root,root,-)
%dir %{_datadir}/gtk-doc/html/%name
%doc %{_datadir}/gtk-doc/html/%name/*


