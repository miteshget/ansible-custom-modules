#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

import os
import stat
import subprocess
from ansible.module_utils.basic import AnsibleModule




def filesystem():
    module_args = dict( 
      path = dict(type='str', required=True),
      storage =  dict(type='bool', required=False, default=False)
      )

    module = AnsibleModule(
      argument_spec=module_args,
      supports_check_mode=True
      )

    result = dict(
       changed=False,
       stdout = '',
       stdout_line='',
       stderr_line='',
       device=''
       )
    
    if os.path.exists(module.params['path']):
      if os.path.isdir(module.params['path']):
        #######################################################  
        #Calculating disk usages
        dump_du_output = subprocess.Popen(["du", "-chd  1", module.params['path']], stdout=subprocess.PIPE ).communicate()[0]
        for lines in dump_du_output.split("\n"):
          if len(lines) > 0:
            if lines.split()[1] == "total" :
              result['stdout'] = lines.split()
        result['stdout_line'] = dump_du_output
        #######################################################
        # finding directory storage path
        # storage_path = subprocess.Popen(["df", "-P", module.params['path']], stdout=subprocess.PIPE ).communicate()[0]
        # if module.params['storage']:
        #   for device_list in storage_path.split("\n"):
        #     if len(device_list.split()) > 0:
        #       if device_list.split()[0] != "Filesystem":
        #         result['device'] = module.params['path'] + " " + " is reside on " + device_list.split()[0]
        #######################################################  
      else:
        result['stderr_line'] = module.params['path'] + " " + "is not directory"
    else:
      result['stderr_line'] = module.params['path'] + " " + "does not exist"

   
    module.exit_json(**result)
  
def main():
  filesystem()

if __name__ == '__main__':
    main()
