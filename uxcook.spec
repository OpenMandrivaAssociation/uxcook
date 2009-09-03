Summary:	Fix problems resulting of improperly set FTP downloads
Name:		uxcook
Version:	2.0.1
Release:	%mkrel 15
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


