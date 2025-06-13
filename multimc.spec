%define commit develop

Name:           multimc
Version:        1.0
Release:        1%{?dist}
Summary:        MultiMC Launcher

License:        MIT
URL:            https://github.com/MultiMC/Launcher
Source0:        https://github.com/MultiMC/Launcher/archive/%{commit}.tar.gz

BuildArch:      noarch

Requires:       desktop-file-utils
Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       qt5-qtsvg
Requires:       wget
Requires:       zenity


%description
A local install wrapper for MultiMC

%prep
%setup -q -n Launcher-%{commit}

%build

%install
cp -a launcher/package/ubuntu/multimc/opt %{buildroot}/
cp -a launcher/package/ubuntu/multimc/usr %{buildroot}/

%files
/*

%postun
if [ $1 -eq 0 ]; then
    /usr/bin/update-desktop-database >/dev/null 2>&1 || :
fi
