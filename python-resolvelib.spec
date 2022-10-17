# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-resolvelib
Epoch: 100
Version: 0.5.4
Release: 1%{?dist}
BuildArch: noarch
Summary: Resolve abstract dependencies into concrete ones
License: ISC
URL: https://github.com/sarugaku/resolvelib/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
ResolveLib at the highest level provides a Resolver class that includes
dependency resolution logic. You give it some things, and a little
information on how it should interact with them, and it will spit out a
resolution result.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-resolvelib
Summary: Resolve abstract dependencies into concrete ones
Requires: python3
Provides: python3-resolvelib = %{epoch}:%{version}-%{release}
Provides: python3dist(resolvelib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-resolvelib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(resolvelib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-resolvelib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(resolvelib) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-resolvelib
ResolveLib at the highest level provides a Resolver class that includes
dependency resolution logic. You give it some things, and a little
information on how it should interact with them, and it will spit out a
resolution result.

%files -n python%{python3_version_nodots}-resolvelib
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-resolvelib
Summary: Resolve abstract dependencies into concrete ones
Requires: python3
Provides: python3-resolvelib = %{epoch}:%{version}-%{release}
Provides: python3dist(resolvelib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-resolvelib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(resolvelib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-resolvelib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(resolvelib) = %{epoch}:%{version}-%{release}

%description -n python3-resolvelib
ResolveLib at the highest level provides a Resolver class that includes
dependency resolution logic. You give it some things, and a little
information on how it should interact with them, and it will spit out a
resolution result.

%files -n python3-resolvelib
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
