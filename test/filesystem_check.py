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
        result['stderr_line'] =  module.params[module_arg] + msg
        module.exit_json(**result)
      if status == "stdout":
        result['stdout_line'] =  module.params[module_arg] + msg
        module.exit_json(**result)
      return

    def mount_device(device, mount_point, filesystem = "", mount_args = ""):
      # Pending with mount commands
      if len(filesystem) == 0 and len(mount_args) == 0:
        #mount device mount_point
        result_output("device", " mount " + device + mount_point + " mounted now", "stdout")
        return
      if len(filesystem) > 0 and len(mount_args) == 0 :
        #mount -t filesystem device mount_point
        result_output("device", " mount -t filesystem " + device + mount_point + " mounted now", "stdout")
        return
      if len(filesystem) == 0 and len(mount_args) > 0 :
        #mount -o mount_args device mount_point
        result_output("device", " mount -o mount_args " + device + mount_point + " mounted now", "stdout")
      return
      if len(filesystem) > 0 and len(mount_args) > 0 :
        #mount -t filesystem -o mount_args device mount_point
        result_output("device", " mount -t filesystem -o mount_args " + device + mount_point + " mounted now", "stdout")
      return

    if os.path.exists(module.params['device']):
      if stat.S_ISBLK(os.stat(module.params['device']).st_mode):
        dump_device = subprocess.Popen(["mount"], stdout=subprocess.PIPE ).communicate()[0]
        if dump_device.split().count(module.params['device']) > 0 :
          result_output("device", " device is already mounted\n")
          return
      else:
        result_output("device", " device is not a valid block device\n")
        return
    else:
      result_output("device", " device does not exist\n")
      return

    if os.path.exists(module.params['mount_point']):
      if os.path.isdir(module.params['mount_point']):
        if not os.path.ismount(module.params['mount_point']):
          mount_device(module.params['device'], module.params['mount_point'])
          #result_output("mount_point", " Successfully mounted ", "stdout")
        else:
          result_output("mount_point", " mount point is already mounted\n")
          return
      else:
        result_output("mount_point", " mount point is not directory\n")
        return
    else:
      result_output("mount_point", " mount point  does not exist\n")
      return 


    module.exit_json(**result)

def main():
  filesystem_check()

if __name__ == '__main__':
    main()
