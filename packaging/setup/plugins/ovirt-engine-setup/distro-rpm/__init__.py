#
# ovirt-engine-setup -- ovirt engine setup
# Copyright (C) 2013 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


""" ovirt-host-setup distro-rpm plugin.
    Includes code relevant for rpm-based distributions
"""


from otopi import util
from . import packages
from . import image_upload


@util.export
def createPlugins(context):
    packages.Plugin(context=context)
    image_upload.Plugin(context=context)


# vim: expandtab tabstop=4 shiftwidth=4
