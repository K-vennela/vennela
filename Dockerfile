FROM centos:6

RUN yum -y install rpm-build git tree 

RUN cd /home && \
	git clone https://bitbucket.ops.expertcity.com/scm/dpt/oracle-admin.git && \
	tar czvf oracleadmin.tar.gz oracle-admin && \
	mkdir -p rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS} && \
	mv oracleadmin.tar.gz rpmbuild/SOURCES/

COPY oracleadmin.spec /home/rpmbuild/SPECS/

RUN rpmbuild --define "_topdir /home/rpmbuild/" -ba /home/rpmbuild/SPECS/oracleadmin.spec








