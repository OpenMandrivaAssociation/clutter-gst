%define name clutter-gst
%define version 1.6.0
%define release %mkrel 2

%define api 1.0
%define clutterapi 1.0
%define major 0
%define libname %mklibname %name %api %major
%define libnamedevel %mklibname -d %name %api

Summary:       GST video texture actor and audio player object for Clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
Patch0:        clutter-gst-nogl.patch
Patch1:        clutter-gst-automake-1.13.patch
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRequires: clutter-devel >= 1.6.14
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: gobject-introspection-devel >= 0.6.8
BuildRequires: gtk-doc
BuildRequires: docbook-dtd412-xml
BuildRequires: pkgconfig(gl)

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
Group:         Development/Other

%description doc
Documentation for Clutter-Gst

%prep
%setup -q
%apply_patches

%build
autoreconf
%configure2_5x \
  --disable-static \
  --enable-gtk-doc \
  --enable-introspection
%make

%install
rm -Rf %{buildroot}

%makeinstall_std

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/ClutterGst-1.0.typelib
%{_libdir}/gstreamer-0.10/libgstclutter.so

%files -n %libnamedevel
%{_libdir}/pkgconfig/%{name}-%{api}.pc
#%{_libdir}/lib%{name}-%{api}.la
%{_libdir}/lib%{name}-%{api}.so
%dir %{_includedir}/clutter-%{clutterapi}/%{name}
%{_includedir}/clutter-%{clutterapi}/%{name}/*.h
%{_datadir}/gir-1.0/ClutterGst-1.0.gir

%files doc
%defattr(-,root,root,-)
%dir %{_datadir}/gtk-doc/html/%name
%doc %{_datadir}/gtk-doc/html/%name/*




%changelog
* Tue Oct  2 2012 Arkady L. Shane <ashejn@rosalab.ru> 1.6.0-2
- rebuilt against new cogl	

* Mon Jun 06 2011 Götz Waschk <waschk@mandriva.org> 1.3.12-1mdv2011.0
+ Revision: 682985
- new version
- fix source URL

* Sun Apr 10 2011 Funda Wang <fwang@mandriva.org> 1.3.8-1
+ Revision: 652251
- update group
- new version 1.3.8
- new version 1.3.6

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Claudio Matsuoka <claudio@mandriva.com>
    - Update to version 1.2.0 for MeeGo 1.1

* Wed Feb 10 2010 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 503756
- new version
- new API
- update build deps

* Wed Jul 29 2009 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 404426
- new version
- new API
- update deps
- update file list

* Fri Jul 24 2009 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdv2010.0
+ Revision: 399404
- new version
- new api
- fix build
- update license

* Sat Sep 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.8.0-1mdv2009.0
+ Revision: 284375
- New version: 0.8.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Feb 21 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.1-2mdv2008.1
+ Revision: 173781
- Improve description

* Wed Feb 20 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.1-1mdv2008.1
+ Revision: 173177
- New version

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.4.0-1mdv2008.1
+ Revision: 136322
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Colin Guthrie <cguthrie@mandriva.org> 0.4.0-1mdv2008.0
+ Revision: 60530
- New version: 0.4.0

* Thu Jun 21 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.1-1mdv2008.0
+ Revision: 42385
- Import clutter-gst

