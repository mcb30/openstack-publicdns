OpenStack DNS hostnames
=======================

The OpenStack networking service (Neutron) can be configured to
automatically create DNS records for virtual machine instances.  For
example: if an instance named `testvm` is launched in a network with
the DNS domain `testnet.example.org` then the Neutron service can
automatically create DNS A and AAAA records for
`testvm.testnet.example.org`.

Different networks may have different DNS domains: records will be
created as expected based on the per-network `dns_domain` attribute.
However, the hostname provided to the instance via DHCP will ignore
the per-network `dns_domain` attribute and will instead be constructed
using the global `dns_domain` parameter in the `neutron.conf` file.

This plugin works around this limitation in the Neutron service: it
updates the DHCP configuration so that the hostname provided to the
instance via DHCP will be constructed in the same way as the DNS
record.
