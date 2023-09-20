%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define	api	1.0
%define	major	0
%define gmajor	1.0
%define	libname	%mklibname %{name} %{api} %{major}
%define	girname	%mklibname %{name}-gir %{gmajor}
%define	devname	%mklibname -d %{name} %{api}

Summary:	Quick Previewer for Nautilus
Name:		sushi
Version:	45.0
Release:	1
License:	GPLv2+
Group:		File tools
Url:		https://www.gnome.org/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/sushi/%{url_ver}/%{name}-%{version}.tar.xz

#for gnome-autogen
BuildRequires:  gjs
BuildRequires:  meson
BuildRequires:	gnome-common
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	unoconv
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(clutter-gst-2.0)
BuildRequires:	pkgconfig(clutter-gst-3.0)
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
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:	pkgconfig(libmusicbrainz5)
BuildRequires:	pkgconfig(webkit2gtk-4.1)
Requires:	nautilus

%description
Sushi is a quick previewer for Nautilus, the GNOME desktop file manager.

%package -n %{libname}
Summary:	Runtime libraries for %{name}
Group:		System/Libraries
# When built with unoconv support, the library will use unoconv to
# read LibreOffice files
Recommends:	unoconv

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
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/sushi
%{_libexecdir}//org.gnome.NautilusPreviewer
%{_datadir}/dbus-1/services/org.gnome.NautilusPreviewer.service
%{_datadir}/metainfo/org.gnome.NautilusPreviewer.appdata.xml
%{_datadir}/sushi/gtksourceview-4/styles/builder-dark.style-scheme.xml
%{_datadir}/sushi/org.gnome.NautilusPreviewer.data.gresource
%{_datadir}/sushi/org.gnome.NautilusPreviewer.src.gresource

%files -n %{libname}
%{_libdir}/%{name}/libsushi-%{api}.so

%files -n %{girname}
%{_libdir}/%{name}/girepository-1.0/Sushi-%{gmajor}.typelib

%files -n %{devname}
%{_datadir}/%{name}/gir-1.0/Sushi-%{gmajor}.gir

