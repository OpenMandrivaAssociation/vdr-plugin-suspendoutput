%define plugin	suspendoutput

Summary:	VDR plugin: Suspend output
Name:		vdr-plugin-%plugin
Version:	1.0.1
Release:	5
Group:		Video
License:	GPLv2+
URL:		https://phivdr.dyndns.org/vdr/vdr-suspendoutput/
Source:		http://phivdr.dyndns.org/vdr/vdr-suspendoutput/vdr-%plugin-%{version}.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Suspend vdr output (display still image instead of live video).
Suspending live TV releases current channel (DVB card) for
recording(s) and saves some CPU time with software decoders.
Blanking display while replay is paused can avoid burning the image
on tube.

%prep
%setup -q -n %plugin-%{version}
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
%doc README HISTORY


