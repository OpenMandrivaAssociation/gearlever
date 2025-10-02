%global debug_package %{nil}

Name:		gearlever
Version:	3.4.4
Release:	1
Source0:	https://github.com/mijorus/gearlever/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	Manage AppImages with ease
URL:		https://github.com/mijorus/gearlever
License:	GPL-3.0
Group:		Package Management

BuildSystem:	meson
BuildRequires:	meson
BuildRequires:	gettext
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	gtk-update-icon-cache
BuildRequires:	desktop-file-utils

Requires:	python%{pyver}dist(pygobject)
Requires:	python%{pyver}dist(pydbus)
Requires:	%{mklibname adwaita}
Requires:   python%{pyver}dist(pyxdg)
Requires:   fcitx-gtk3


%description
%summary

%prep
%autosetup -p1

%files
%{_bindir}/%{name}
%{_datadir}/appdata/*
%{_datadir}/%{name}
%{_iconsdir}/hicolor/scalable/actions/*
%{_datadir}/applications/*
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/gearlever.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/gearlever.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/gearlever.mo
%lang(fi_FI) %{_datadir}/locale/fi_FI/LC_MESSAGES/gearlever.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/gearlever.mo
%lang(hi) %{_datadir}/locale/hi/LC_MESSAGES/gearlever.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/gearlever.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/gearlever.mo
%lang(oc) %{_datadir}/locale/oc/LC_MESSAGES/gearlever.mo
%lang(pl_PL) %{_datadir}/locale/pl_PL/LC_MESSAGES/gearlever.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/gearlever.mo
%lang(pt_PT) %{_datadir}/locale/pt_PT/LC_MESSAGES/gearlever.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/gearlever.mo
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/gearlever.mo
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/gearlever.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/gearlever.mo
%{_iconsdir}/*/*/*/it.mijorus.gearlever*
%{_datadir}/glib-2.0/*/it.mijorus.gearlever.gschema.xml


