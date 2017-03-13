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

from fabric.api import sudo, put
from cloudify import ctx
import os


def install():

    sudo('apt-get -y update')

    ctx.logger.info('Installing package: apache2')
    sudo('sudo apt-get -y install apache2')
    ctx.logger.info('Successfully installed package: apache2')


def start():
    ctx.logger.info('Starting apache2 service')
    sudo('service apache2 start')
    ctx.logger.info('Successfully started apache2 service')


def stop():
    ctx.logger.info('Stopping apache2 service')
    sudo('service apache2 stop')
    ctx.logger.info('Successfully stopped apache2 service')


def configure_php():
    sudo('apt-get -y install php5 libapache2-mod-php5 php5-mcrypt')
    execution_id_dir = '/tmp/{0}'.format(ctx.execution_id)
    info_php = '{0}/info.php'.format(execution_id_dir)
    os.mkdir(execution_id_dir)
    ctx.download_resource(resource_path='resources/info.php',
                          target_path=info_php)
    put(info_php, '/var/www/info.php', use_sudo=True)


def uninstall():
    ctx.logger.info('Uninstalling package: apache2')
    sudo('apt-get -y remove apache2')
    ctx.logger.info('Successfully uninstalled package: apache2')


