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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ["preview"],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_ssl_policy
description:
- Represents a SSL policy. SSL policies give you the ability to control the features
  of SSL that your SSL proxy or HTTPS load balancer negotiates.
short_description: Creates a GCP SslPolicy
version_added: '2.7'
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
  description:
    description:
    - An optional description of this resource.
    required: false
    type: str
  name:
    description:
    - Name of the resource. Provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
    type: str
  profile:
    description:
    - Profile specifies the set of SSL features that can be used by the load balancer
      when negotiating SSL with clients. This can be one of `COMPATIBLE`, `MODERN`,
      `RESTRICTED`, or `CUSTOM`. If using `CUSTOM`, the set of SSL features to enable
      must be specified in the `customFeatures` field.
    - 'Some valid choices include: "COMPATIBLE", "MODERN", "RESTRICTED", "CUSTOM"'
    required: false
    type: str
  min_tls_version:
    description:
    - The minimum version of SSL protocol that can be used by the clients to establish
      a connection with the load balancer. This can be one of `TLS_1_0`, `TLS_1_1`,
      `TLS_1_2`.
    - 'Some valid choices include: "TLS_1_0", "TLS_1_1", "TLS_1_2"'
    required: false
    type: str
  custom_features:
    description:
    - A list of features enabled when the selected profile is CUSTOM. The method returns
      the set of features that can be specified in this list. This field must be empty
      if the profile is not CUSTOM.
    required: false
    type: list
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
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/rest/v1/sslPolicies)'
- 'Using SSL Policies: U(https://cloud.google.com/compute/docs/load-balancing/ssl-policies)'
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a SSL policy
  google.cloud.gcp_compute_ssl_policy:
    name: test_object
    profile: CUSTOM
    min_tls_version: TLS_1_2
    custom_features:
    - TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
    - TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource.
  returned: success
  type: str
id:
  description:
  - The unique identifier for the resource.
  returned: success
  type: int
name:
  description:
  - Name of the resource. Provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
profile:
  description:
  - Profile specifies the set of SSL features that can be used by the load balancer
    when negotiating SSL with clients. This can be one of `COMPATIBLE`, `MODERN`,
    `RESTRICTED`, or `CUSTOM`. If using `CUSTOM`, the set of SSL features to enable
    must be specified in the `customFeatures` field.
  returned: success
  type: str
minTlsVersion:
  description:
  - The minimum version of SSL protocol that can be used by the clients to establish
    a connection with the load balancer. This can be one of `TLS_1_0`, `TLS_1_1`,
    `TLS_1_2`.
  returned: success
  type: str
enabledFeatures:
  description:
  - The list of features enabled in the SSL policy.
  returned: success
  type: list
customFeatures:
  description:
  - A list of features enabled when the selected profile is CUSTOM. The method returns
    the set of features that can be specified in this list. This field must be empty
    if the profile is not CUSTOM.
  returned: success
  type: list
fingerprint:
  description:
  - Fingerprint of this resource. A hash of the contents stored in this object. This
    field is used in optimistic locking.
  returned: success
  type: str
warnings:
  description:
  - If potential misconfigurations are detected for this SSL policy, this field will
    be populated with warning messages.
  returned: success
  type: complex
  contains:
    code:
      description:
      - A warning code, if applicable.
      returned: success
      type: str
    message:
      description:
      - A human-readable description of the warning code.
      returned: success
      type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(state=dict(default='present', choices=['present', 'absent'], type='str'), description=dict(type='str'), name=dict(required=True, type='str'), profile=dict(type='str'), min_tls_version=dict(type='str'), custom_features=dict(type='list', elements='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#sslPolicy'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.patch(link, resource_to_request(module)))


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = { u'kind': 'compute#sslPolicy',u'description': module.params.get('description'),u'name': module.params.get('name'),u'profile': module.params.get('profile'),u'minTlsVersion': module.params.get('min_tls_version'),u'customFeatures': module.params.get('custom_features') }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/sslPolicies/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/sslPolicies".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
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
    return { u'creationTimestamp': response.get(u'creationTimestamp'),u'description': module.params.get('description'),u'id': response.get(u'id'),u'name': module.params.get('name'),u'profile': response.get(u'profile'),u'minTlsVersion': response.get(u'minTlsVersion'),u'enabledFeatures': response.get(u'enabledFeatures'),u'customFeatures': response.get(u'customFeatures'),u'fingerprint': response.get(u'fingerprint'),u'warnings': SslPolicyWarningsArray(response.get(u'warnings', []), module).from_response() }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/global/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#sslPolicy')

def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class SslPolicyWarningsArray(object):
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
        return remove_nones_from_dict({  }
)

    def _response_from_item(self, item):
        return remove_nones_from_dict({  }
)


if __name__ == '__main__':
    main()
