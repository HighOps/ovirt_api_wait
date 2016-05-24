#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Rob Cousins - @highops <rob@highops1.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible. If not, see <http://www.gnu.org/licenses/>.

from ansible.module_utils.basic import *
from time import sleep

try:
    from ovirtsdk.api import API
    from ovirtsdk.xml import params
except ImportError:
    module.fail_json(msg='ovirtsdk required for this module')



#---- Documentation Start ----------------------------------------------------#
DOCUMENTATION = '''
---

module: ovirt_api_wait
author: Rob Cousins - @highops
short_description: 
description:
  - This module waits for ovirt api to become active.
version_added: "1.0"
options:
  username:
    description:
      Username for ovirt api.
    default: null
    required: true
    aliases: []
  password:
    description:
      Password for ovirt api.
    default: null
    required: true
    aliases: []      
  url:
    description:
      Url for ovirt api.
    default: null
    required: true
    aliases: [] 
  max_tries:
    description:
      Max number of retries in seconds. 
    default: 300
    required: false
    aliases: [] 
  time_out:
    description:
      Length of time to wait between retries.
    default: 5
    required: false
    aliases: [] 
           
  requirements:
    - "python >= 2.6"
    - "ovirt-engine-sdk-python"
'''

EXAMPLES = '''
- name: wait for api
  ovirt_waitfor: username=admin 
                 password=somepassword
                 url=https://engine.example.com
                 max_tries=300
                 time_out=5
                 
'''


#---- Logic Start ------------------------------------------------------------#


def waitfor_api(module):
    
    username = module.params['username']
    password = module.params['password']
    url = module.params['url']
    max_tries = module.params['max_tries']
    time_out = module.params['time_out']
    
    while max_tries>0:
        try:
            api = API(url=url,username=username,password=password,insecure=True,timeout=0)
            module.exit_json(changed=False)
        except Exception as ex:
            sleep(time_out)
            max_tries -= 1
    
    module.fail_json(msg='ovirt api timed out')
  
def main():

    # Note: 'AnsibleModule' is an Ansible utility imported below
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True,type='str'),
            username=dict(required=True,type='str'),
            password=dict(required=True,type='str'),
            max_tries=dict(required=False,type='int',default=300),
            time_out=dict(required=False,type='int',default=5)
        ),
        supports_check_mode=False
    )
    waitfor_api(module)
        

#---- Import Ansible Utilities (Ansible Framework) ---------------------------#

main()
