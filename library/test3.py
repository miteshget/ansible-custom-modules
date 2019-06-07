#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def test3():
    module = AnsibleModule(
      argument_spec=module_args,
      supports_check_mode=True
      )

    module_args = dict( 
      input = dict( type='str', required=True)
      print = dict( type='bool', required=True, default=False)
    )
    result = dict(
       stdout = '',
       changed = False
       )

    if module_args.print == true:
      result.stdout = module_args.input
      result.changed = True
    else:
      result.stdout = "Hello World"
      result.changed = false

    module.exit_json(**result)
  

def main():
  test3()

if __name__ == '__main__':
    main()
