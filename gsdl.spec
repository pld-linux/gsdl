#
# TODO:
# - add BRs,
# - check if it's compile ;)
# - finish all ;>
# - wrong, see at packages, build gsdl with shared programs and libs
#
Summary:	Software to serve digital library collections
Summary(pl.UTF-8):	Program do obsługi cyfrowych bibliotek danych
Name:		gsdl
Version:	2.39
Release:	0.1
License:	GPL
Group:		Applications/Utilities
Source0:	http://dl.sourceforge.net/greenstone/%{name}-%{version}-src.tgz
# Source0-md5:	83e3900810f62fca8ab2bc8c102d211a
Patch0:		%{name}-configure.patch
URL:		http://www.greenstone.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Greenstone is a suite of software which has the ability to serve
digital library collections and build new collections. It provides
a new way of organizing information and publishing it on the Internet
or on CD-ROM. Greenstone is produced by the New Zealand Digital
Library Project at the University of Waikato, and distributed in
cooperation with UNESCO and the Human Info NGO. It is open-source
software, available from http://greenstone.org/ under the terms of the
GNU General Public License.

%description -l pl.UTF-8
Greenstone to pakiet oprogramowania dający możliwość serwowania
zbiorów biblioteki cyfrowej oraz tworzenie nowych zbiorów. Udostępnia
nową metodę organizowania informacji i publikowania jej w Internecie
lub na płytach CD-ROM. Greenstone jest tworzony przez New Zealand
Digital Library Project (nowozelandzki projekt cyfrowej biblioteki) i
rozpowszechniany w kooperacji z UNESCO oraz Human Info NGO. Jest to
wolne oprogramowanie, dostępne pod http://greenstone.org/ na warunkach
Powszechnej Licencji Publicznej GNU (GPL).

%prep
%setup -q -n %{name}
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
