OpenStack public DNS plugins
============================

This package provides a collection of plugins to simplify the use of
public DNS names for OpenStack virtual machine instances.

Each OpenStack network can have a configured `dns_domain`.  Virtual
machine instances launched within that network will have a hostname
constructed from the network's `dns_domain`, and appropriate DNS
records will be created automatically.

For example: if an instance named `testvm` is launched in a network
with the DNS domain `example.org` then the instance will be given the
DHCP hostname `testvm.example.org` and the DNS A and AAAA records for
`testvm.example.org` will be added to the DNS zone.
