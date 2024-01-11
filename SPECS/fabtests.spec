Name:           fabtests
Version:        1.18.0
Release:        1%{?dist}.1
Summary:        Test suite for libfabric API
# include/jsmn.h and common/jsmn.c are licensed under MIT.
# All other source files permit distribution under BSD. Some of them
# additionaly expressly allow the option to be licensed under GPLv2.
# See the license headers in individual source files to see which those are.
License:        BSD and (BSD or GPLv2) and MIT
Url:            https://github.com/ofiwg/libfabric
Source:         https://github.com/ofiwg/libfabric/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Patch0:         0001-adjust-shebang-lines-in-rft_yaml_to_junit_xml-and-ru.patch
BuildRequires:  libfabric-devel >= %{version}
BuildRequires:  valgrind-devel
BuildRequires:  gcc
BuildRequires:  make
Requires:       python3-pytest

%description
Fabtests provides a set of examples that uses libfabric - a high-performance
fabric software library.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p2

%build
%configure --with-valgrind
make %{?_smp_mflags} V=1

%install
%make_install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%files
%{_datadir}/%{name}/
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*
%doc AUTHORS README
%license COPYING

%changelog
* Tue Jul 11 2023 Kamal Heib <kheib@redhat.com> - 1.18.0-1.1
- Rebuilt for fixing tag.
- Resolves: rhbz#2214187

* Mon Jun 12 2023 Kamal Heib <kheib@redhat.com> - 1.18.0-1
- Update to upstream release 1.18.0
- Add gating tests
- Resolves: rhbz#2214187

* Wed Feb 08 2023 Michal Schmidt <mschmidt@redhat.com> - 1.17.0-2
- Update to upstream release 1.17.0
- Require python3-pytest
- Resolves: rhbz#2168114, rhbz#2159964

* Fri Aug 19 2022 Michal Schmidt <mschmidt@redhat.com> - 1.15.1-1
- Update to upstream release 1.15.1
- Resolves: rhbz#2114061

* Fri Nov 26 2021 Honggang Li <honli@redhat.com> - 1.14.0-1
- Rebase to upstream release v1.14.0
- Resolves: bz2008510

* Thu May 13 2021 Honggang Li <honli@redhat.com> - 1.12.1-1
- Rebase to upstream release v1.12.1
- Resolves: bz1960071

* Tue Dec 22 2020 Honggang Li <honli@redhat.com> - 1.11.2-1
- Rebase to upstream release v1.11.2
- Resolves: bz1909635

* Tue Nov 17 2020 Honggang Li <honli@redhat.com> - 1.11.1-1
- Rebase to upstream release v1.11.1
- Resolves: bz1856274

* Sat Apr 25 2020 Honggang Li <honli@redhat.com> - 1.10.0
- Rebase to upstream release v1.10.0
- Resolves: bz1770651

* Mon Nov 11 2019 Honggang Li <honli@redhat.com> - 1.9.0rc1-1
- Rebase to upstream release v1.9.0rc1
- Resolves: bz1770650

* Mon Jul  1 2019 Honggang Li <honli@redhat.com> - 1.8.0-1
- Rebase to upstream release v1.8.0
- Resolves: bz1710870

* Mon Dec 10 2018 Honggang Li <honli@redhat.com> - 1.6.2-1
- Rebase to upstream release v1.6.2
- Resolves: bz1654871

* Sat Aug  4 2018 Florian Weimer <fweimer@redhat.com> - 1.6.1-3
- Fix shell syntax error in %%build

* Fri Aug  3 2018 Florian Weimer <fweimer@redhat.com> - 1.6.1-2
- Honor %%{valgrind_arches}

* Fri Jun 22 2018 Honggang Li <honli@redhat.com> - 1.6.1-1
- Rebase to upstream release v1.6.1
- Resolves: bz1448975

* Thu May 10 2018 Honggang Li <honli@redhat.com> - 1.6.0-1
- Rebase to upstream release v1.6.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Honggang Li <honli@redhat.com> - 1.4.1-1
- Rebase to latest upstream release.
- Resolves: bz1428619

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov  8 2016 Honggang Li <honli@redhat.com> - 1.4.0-1
- Rebase to latest upstream release.

* Tue Apr 19 2016 Honggang Li <honli@redhat.com> - 1.3.0-3
- Provide precise license information.

* Thu Apr 14 2016 Honggang Li <honli@redhat.com> - 1.3.0-2
- Remove license comment in file section.
- Merge duplicated file entries.

* Thu Apr 14 2016 Honggang Li <honli@redhat.com> - 1.3.0-1
- Import fabtests for Fedora.
