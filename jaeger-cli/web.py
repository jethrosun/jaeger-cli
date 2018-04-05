# Copyright 2018 MassOpenCloud.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import six
import webob.dec

from osprofiler import _utils as utils
from osprofiler import profiler


# Trace keys that are required or optional, any other
# keys that are present will cause the trace to be rejected...
_REQUIRED_KEYS = ("base_id", "hmac_key")
_OPTIONAL_KEYS = ("parent_id",)

#: Http header that will contain the needed traces data.
X_TRACE_INFO = "X-Trace-Info"

#: Http header that will contain the traces data hmac (that will be validated).
X_TRACE_HMAC = "X-Trace-HMAC"


def get_trace_id_headers():
    pass

_ENABLED = None
_HMAC_KEYS = None


def disable():
    pass
    
def enable(hmac_keys=None):
    pass
    
class WsgiMiddleware(object):

    pass
