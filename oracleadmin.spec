###############################################################################
# Spec file for Utils
################################################################################
#
Summary: For testing Oracle admin RPM
Name: oracleadmin
Version:2.3
Release: 1%{?dist}
License: DBA
URL: https://bitbucket.ops.expertcity.com/scm/dpt/oracle-admin.git
BuildRoot:  %{_tmppath}/%{name}-%{version}-root
BuildArch:      noarch
Source0 : oracleadmin.tar.gz
# Build with the following syntax:
# rpmbuild --target noarch -bb utils.spec

%description
For testing Oracle admin RPM
%prep
################################################################################
# Create the build tree and copy the files from the oracle-admin directories   #
# into the build tree.                                                         #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"

mkdir -p $RPM_BUILD_ROOT/home/oracle/
mkdir -p $RPM_BUILD_ROOT/home/oracle/admin

cp -R /home/oracle-admin/* $RPM_BUILD_ROOT/home/oracle/admin/


exit

%files
%defattr(-, oracle, oinstall)
/home/oracle/admin/*

%pre
if [ -d "/home/oracle/admin" ]; then
 mv /home/oracle/admin /home/oracle/admin-old
fi

%post
chown -R oracle:oinstall /home/oracle/admin

%clean
rm -rf $RPM_BUILD_ROOT/home/oracle/admin

%changelog
* Wed Sep 02 2020 vennela <vennela.k@logmein.com>
  - remove one file and tested file to check replace and deletion
* Wed Sep 02 2020 vennela <vennela.k@logmein.com>
  - Added helloworld file to check replace
* Tue Sep 01 2020 vennela <vennela.k@logmein.com>
  - For testing Oracle admin RPM
