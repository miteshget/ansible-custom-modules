#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def test3():

    module_args = dict( 
      input = dict( type='str', required=True),
      print1 = dict( type='bool', required=True)
    )

    module = AnsibleModule(
      argument_spec=module_args,
      supports_check_mode=True
      )
    result = dict(
       stdout_line = '',
       changed = False
       )

    if module.params['print1'] == True:
      result['stdout_line'] = module.params['input']
      result['changed'] = True
    else:
      result['stdout_line'] = "Hello World"
      result['changed'] = False
    module.exit_json(**result)
  

def main():
  test3()

if __name__ == '__main__':
    main()
