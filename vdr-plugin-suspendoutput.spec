
%define plugin	suspendoutput
%define name	vdr-plugin-%plugin
%define version	0.2.5
%define rel	4

Summary:	VDR plugin: Suspend output
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://phivdr.dyndns.org/vdr/vdr-suspendoutput/
Source:		http://phivdr.dyndns.org/vdr/vdr-suspendoutput/vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
Suspend vdr output (display still image instead of live video).
Suspending live TV releases current channel (DVB card) for
recording(s) and saves some CPU time with software decoders.
Blanking display while replay is paused can avoid burning the image
on tube.

%prep
%setup -q -n %plugin-%version

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
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
