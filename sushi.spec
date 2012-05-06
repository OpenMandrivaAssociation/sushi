%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define	api	1.0
%define	major	0
%define gmajor	1.0
%define	libname		%mklibname %{name} %{api} %{major}
%define	girname		%mklibname %{name}-gir %{gmajor}
%define	develname	%mklibname -d %{name} %{api}

Summary:	Quick Previewer for Nautilus
Name:		sushi
Version:	0.4.0
Release:	2
License:	GPLv2+
Group:		File tools
Url:		http://www.gnome.org/
Source0:	http://download.gnome.org/sources/sushi/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		sushi-0.3.91-linking.patch

#for gnome-autogen
BuildRequires:	gnome-common
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	unoconv
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(clutter-gst-1.0)
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(evince-document-3.0)
BuildRequires:	pkgconfig(evince-view-3.0)
BuildRequires:	pkgconfig(gjs-1.0)
BuildRequires:	pkgconfig(gjs-dbus-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-pbutils-0.10)
BuildRequires:	pkgconfig(gstreamer-tag-0.10)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(libmusicbrainz3)
BuildRequires:	pkgconfig(webkitgtk-3.0)
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

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
The sushi-devel package contains libraries and header files for developing
applications that use sushi.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/sushi
%{_libexecdir}/sushi-start
%{_datadir}/dbus-1/services/org.gnome.Sushi.service
%{_datadir}/sushi/

%files -n %{libname}
%{_libdir}/libsushi-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Sushi-%{gmajor}.typelib

%files -n %{develname}
%{_libdir}/libsushi-%{api}.so
%{_datadir}/gir-1.0/Sushi-%{gmajor}.gir

