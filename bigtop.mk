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

BIGTOP_VERSION=0.1.0-incubating

# Hadoop 0.20.0-based hadoop package
HADOOP_NAME=hadoop
HADOOP_RELNOTES_NAME=Apache Hadoop
HADOOP_BASE_VERSION=0.20.2
HADOOP_PKG_VERSION=0.20.2
HADOOP_RELEASE_VERSION=1
HADOOP_TARBALL_DST=$(HADOOP_NAME)-$(HADOOP_BASE_VERSION).tar.gz
HADOOP_TARBALL_SRC=$(HADOOP_TARBALL_DST)
HADOOP_SITE=$(APACHE_MIRROR)/hadoop/common/$(HADOOP_NAME)-$(HADOOP_BASE_VERSION)/
$(eval $(call PACKAGE,hadoop,HADOOP))

# ZooKeeper
ZOOKEEPER_NAME=zookeeper
ZOOKEEPER_RELNOTES_NAME=Apache Zookeeper
ZOOKEEPER_PKG_NAME=hadoop-zookeeper
ZOOKEEPER_BASE_VERSION=3.3.3
ZOOKEEPER_PKG_VERSION=3.3.3
ZOOKEEPER_RELEASE_VERSION=1
ZOOKEEPER_TARBALL_DST=zookeeper-$(ZOOKEEPER_BASE_VERSION).tar.gz
ZOOKEEPER_TARBALL_SRC=$(ZOOKEEPER_TARBALL_DST)
ZOOKEEPER_PACKAGE_GIT_REPO=$(REPO_DIR)/cdh3/zookeeper-package
ZOOKEEPER_SITE=$(APACHE_MIRROR)/zookeeper/zookeeper-3.3.3/
$(eval $(call PACKAGE,zookeeper,ZOOKEEPER))

# HBase
HBASE_NAME=hbase
HBASE_RELNOTES_NAME=Apache HBase
HBASE_PKG_NAME=hadoop-hbase
HBASE_BASE_VERSION=0.90.3
HBASE_PKG_VERSION=$(HBASE_BASE_VERSION)
HBASE_RELEASE_VERSION=1
HBASE_TARBALL_DST=hbase-$(HBASE_BASE_VERSION).tar.gz
HBASE_TARBALL_SRC=$(HBASE_TARBALL_DST)
HBASE_SITE=$(APACHE_MIRROR)/hbase/hbase-0.90.3/
$(eval $(call PACKAGE,hbase,HBASE))

# Pig
PIG_BASE_VERSION=0.9.0
PIG_PKG_VERSION=$(PIG_BASE_VERSION)
PIG_RELEASE_VERSION=1
PIG_NAME=pig
PIG_RELNOTES_NAME=Apache Pig
PIG_PKG_NAME=hadoop-pig
PIG_TARBALL_DST=pig-$(PIG_BASE_VERSION).tar.gz
PIG_TARBALL_SRC=$(PIG_TARBALL_DST)
PIG_SITE=$(APACHE_MIRROR)/pig/pig-$(PIG_BASE_VERSION)/
$(eval $(call PACKAGE,pig,PIG))

# Hive
HIVE_NAME=hive
HIVE_RELNOTES_NAME=Apache Hive
HIVE_PKG_NAME=hadoop-hive
HIVE_BASE_VERSION=0.7.0
HIVE_PKG_VERSION=$(HIVE_BASE_VERSION)
HIVE_RELEASE_VERSION=1
HIVE_TARBALL_DST=hive-$(HIVE_BASE_VERSION).tar.gz
HIVE_TARBALL_SRC=$(HIVE_TARBALL_DST)
HIVE_SITE=$(APACHE_MIRROR)/hive/hive-$(HIVE_BASE_VERSION)/
$(eval $(call PACKAGE,hive,HIVE))

# Sqoop
SQOOP_NAME=sqoop
SQOOP_RELNOTES_NAME=Sqoop
SQOOP_PKG_NAME=sqoop
SQOOP_BASE_VERSION=1.2.0
SQOOP_PKG_VERSION=1.2.0
SQOOP_RELEASE_VERSION=1
SQOOP_TARBALL_DST=sqoop-$(SQOOP_BASE_VERSION).tar.gz
SQOOP_TARBALL_SRC=$(SQOOP_TARBALL_DST)
SQOOP_SITE=http://github.com/downloads/cloudera/sqoop/
$(eval $(call PACKAGE,sqoop,SQOOP))

# Oozie
OOZIE_NAME=oozie
OOZIE_RELNOTES_NAME=Apache Oozie
OOZIE_PKG_NAME=oozie
OOZIE_BASE_VERSION=2.3.1
OOZIE_PKG_VERSION=2.3.1
OOZIE_RELEASE_VERSION=1
OOZIE_TARBALL_DST=oozie-2.3.1.tar.gz
OOZIE_TARBALL_SRC=2.3.1
OOZIE_PACKAGE_GIT_REPO=$(REPO_DIR)/cdh3/oozie-package
OOZIE_SITE=http://github.com/yahoo/oozie/tarball
$(eval $(call PACKAGE,oozie,OOZIE))

# Whirr
WHIRR_NAME=whirr
WHIRR_RELNOTES_NAME=Apache Whirr
WHIRR_PKG_NAME=whirr
WHIRR_BASE_VERSION=0.5.0
WHIRR_PKG_VERSION=0.5.0
WHIRR_RELEASE_VERSION=1
WHIRR_TARBALL_DST=whirr-$(WHIRR_BASE_VERSION)-incubating-src.tar.gz
WHIRR_TARBALL_SRC=$(WHIRR_TARBALL_DST)
WHIRR_SITE=$(APACHE_MIRROR)//incubator/whirr/whirr-0.5.0-incubating/
$(eval $(call PACKAGE,whirr,WHIRR))

# Flume
FLUME_NAME=flume
FLUME_RELNOTES_NAME=Flume
FLUME_PKG_NAME=flume
FLUME_BASE_VERSION=0.9.3
FLUME_PKG_VERSION=0.9.3
FLUME_RELEASE_VERSION=1
FLUME_TARBALL_DST=flume-$(FLUME_BASE_VERSION).tar.gz
FLUME_TARBALL_SRC=$(FLUME_TARBALL_DST)
FLUME_SITE=http://github.com/downloads/cloudera/flume/
$(eval $(call PACKAGE,flume,FLUME))
