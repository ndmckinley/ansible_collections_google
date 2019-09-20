#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_tpu_node
description:
- A Cloud TPU instance.
short_description: Creates a GCP Node
version_added: '2.9'
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  name:
    description:
    - The immutable name of the TPU.
    required: true
    type: str
  description:
    description:
    - The user-supplied description of the TPU. Maximum of 512 characters.
    required: false
    type: str
  accelerator_type:
    description:
    - The type of hardware accelerators associated with this node.
    required: true
    type: str
  tensorflow_version:
    description:
    - The version of Tensorflow running in the Node.
    required: true
    type: str
  network:
    description:
    - The name of a network to peer the TPU node to. It must be a preexisting Compute
      Engine network inside of the project on which this API has been activated. If
      none is provided, "default" will be used.
    required: false
    type: str
  cidr_block:
    description:
    - The CIDR block that the TPU node will use when selecting an IP address. This
      CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller
      block, and using a larger block would be wasteful (a node can only consume one
      IP address).
    - Errors will occur if the CIDR block has already been used for a currently existing
      TPU node, the CIDR block conflicts with any subnetworks in the user's provided
      network, or the provided network is peered with another network that is using
      that CIDR block.
    required: true
    type: str
  scheduling_config:
    description:
    - Sets the scheduling options for this TPU instance.
    required: false
    type: dict
    suboptions:
      preemptible:
        description:
        - Defines whether the TPU instance is preemptible.
        required: false
        default: 'false'
        type: bool
  labels:
    description:
    - Resource labels to represent user provided metadata.
    required: false
    type: dict
  zone:
    description:
    - The GCP location for the TPU.
    required: true
    type: str
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/tpu/docs/reference/rest/)'
- 'Official Documentation: U(https://cloud.google.com/tpu/docs/)'
- for authentication, you can set service_account_file using the c(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the c(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a node
  gcp_tpu_node:
    name: test_object
    zone: us-central1-b
    accelerator_type: v3-8
    tensorflow_version: '1.11'
    cidr_block: 10.2.0.0/29
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - The immutable name of the TPU.
  returned: success
  type: str
description:
  description:
  - The user-supplied description of the TPU. Maximum of 512 characters.
  returned: success
  type: str
acceleratorType:
  description:
  - The type of hardware accelerators associated with this node.
  returned: success
  type: str
tensorflowVersion:
  description:
  - The version of Tensorflow running in the Node.
  returned: success
  type: str
network:
  description:
  - The name of a network to peer the TPU node to. It must be a preexisting Compute
    Engine network inside of the project on which this API has been activated. If
    none is provided, "default" will be used.
  returned: success
  type: str
cidrBlock:
  description:
  - The CIDR block that the TPU node will use when selecting an IP address. This CIDR
    block must be a /29 block; the Compute Engine networks API forbids a smaller block,
    and using a larger block would be wasteful (a node can only consume one IP address).
  - Errors will occur if the CIDR block has already been used for a currently existing
    TPU node, the CIDR block conflicts with any subnetworks in the user's provided
    network, or the provided network is peered with another network that is using
    that CIDR block.
  returned: success
  type: str
serviceAccount:
  description:
  - The service account used to run the tensor flow services within the node. To share
    resources, including Google Cloud Storage data, with the Tensorflow job running
    in the Node, this account must have permissions to that data.
  returned: success
  type: str
schedulingConfig:
  description:
  - Sets the scheduling options for this TPU instance.
  returned: success
  type: complex
  contains:
    preemptible:
      description:
      - Defines whether the TPU instance is preemptible.
      returned: success
      type: bool
networkEndpoints:
  description:
  - The network endpoints where TPU workers can be accessed and sent work.
  - It is recommended that Tensorflow clients of the node first reach out to the first
    (index 0) entry.
  returned: success
  type: complex
  contains:
    ipAddress:
      description:
      - The IP address of this network endpoint.
      returned: success
      type: str
    port:
      description:
      - The port of this network endpoint.
      returned: success
      type: int
labels:
  description:
  - Resource labels to represent user provided metadata.
  returned: success
  type: dict
zone:
  description:
  - The GCP location for the TPU.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import (
    navigate_hash,
    GcpSession,
    GcpModule,
    GcpRequest,
    remove_nones_from_dict,
    replace_resource_dict,
)
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            description=dict(type='str'),
            accelerator_type=dict(required=True, type='str'),
            tensorflow_version=dict(required=True, type='str'),
            network=dict(type='str'),
            cidr_block=dict(required=True, type='str'),
            scheduling_config=dict(type='dict', options=dict(preemptible=dict(type='bool'))),
            labels=dict(type='dict'),
            zone=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), fetch)
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, create_link(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'tpu')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, fetch):
    update_fields(module, resource_to_request(module), response_to_hash(module, fetch))
    return fetch_resource(module, self_link(module))


def update_fields(module, request, response):
    if response.get('tensorflowVersion') != request.get('tensorflowVersion'):
        tensorflow_version_update(module, request, response)


def tensorflow_version_update(module, request, response):
    auth = GcpSession(module, 'tpu')
    auth.post(
        ''.join(["https://tpu.googleapis.com/v1/", "projects/{project}/locations/{zone}/nodes/{name}:reimage"]).format(**module.params),
        {u'tensorflowVersion': module.params.get('tensorflow_version')},
    )


def delete(module, link):
    auth = GcpSession(module, 'tpu')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'acceleratorType': module.params.get('accelerator_type'),
        u'tensorflowVersion': module.params.get('tensorflow_version'),
        u'network': module.params.get('network'),
        u'cidrBlock': module.params.get('cidr_block'),
        u'schedulingConfig': NodeSchedulingconfig(module.params.get('scheduling_config', {}), module).to_request(),
        u'labels': module.params.get('labels'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'tpu')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://tpu.googleapis.com/v1/projects/{project}/locations/{zone}/nodes/{name}".format(**module.params)


def collection(module):
    return "https://tpu.googleapis.com/v1/projects/{project}/locations/{zone}/nodes".format(**module.params)


def create_link(module):
    return "https://tpu.googleapis.com/v1/projects/{project}/locations/{zone}/nodes?nodeId={name}".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'acceleratorType': module.params.get('accelerator_type'),
        u'tensorflowVersion': response.get(u'tensorflowVersion'),
        u'network': module.params.get('network'),
        u'cidrBlock': module.params.get('cidr_block'),
        u'serviceAccount': response.get(u'serviceAccount'),
        u'schedulingConfig': NodeSchedulingconfig(module.params.get('scheduling_config', {}), module).to_request(),
        u'networkEndpoints': NodeNetworkendpointsArray(response.get(u'networkEndpoints', []), module).from_response(),
        u'labels': module.params.get('labels'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://tpu.googleapis.com/v1/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response)
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['done'])
    wait_done = wait_for_completion(status, op_result, module)
    raise_if_errors(wait_done, ['error'], module)
    return navigate_hash(wait_done, ['response'])


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while not status:
        raise_if_errors(op_result, ['error'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, False)
        status = navigate_hash(op_result, ['done'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class NodeSchedulingconfig(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'preemptible': self.request.get('preemptible')})

    def from_response(self):
        return remove_nones_from_dict({u'preemptible': self.request.get(u'preemptible')})


class NodeNetworkendpointsArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({})

    def _response_from_item(self, item):
        return remove_nones_from_dict({})


if __name__ == '__main__':
    main()
