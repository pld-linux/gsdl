#
# TODO:
# - add BRs,
# - add polish desc,
# - check if it's compile ;)
# - finish all ;>
#
Summary:	Software to serve digital library collections
Summary(pl):	Program do obs³ugi cyfrowych bibliotek danych
Name:		gsdl
Version:	2.39
Release:	0.1
License:	GPL
Group:		Applications/Utilities
Source0:	http://prdownloads.sourceforge.net/greenstone/%{name}-%{version}-src.tgz
Patch0:		%{name}-configure.patch
URL:		http://www.greenstone.org/
BuildRequires:	gdbm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Greenstone is a suite of software which has the ability to serve
digital library collections and build new collections. It provides
a new way of organizing information and publishing it on the Internet
or on CD-ROM. Greenstone is produced by the New Zealand Digital Library
Project at the University of Waikato, and distributed in cooperation
with UNESCO and the Human Info NGO. It is open-source software, available
from http://greenstone.org/ under the terms of the GNU General Public
License. 

%description -l pl

%prep
%setup -q -n %{name}
%patch -p1

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
