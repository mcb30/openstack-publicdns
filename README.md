OpenStack public DNS plugins
============================

This package provides a collection of plugins to simplify the use of
public DNS names for OpenStack virtual machine instances.

Each OpenStack network can have a configured `dns_domain`.  Virtual
machine instances launched within that network will have a hostname
constructed from the network's `dns_domain` and appropriate DNS
records will be created automatically.

For example: if an instance named `testvm` is launched in a network
with the DNS domain `example.org` then the instance will be given the
DHCP hostname `testvm.example.org` and the DNS A and AAAA records for
`testvm.example.org` will be added to the DNS zone.

Installation
------------

The easiest approach is to install the prebuilt RPM from the [COPR
repository](https://copr.fedorainfracloud.org/coprs/unipartdigital/pkgs/).

Configuration
-------------

In `/etc/neutron/plugin.ini` in the `[ml2]` section, change the
`extension_drivers` list to include `publicdns` instead of
`dns_domain_ports` (or `dns`).  For example:

```ini
[ml2]
extension_drivers = port_security,publicdns
```

In `/etc/neutron/dhcp_agent.ini` in the `[DEFAULT]` section, change
`dhcp_driver` from `neutron.agent.linux.dhcp.Dnsmasq` to
`openstack_publicdns.neutron.dhcp.Dnsmasq`.  For example:

```ini
[DEFAULT]
dhcp_driver = openstack_publicdns.neutron.dhcp.Dnsmasq
```

In `/etc/designate/designate.conf`, in the `[service:central]`
section, change `storage_driver` from `sqlalchemy` to `publicdns`.
For example:

```ini
[service:central]
storage_driver = publicdns
```
