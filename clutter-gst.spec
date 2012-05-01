%define api 1.0
%define major 0
%define gir_major 1.0
%define libname		%mklibname %{name} %{api} %{major}
%define girname		%mklibname %{name}-gir %{api}
%define develname	%mklibname -d %{name} %{api}

Summary:	GST video texture actor and audio player object for Clutter
Name:		clutter-gst
Version:	1.5.4
Release:	1
License:	LGPLv2+
Group:		Graphics
Url:		http://clutter-project.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires: gtk-doc
BuildRequires: docbook-dtd412-xml
BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-0.10)

%description
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

%package -n %{libname}
Summary:	GST video texture actor and audio player object for Clutter
Group:		Graphics
Requires:	gstreamer0.10-plugins-base

%description -n %{libname}
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:       Development headers/libraries for %{name}
Group:         Development/X11
Provides:      %{name}-devel = %{version}-%{release}
Requires:      %{libname} = %{version}-%{release}
Requires:      %{girname} = %{version}-%{release}

%description -n %{develname}
Development headers/libraries for %{name} (see %{libname} package)

%package doc
Summary:       API reference for clutter-gst
Group:         Development/Other

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
%makeinstall_std
find %{buildroot} -name *.la | xargs rm

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/gstreamer-0.10/libgstclutter.so

%files -n %{girname}
%{_libdir}/girepository-1.0/ClutterGst-1.0.typelib

%files -n %{develname}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/lib%{name}-%{api}.so
%dir %{_includedir}/clutter-%{api}/%{name}
%{_includedir}/clutter-%{api}/%{name}/*.h
%{_datadir}/gir-1.0/ClutterGst-1.0.gir

%files doc
%dir %{_datadir}/gtk-doc/html/%{name}
%doc %{_datadir}/gtk-doc/html/%{name}/*

