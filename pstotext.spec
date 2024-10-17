%define name	pstotext
%define version 1.9
%define	rel	1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary: Extract text from PostScript files
Name:	 %{name}
Version: %{version}
Release: %{release}
Source0: ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/contrib/%{name}-%{version}.tar.gz
License: GPL
Group:	 Publishing
Url:   https://pages.cs.wisc.edu/~ghost/doc/pstotext.htm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:  ghostscript

%description
pstotext extracts plain text from PostScript files using GhostScript.

%prep
%setup -q

%build
%make

%install
%__rm -rf %{buildroot}

%__install -d -m 755 %{buildroot}%{_bindir}
%__install -m 755 pstotext %{buildroot}%{_bindir}
%__install -d -m 755 %{buildroot}%{_mandir}/man1
%__install -m 755 pstotext.1 %{buildroot}%{_mandir}/man1

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/pstotext
%_mandir/man1/pstotext.*


%changelog
* Wed Sep 05 2012 Lev Givon <lev@mandriva.org> 1.9-1
+ Revision: 816357
- imported package pstotext

