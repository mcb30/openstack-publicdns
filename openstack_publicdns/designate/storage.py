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

from designate.storage import impl_sqlalchemy as sqla


class PublicDNSStorage(sqla.SQLAlchemyStorage):
    """Public DNS storage

    The upstream SQLAlchemy storage automatically applies a
    `tenant_id` equality filter to almost every operation.  This is in
    addition to and independent of the access control policy.  The net
    effect is that many operations will silently fail if performed
    with the "wrong" tenant selected, even if the user has the
    required permissions.  This tends to break the Neutron DNS
    integration: if an administrator performs an action that modifies
    a port (e.g. creating an instance, deleting an instance, moving an
    instance to a new network, etc) then the DNS update will be
    silently dropped unless the administrator remembered to switch to
    the zone-owning project.

    This extension modifies the storage layer to omit the `tenant_id`
    filtering.  A side effect is that commands such as "openstack zone
    list" will return all zones regardless of tenant.
    """

    def _apply_tenant_criteria(self, context, table, query,
                               include_null_tenant=True):
        # Bypass all tenant filtering
        return query
