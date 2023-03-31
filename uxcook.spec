Summary:	Fix problems resulting of improperly set FTP downloads
Name:		uxcook
Version:	2.0.1
Release:	29
License:	GPL
Group:		File tools
URL:		http://www.free-music.com/uxcook.htm
Source0:	http://www.free-music.com/%{name}-%{version}.tar.bz2
Patch0:		uxcook-fix-overriding-cflags.patch
Patch1:		uxcook-2.0.1-LDFLAGS.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is basically a clone of Uncook95 (which runs under Microsoft Windows). It
is designed to allow Netscape users to fix MP3 files that were retrieved from
improperly set servers. Of course this is not limited to MP3 files.

Actually, these problems mainly come from binary files downloaded in ASCII mode
(e.g. when a server sends binary information as text it inserts linefeeds at
semi-regular intervals). With uxcook you will avoid re-doing the download.

%prep

%setup -q
%patch0 -p0
%patch1 -p0

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/%{name}




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-18mdv2011.0
+ Revision: 670758
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-17mdv2011.0
+ Revision: 608120
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-16mdv2010.1
+ Revision: 519079
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.1-15mdv2010.0
+ Revision: 427487
- rebuild

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-14mdv2009.1
+ Revision: 317916
- use %%ldflags

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.0.1-13mdv2009.0
+ Revision: 225915
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-12mdv2008.1
+ Revision: 178850
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-11mdv2007.0
+ Revision: 134476
- Import uxcook

* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-11mdv2007.1
- use the %%mkrel macro

* Sun Jan 01 2006 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0.1-10mdk
- Rebuild

* Fri Nov 19 2004 Olivier Blin <blino@mandrake.org> 2.0.1-9mdk
- birthday rebuild

