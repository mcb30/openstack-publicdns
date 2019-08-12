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

from neutron.plugins.ml2.extensions import dns_integration as dns


class PublicDNSExtensionDriver(dns.DNSDomainPortsExtensionDriver):
    """Public DNS extension driver

    The upstream DNS extension driver constructs the DNS record names
    (stored in the `portdnses` table) based on the network's
    `dns_domain`, but does not propagate this information to the
    port's own `dns_assignments`.  The upshot of this is that DNS
    records are created as expected using the network's `dns_domain`,
    but the DHCP hostsfile records are created using the `dns_domain`
    from `neutron.conf` rather than the network's `dns_domain`.

    This extension modifies this behaviour so that the port's
    `dns_assignments` are also constructed using the network's
    `dns_domain`.
    """

    def _get_request_dns_name_and_domain_name(self, dns_data_db):
        dns_name, dns_domain = (
            super(PublicDNSExtensionDriver,
                  self)._get_request_dns_name_and_domain_name(dns_data_db))
        if dns_data_db:
            if dns_data_db.current_dns_name:
                dns_name = dns_data_db.current_dns_name
                dns_domain = dns_data_db.current_dns_domain
        return dns_name, dns_domain

    def external_dns_not_needed(self, context, network):
        # Bypass the usual checks and assume that all networks may
        # require external DNS updates
        return False
