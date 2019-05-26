#!/usr/bin/python



from __future__ import (absolute_import, division)
__metaclass__ = type

from ansible.compat.tests import unittest
from ansible.compat.tests.mock import call, create_autospec, patch, mock_open
from ansible.module_utils.basic import AnsibleModule

from ansible.modules.cloud.somebodyscomputer import firstmod



def save_data(mod):
    raise NotImplementedError

def main():
    mod = AnsibleModule(
       argument_spec=dict(
          src=dict(required=True),
          dest=dict(required=False, default="/tmp/firstmod")
          )
      )

    save_data(mod)

if __name__ == '__main__':
    main()

