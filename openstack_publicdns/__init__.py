# Copyright (c) 2019 Unipart Digital
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

from oslo_log import log as logging
from neutron.plugins.ml2.extensions import dns_integration as dns

LOG = logging.getLogger(__name__)


class PublicDNSExtensionDriver(dns.DNSDomainPortsExtensionDriver):

    def _get_request_dns_name_and_domain_name(self, dns_data_db):
        dns_name, dns_domain = (
            super(PublicDNSExtensionDriver,
                  self)._get_request_dns_name_and_domain_name(dns_data_db))
        if dns_data_db:
            if dns_data_db.current_dns_name:
                dns_name = dns_data_db.current_dns_name
                dns_domain = dns_data_db.current_dns_domain
        return dns_name, dns_domain
