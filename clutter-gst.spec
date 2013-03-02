%define url_ver %(echo %{version}|cut -d. -f1,2)

%define gstapi	1.0
%define api	2.0
%define major	0
%define libname	%mklibname %{name} %{api} %{major}
%define girname	%mklibname %{name}-gir %{api}
%define devname	%mklibname -d %{name} %{api}

Summary:	GST video texture actor and audio player object for Clutter
Name:		clutter-gst
Version:	2.0.2
Release:	1
License:	LGPLv2+
Group:		Graphics
Url:		http://clutter-project.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/clutter-gst/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	docbook-dtd412-xml
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})

%description
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

%package -n %{libname}
Summary:	GST video texture actor and audio player object for Clutter
Group:		Graphics
Requires:	gstreamer%{gstapi}-plugins-base

%description -n %{libname}
An integration library for using GStreamer with Clutter.
GST video texture actor and audio player object.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development headers/libraries for %{name}
Group:		Development/X11
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Obsoletes:	%{name}-doc

%description -n %{devname}
Development headers/libraries for %{name}.

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

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/gstreamer-%{gstapi}/libgstclutter.so

%files -n %{girname}
%{_libdir}/girepository-1.0/ClutterGst-%{api}.typelib

%files -n %{devname}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/lib%{name}-%{api}.so
%dir %{_includedir}/clutter-gst-%{api}/%{name}
%{_includedir}/clutter-gst-%{api}/%{name}/*.h
%{_datadir}/gir-1.0/ClutterGst-%{api}.gir
%dir %{_datadir}/gtk-doc/html/%{name}
%doc %{_datadir}/gtk-doc/html/%{name}/*

