%define commit 2eb4cc9694f891ebc4139b9164cc733a856f0818

Name:           multimc
Version:        1.0
Release:        4%{?dist}
Summary:        MultiMC Launcher

License:        MS-PL
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
mkdir -p %{buildroot}/opt/multimc
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/man/man1
mkdir -p %{buildroot}%{_datadir}/metainfo

install -m 0644 launcher/package/ubuntu/multimc/opt/multimc/icon.svg %{buildroot}/opt/multimc/icon.svg
install -m 0755 launcher/package/ubuntu/multimc/opt/multimc/run.sh %{buildroot}/opt/multimc/run.sh
install -m 0644 launcher/package/ubuntu/multimc/usr/share/applications/multimc.desktop %{buildroot}%{_datadir}/applications/multimc.desktop
install -m 0644 launcher/package/ubuntu/multimc/usr/share/man/man1/multimc.1 %{buildroot}%{_datadir}/man/man1/multimc.1
install -m 0644 launcher/package/ubuntu/multimc/usr/share/metainfo/multimc.metainfo.xml %{buildroot}%{_datadir}/metainfo/multimc.metainfo.xml

%files
/opt/multimc
%{_datadir}/applications/multimc.desktop
%{_datadir}/man/man1/multimc.1*
%{_datadir}/metainfo/multimc.metainfo.xml

%postun
if [ $1 -eq 0 ]; then
    /usr/bin/update-desktop-database >/dev/null 2>&1 || :
fi
