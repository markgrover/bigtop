# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
%define etc_hbase /etc/hbase
%define hbase_home /usr/lib/hbase
%define bin_hbase %{hbase_home}/bin
%define lib_hbase %{hbase_home}/lib
%define conf_hbase %{hbase_home}/conf
%define logs_hbase %{hbase_home}/logs
%define pids_hbase %{hbase_home}/pids
%define webapps_hbase %{hbase_home}/hbase-webapps
%define doc_hbase %{_docdir}/hbase-%{hbase_version}
%define man_dir %{_mandir}
%define hbase_username hbase
%define hbase_services master regionserver thrift

%if  %{?suse_version:1}0

# Only tested on openSUSE 11.4. le'ts update it for previous release when confirmed
%if 0%{suse_version} > 1130
%define suse_check \# Define an empty suse_check for compatibility with older sles
%endif

# SLES is more strict anc check all symlinks point to valid path
# But we do point to a hadoop jar which is not there at build time
# (but would be at install time).
# Since our package build system does not handle dependencies,
# these symlink checks are deactivated
%define __os_install_post \
    %{suse_check} ; \
    /usr/lib/rpm/brp-compress ; \
    %{nil}


%global initd_dir %{_sysconfdir}/rc.d

%else

%global initd_dir %{_sysconfdir}/rc.d/init.d

%endif


Name: hadoop-hbase
Version: %{hbase_version}
Release: %{hbase_release}
Summary: HBase is the Hadoop database. Use it when you need random, realtime read/write access to your Big Data. This project's goal is the hosting of very large tables -- billions of rows X millions of columns -- atop clusters of commodity hardware. 
URL: http://hadoop.apache.org/hbase/
Group: Development/Libraries
Buildroot: %{_topdir}/INSTALL/%{name}-%{version}
License: APL2
Source0: hbase-%{hbase_base_version}.tar.gz
Source1: hadoop-hbase.sh
Source2: hadoop-hbase.sh.suse
Source3: hbase.default
Source4: install_hbase.sh
BuildArch: noarch
Requires: sh-utils, textutils, /usr/sbin/useradd, /sbin/chkconfig, /sbin/service, hadoop-zookeeper, hadoop >= 0.20.2, hadoop-zookeeper >= 3.3.1

# RHEL6 provides natively java
%if 0%{?rhel} == 6
BuildRequires: java-1.6.0-sun-devel
Requires: java-1.6.0-sun
%else
BuildRequires: jdk >= 1.6
Requires: jre >= 1.6
%endif

%description 
HBase is an open-source, distributed, column-oriented store modeled after Google' Bigtable: A Distributed Storage System for Structured Data by Chang et al. Just as Bigtable leverages the distributed data storage provided by the Google File System, HBase provides Bigtable-like capabilities on top of Hadoop. HBase includes:

    * Convenient base classes for backing Hadoop MapReduce jobs with HBase tables
    * Query predicate push down via server side scan and get filters
    * Optimizations for real time queries
    * A high performance Thrift gateway
    * A REST-ful Web service gateway that supports XML, Protobuf, and binary data encoding options
    * Cascading source and sink modules
    * Extensible jruby-based (JIRB) shell
    * Support for exporting metrics via the Hadoop metrics subsystem to files or Ganglia; or via JMX

%package master
Summary: The Hadoop HBase master Server.
Group: System/Daemons
Provides: hbase-master
Requires: %{name} = %{version}-%{release}

%if  %{?suse_version:1}0
# Required for init scripts
Requires: insserv
%else
# Required for init scripts
Requires: redhat-lsb
%endif


%description master
HMaster is the "master server" for a HBase. There is only one HMaster for a single HBase deployment.

%package regionserver
Summary: The Hadoop HBase RegionServer server.
Group: System/Daemons
Provides: hbase-regionserver
Requires: %{name} = %{version}-%{release}

%if  %{?suse_version:1}0
# Required for init scripts
Requires: insserv
%else
# Required for init scripts
Requires: redhat-lsb
%endif


%description regionserver 
HRegionServer makes a set of HRegions available to clients. It checks in with the HMaster. There are many HRegionServers in a single HBase deployment.

%package thrift
Summary: The Hadoop HBase Thrift Interface
Group: System/Daemons
Provides: hbase-thrift
Requires: %{name} = %{version}-%{release}

