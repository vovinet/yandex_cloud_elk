#!/usr/bin/python

import os.path
import filecmp

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_test:
    name: fail me
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule

def make_tmp_file(tmp_file_path, file_content):
    with open(tmp_file_path,"w+") as f:
        file.write(file_content)
        file.close()

def edit_file(file_path, file_content):

def cleanup(tmp_file_path):
    # Cleanup
    if os.path.is_file(tmp_file_path):
        os.remove(tmp_file_path)

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        file_path=dict(type='str', required=True),
        file_content=dict(type='bool', required=False, default='')
    )

    tmp_file_path = '/tmp/ansible_vovinet_my_own_module.tmp'

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['original_message'] = module.params['file_path']
    result['message'] = 'goodbye'

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['file_content'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # Processing file content

    # If target file not found - put received content to destination path
    if not os.path.is_file(file_path):
        result['changed'] = True
        make_tmp_file(tmp_file_path, file_content)
        if module.check_mode:
            cleanup(tmp_file_path)
            module.exit_json(**result)
        move_file(file_path, file_content)

    # If file already exists - check content equity
    else: 
        make_tmp_file(tmp_file_path, file_content)
        if filecmp.cmp(tmp_file, file_content):
            result['changed'] = True
            if module.check_mode:
                cleanup(tmp_file_path)
                module.exit_json(**result)
            edit_file(file_path, file_content):
    # If file exists with equal content - do nothing
        else:
            cleanup(tmp_file_path)
            result['changed'] = False

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    cleanup(tmp_file_path)
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
