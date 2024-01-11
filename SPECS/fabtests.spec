Name:           fabtests
Version:        1.17.0
Release:        2%{?dist}
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
* Fri Feb 03 2023 Michal Schmidt <mschmidt@redhat.com> - 1.17.0-2
- Require python3-pytest
- Resolves: rhbz#2166804

* Fri Feb 03 2023 Kamal Heib <kheib@redhat.com> - 1.17.0-1
- Update to upstream release 1.17.0
- Resolves: rhbz#2166804

* Wed Aug 03 2022 Michal Schmidt <mschmidt@redhat.com> - 1.15.1-1
- Update to upstream release 1.15.1
- Resolves: rhbz#2114058

* Thu Nov 25 2021 Honggang Li <honli@redhat.com> - 1.14.0-1
- Rebase to upstream release v1.14.0
- Related: rhbz#2015405

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.12.1-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 1.12.1-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Apr 02 2021 Honggang Li <honli@redhat.com> - 1.12.1-1
- Rebase to upstream release v1.12.1

* Sun Jan 31 2021 Honggang Li <honli@redhat.com> - 1.12.0-0.1
- Rebase to upstream release v1.12.0rc1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 2020 Honggang Li <honli@redhat.com> - 1.11.2-1
- Rebase to upstream release v1.11.2

* Wed Dec 09 2020 Honggang Li <honli@redhat.com> - 1.11.2-0.1
- Rebase to upstream release v1.11.2rc1

* Sun Oct 11 2020 Honggang Li <honli@redhat.com> - 1.11.1
- Rebase to upstream release v1.11.1

* Fri Oct 09 2020 Honggang Li <honli@redhat.com> - 1.11.1rc1-1
- Rebase to upstream release v1.11.1rc1

* Mon Aug 17 2020 Honggang Li <honli@redhat.com> - 1.11.0-1
- Rebase to upstream release v1.11.0

* Wed Aug 05 2020 Honggang Li <honli@redhat.com> - 1.11.0rc2-1
- Rebase to upstream release v1.11.0rc2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Honggang Li <honli@redhat.com> - 1.11.0rc1-1
- Rebase to upstream release v1.11.0rc1

* Sat May 09 2020 Honggang Li <honli@redhat.com> - 1.10.1-1
- Rebase to upstream release v1.10.1

* Fri Apr 24 2020 Honggang Li <honli@redhat.com> - 1.10.0-1
- Rebase to upstream release v1.10.0

* Sun Apr 12 2020 Honggang Li <honli@redhat.com> - 1.10.0rc2-1
- Rebase to upstream release v1.10.0rc2

* Sat Apr 04 2020 Honggang Li <honli@redhat.com> - 1.10.0rc1-1
- Rebase to upstream release v1.10.0rc1

* Mon Mar 09 2020 Honggang Li <honli@redhat.com> - 1.9.1
- Rebase to upstream release v1.9.1

* Mon Feb 17 2020 Honggang Li <honli@redhat.com> - 1.9.1rc1-1
- Rebase to upstream release v1.9.1rc1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Honggang Li <honli@redhat.com> - 1.9.0rc1-1
- Rebase to upstream release v1.9.0rc1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Honggang Li <honli@redhat.com> - 1.8.0-1
- Rebase to upstream release v1.8.0

* Mon Apr 15 2019 Honggang Li <honli@redhat.com> - 1.7.1-1
- Rebase to upstream release v1.7.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 31 2019 Honggang Li <honli@redhat.com> - 1.7.0-1
- Rebase to upstream release v1.7.0
- Resolves: bz1671197

* Tue Oct  9 2018 Honggang Li <honli@redhat.com> - 1.6.2-1
- Rebase to upstream release v1.6.2
- Resolves: bz1637336

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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