%if  %{?suse_version:1}0
# Required for init scripts
Requires: insserv
%else
# Required for init scripts
Requires: redhat-lsb
%endif


%description thrift
ThriftServer - this class starts up a Thrift server which implements the Hbase API specified in the Hbase.thrift IDL file.
"Thrift is a software framework for scalable cross-language services development. It combines a powerful software stack with a code generation engine to build services that work efficiently and seamlessly between C++, Java, Python, PHP, and Ruby. Thrift was developed at Facebook, and we are now releasing it as open source." For additional information, see http://developers.facebook.com/thrift/. Facebook has announced their intent to migrate Thrift into Apache Incubator.

%package doc
Summary: Hbase Documentation
Group: Documentation
BuildArch: noarch
Obsoletes: %{name}-docs

%description doc
Documentation for Hbase


%prep
%setup -n hbase-%{hbase_base_version}

%build
mvn clean
mvn -DskipTests -Dhbase.version=%{version} install assembly:assembly  

%install
%__rm -rf $RPM_BUILD_ROOT
sh $RPM_SOURCE_DIR/install_hbase.sh \
	--build-dir=. \
   --doc-dir=%{doc_hbase} \
	--prefix=$RPM_BUILD_ROOT

%__install -d -m 0755 $RPM_BUILD_ROOT/%{initd_dir}/

%__install -d -m 0755 $RPM_BUILD_ROOT/etc/default/
%__install -m 0644 $RPM_SOURCE_DIR/hbase.default $RPM_BUILD_ROOT/etc/default/hbase

%if  %{?suse_version:1}0
orig_init_file=$RPM_SOURCE_DIR/hadoop-hbase.sh.suse
%else
orig_init_file=$RPM_SOURCE_DIR/hadoop-hbase.sh
%endif

for service in %{hbase_services}
do
	init_file=$RPM_BUILD_ROOT/%{initd_dir}/%{name}-${service}
	%__cp $orig_init_file $init_file
	%__sed -i -e "s|@HBASE_DAEMON@|${service}|" $init_file
	chmod 755 $init_file
done

%__install -d -m 0755 $RPM_BUILD_ROOT/usr/bin

# Pull zookeeper and hadoop from their packages
rm -f $RPM_BUILD_ROOT/usr/lib/hbase/lib/hadoop* \
      $RPM_BUILD_ROOT/usr/lib/hbase/lib/zookeeper*
ln -s /usr/lib/hadoop/hadoop-core.jar $RPM_BUILD_ROOT/usr/lib/hbase/lib/hadoop-core.jar
ln -s /usr/lib/zookeeper/zookeeper.jar $RPM_BUILD_ROOT/usr/lib/hbase/lib/zookeeper.jar

%pre
getent group hbase 2>/dev/null >/dev/null || /usr/sbin/groupadd -r hbase
getent passwd hbase 2>&1 > /dev/null || /usr/sbin/useradd -c "HBase" -s /sbin/nologin -g hbase -r -d /var/run/hbase hbase 2> /dev/null || :

%__install -d -m 0755 -o hbase -g hbase /var/log/hbase
%__install -d -m 0755 -o hbase -g hbase /var/run/hbase

%post
unlink %{logs_hbase} 2> /dev/null
unlink %{pids_hbase} 2> /dev/null

ln -s /var/log/hbase %{logs_hbase}
ln -s /var/run/hbase %{pids_hbase}


#######################
#### FILES SECTION ####
#######################
%files 
%defattr(-,hbase,hbase)
%{_sysconfdir}/default/hbase
%{hbase_home}
%{hbase_home}/hbase-*.jar
%{webapps_hbase}

%defattr(0755,root,root)
/usr/bin/hbase
%config %{etc_hbase}/conf

%files doc
%defattr(-,root,root)
%{doc_hbase}/


%define service_macro() \
%files %1 \
%attr(0755,root,root)/%{initd_dir}/%{name}-%1 \
%post %1 \
chkconfig --add %{name}-%1 \
\
%preun %1 \
if [ "$1" = 0 ] ; then \
	service %{name}-%1 stop > /dev/null \
	chkconfig --del %{name}-%1 \
fi
%service_macro master
%service_macro thrift
%service_macro regionserver
