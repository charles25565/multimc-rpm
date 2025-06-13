%define commit 2eb4cc9694f891ebc4139b9164cc733a856f0818

Name:           multimc
Version:        1.0
Release:        2%{?dist}
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
/opt/multimc/icon.svg
/opt/multimc/run.sh
/usr/share/applications/multimc.desktop
/usr/share/man/man1/multimc.1
/usr/share/metainfo/multimc.metainfo.xml

%postun
if [ $1 -eq 0 ]; then
    /usr/bin/update-desktop-database >/dev/null 2>&1 || :
fi
