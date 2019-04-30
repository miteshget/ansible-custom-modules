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

def mount_device():
  return


def filesystem_check():
    module_args = dict( 
      device = dict(type='str', required=True),  
      mount_point = dict(type='str', required=True ),
      mount_args = dict(type='str', required=False),
      filesystem = dict(type='str', required=False)
      )

    module = AnsibleModule(
      argument_spec=module_args,
      supports_check_mode=True
      )

    result = dict(
       changed=False,
       stdout_line='',
       stderr_line=''
       )

    def result_output(module_arg, msg, status = "stderr"):
      if status == "stderr":
        result['stderr_line'] =   msg
        module.exit_json(**result)
      if status == "stdout":
        result['stderr_line'] =  module.params[module_arg] + msg
        module.exit_json(**result)
      return

    if os.path.exists(module.params['device']):
      if stat.S_ISBLK(os.stat(module.params['device']).st_mode):
        dump_device = subprocess.Popen(["mount"], stdout=subprocess.PIPE ).communicate()[0]
        if dump_device.split().count(module.params['device']) > 0 :
          result_output("device", "is already mounted\n")
          #result['stderr_line'] = "Device " + module.params['device'] + " is already mounted\n"
          #module.exit_json(**result)
          return
      else:
        result['stderr_line'] = "Device " + module.params['device'] + " is not a valid block device\n"
        module.exit_json(**result)
        return
    else:
      result_output("device", "does not exist\n")
      #result['stderr_line'] = "Device " + module.params['device'] + " does not exist\n"
      #module.exit_json(**result)
      return

    if os.path.exists(module.params['mount_point']):
      if os.path.isdir(module.params['mount_point']):
        if not os.path.ismount(module.params['mount_point']):
          result['stdout_line'] = "Successfully " + module.params['device'] + " mounted on" + module.params['mount_point']
          # need to write mount commands
        else:
          result['stderr_line'] = "Directory " + module.params['mount_point'] + " is already mounted\n"
          module.exit_json(**result)
          return
      else:
        result['stderr_line'] =  module.params['mount_point'] + " is not directory\n"
        module.exit_json(**result)
        return
    else:
      result['stderr_line'] = "Directory " + module.params['mount_point'] + " does not exist\n"
      module.exit_json(**result)
      return 


    module.exit_json(**result)

def main():
  filesystem_check()

if __name__ == '__main__':
    main()