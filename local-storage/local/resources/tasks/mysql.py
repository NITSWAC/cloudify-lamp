########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from fabric.api import sudo
from cloudify import ctx


def install():
    _set_root_password()
    
    sudo('apt-get -y update')

    ctx.logger.info('Installing package: mysql-server')
    sudo('apt-get -y install mysql-server')
    ctx.logger.info('Successfully installed package: mysql-server')

    ctx.logger.info('Installing package: libapache2-mod-auth-mysql')
    sudo('apt-get -y install libapache2-mod-auth-mysql')
    ctx.logger.info('Successfully installed package: libapache2-mod-auth-mysql')

    ctx.logger.info('Installing package: php5-mysql')
    sudo('apt-get -y install php5-mysql')
    ctx.logger.info('Successfully installed package: php5-mysql')


def start():
    ctx.logger.info('Starting mysql_install_db')
    sudo('mysql_install_db')
    ctx.logger.info('Successfully started mysql service')


def stop():
    ctx.logger.info('Stopping mysql service')
    sudo('service mysqld stop')
    ctx.logger.info('Successfully stopped mysql service')


def uninstall():
    ctx.logger.info('Uninstalling package: mysql-server')
    sudo('apt-get -y remove mysql-server')
    ctx.logger.info('Successfully uninstalled package: mysql-server')


def _set_root_password():
    root_password = ctx.node.properties['root_password']
    ctx.logger.info('Setting mysql root password to {0}'.format(root_password))
    root_password_command = "sudo debconf-set-selections <<< " \
                            "'mysql-server mysql-server/root_password password " \
                            "{0}'".format(root_password)
    root_password_again_command = "sudo debconf-set-selections <<< " \
                                  "'mysql-server mysql-server/root_password_again password " \
                                  "{0}'".format(root_password)

    sudo(root_password_command)
    sudo(root_password_again_command)
