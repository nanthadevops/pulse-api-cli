#
# Copyright 2015 BMC Software, Inc.
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
from boundary import ApiCli


class HostgroupSearch(ApiCli):
    def __init__(self):
        ApiCli.__init__(self)
        self.method = "GET"
        self.path = "v1/hostgroups/search"
        self.hostGroupName = ""

    def add_arguments(self):
        ApiCli.add_arguments(self)
        self.parser.add_argument('-n', '--host-group-name', dest='hostGroupName', metavar="host_group_name",
                                 action='store', required=True,help='Host group name')

    def get_arguments(self):
        """
        Extracts the specific arguments of this CLI
        """
        ApiCli.get_arguments(self)
        if self.args.hostGroupName is not None:
            self.url_parameters = {"name": self.args.hostGroupName}

    def get_description(self):
        return 'Searches for Host Group by name in an {0} account'.format(self.product_name)
