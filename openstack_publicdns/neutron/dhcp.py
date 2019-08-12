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
from neutron.agent.linux import dhcp

LOG = logging.getLogger(__name__)


class Dnsmasq(dhcp.Dnsmasq):
    """Public DNS DHCP agent

    The upstream DHCP agent starts `dnsmasq` with a `--domain` option
    using the `dns_domain` from `neutron.conf` rather than from the
    network's `dns_domain`.

    This extension modifies this behaviour so that the `--domain`
    option uses the network's `dns_domain`.
    """

    def _build_cmdline_callback(self, pid_file):
        cmd = super(Dnsmasq, self)._build_cmdline_callback(pid_file)
        if hasattr(self.network, 'dns_domain') and self.network.dns_domain:
            LOG.debug("Setting dnsmasq domain \"%s\" for network %s",
                      self.network.dns_domain, self.network.id)
            cmd = [x for x in cmd if not x.startswith('--domain=')]
            cmd.append('--domain=%s' % self.network.dns_domain)
        return cmd
