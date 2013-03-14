
%define plugin	suspendoutput
%define name	vdr-plugin-%plugin
%define version	1.0.1
%define rel	3

Summary:	VDR plugin: Suspend output
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		http://phivdr.dyndns.org/vdr/vdr-suspendoutput/
Source:		http://phivdr.dyndns.org/vdr/vdr-suspendoutput/vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Suspend vdr output (display still image instead of live video).
Suspending live TV releases current channel (DVB card) for
recording(s) and saves some CPU time with software decoders.
Blanking display while replay is paused can avoid burning the image
on tube.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# Show suspend/resume entry in main menu (default)
var=MENU
param=-m
# Don't show entry in main menu
var=NOMENU
param=-M
# Suspend output after MIN minutes of inactivity (default: 120 minutes)
var=TIMER_MIN
param=--timer=TIMER_MIN
# Disable inactivity timer
var=NOTIMER
param=-T
# Allow suspend when replay is paused
var=PAUSED
param=-p
# Show VDR logo when suspended
var=LOGO
param=-l
# Blank screen when suspended
var=BLANK
param=-b
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.0.1-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 396138
- new version
- update license tag

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.2.5-8mdv2009.1
+ Revision: 359371
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.2.5-7mdv2009.0
+ Revision: 197983
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.2.5-6mdv2009.0
+ Revision: 197728
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.2.5-5mdv2008.1
+ Revision: 145208
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.2.5-4mdv2008.1
+ Revision: 103218
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.2.5-3mdv2008.0
+ Revision: 50052
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.2.5-2mdv2008.0
+ Revision: 42135
- rebuild for new vdr

* Sun Jun 10 2007 Anssi Hannula <anssi@mandriva.org> 0.2.5-1mdv2008.0
+ Revision: 37872
- initial Mandriva release

