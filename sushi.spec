%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define	api	1.0
%define	major	0
%define gmajor	1.0
%define	libname	%mklibname %{name} %{api} %{major}
%define	girname	%mklibname %{name}-gir %{gmajor}
%define	devname	%mklibname -d %{name} %{api}

Summary:	Quick Previewer for Nautilus
Name:		sushi
Version:	3.18.0
Release:	3
License:	GPLv2+
Group:		File tools
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sushi/%{url_ver}/%{name}-%{version}.tar.xz

#for gnome-autogen
BuildRequires:	gnome-common
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(clutter-gst-2.0)
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(evince-document-3.0)
BuildRequires:	pkgconfig(evince-view-3.0)
BuildRequires:	pkgconfig(gjs-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:	pkgconfig(gstreamer-tag-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:	pkgconfig(webkit2gtk-4.0)
Suggests:	nautilus

%description
Sushi is a quick previewer for Nautilus, the GNOME desktop file manager.

%package -n %{libname}
Summary:	Runtime libraries for %{name}
Group:		System/Libraries
# When built with unoconv support, the library will use unoconv to
# read LibreOffice files
Suggests:	unoconv

%description -n %{libname}
Runtime libraries for %{name}.

%package -n %{girname}
Summary:	GObject introspection interface for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject introspection interface for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The sushi-devel package contains libraries and header files for developing
applications that use sushi.

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/sushi
%{_libexecdir}/sushi-start
%{_datadir}/dbus-1/services/org.gnome.Sushi.service
%{_datadir}/sushi/js

%files -n %{libname}
%{_libdir}/%{name}/libsushi-%{api}.so

%files -n %{girname}
%{_libdir}/%{name}/girepository-1.0/Sushi-%{gmajor}.typelib

%files -n %{devname}
%{_datadir}/%{name}/gir-1.0/Sushi-%{gmajor}.gir

