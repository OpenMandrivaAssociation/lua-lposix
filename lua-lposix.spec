%define soname		posix
%define lua_version	5.1

Summary:	A POSIX library for the Lua programming language
Name:		lua-lposix
Version:	1.0
Release:	%{mkrel 4}
License:	Public Domain
Group:		Development/Other
URL:		http://www.tecgraf.puc-rio.br/~lhf/ftp/lua/
Source0:	lposix.tar.bz2
Patch0:		luaposix.patch
# From upstream reference (by Funda)
Patch1:		lposix-build-5.1.patch
# Corrects use of obsolete CLK_TCK constant to CLOCKS_PER_SEC - AdamW
# 2008/07 (see http://www.mail-archive.com/debian-glibc@lists.debian.org/msg34448.html )
Patch2:		lposix-clktck.patch
BuildRoot:	%_tmppath/%{name}-buildroot
BuildRequires:	lua-devel
Requires:	lua
# Relics from previous crack-addled packaging of this simple plugin
# as if it were a shared library. Debian goes the whole hog and
# installs lua plugins like this to /usr/lib as proper shared libs as
# well as installing them as lua plugins, but I don't see any need to
# go to that trouble as I don't know of any code which would actually
# want to link against this directly - AdamW 2008/07
Obsoletes:	%{mklibname posix 1} < %{version}-%{release}
Obsoletes:	%{mklibname luaposix} < %{version}-%{release}
Obsoletes:	%{mklibname luaposix 1} < %{version}-%{release}

%description
A POSIX module for the Lua programming language.

%package devel
Summary:	Development header for the lposix LUA module
Group:		Development/Other
License:	Public Domain
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{mklibname luaposix 1 -d} < %{version}-%{release}

%description devel
Development header for the lposix LUA module.

%prep
%setup -q -n %{soname}
%patch0 -p1
%patch1 -p0
%patch2 -p1 -b .clktck

%build
export CFLAGS="%{optflags} -fPIC"
%make

%install
%__rm -rf %{buildroot}
install -d %{buildroot}/%{_datadir}/lua/%{lua_version}
install -d %{buildroot}/%{_libdir}/lua/%{lua_version}
install -m0755 %{soname}.so %{buildroot}%{_libdir}/lua/%{lua_version}
install -m0644 %{soname}.a %{buildroot}/%{_libdir}/lua/%{lua_version}
install -m0644 %{soname}.lua %{buildroot}/%{_datadir}/lua/%{lua_version}
install -m0644 test.lua %{buildroot}/%{_datadir}/lua/%{lua_version}
install -m0644 tree.lua %{buildroot}/%{_datadir}/lua/%{lua_version}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/lua/%{lua_version}/*.so
%{_datadir}/lua/%{lua_version}/*.lua

%files devel
%defattr(-,root,root)
%{_libdir}/lua/%{lua_version}/*.a


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2010.0
+ Revision: 429882
- rebuild

* Thu Jul 17 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-3mdv2009.0
+ Revision: 237784
- buildrequires lua-devel
- import lua-lposix


