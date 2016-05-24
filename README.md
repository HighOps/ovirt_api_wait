# ovirt_api_wait Ansible role

This role will wait for hosted engine 3.6 api to become active.


##Requirements
Centos 7
Ansible 1.4 and a above

##Role variables
* ovirt_api_wait_engine_user:
Ovirt engine username.

* ovirt_api_wait_engine_password:
Ovrt engine password.

* ovirt_api_wait_engine_fqdn:: 
Ovirt engine password.

* ovirt_api_max_tries:
Max number of retries in seconds.

* ovirt_api_time_out:
Length of time to wait between retries.


## Example Playbook
```yaml
- hosts: ovirt_host
```
  roles:
    - ovirt_api_wait

See defaults for values.
