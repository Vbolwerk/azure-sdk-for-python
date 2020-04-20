# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.netapp.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class NetAppAccountPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetAppAccount <azure.mgmt.netapp.models.NetAppAccount>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetAppAccount]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetAppAccountPaged, self).__init__(*args, **kwargs)
class CapacityPoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CapacityPool <azure.mgmt.netapp.models.CapacityPool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CapacityPool]'}
    }

    def __init__(self, *args, **kwargs):

        super(CapacityPoolPaged, self).__init__(*args, **kwargs)
class VolumePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Volume <azure.mgmt.netapp.models.Volume>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Volume]'}
    }

    def __init__(self, *args, **kwargs):

        super(VolumePaged, self).__init__(*args, **kwargs)
class SnapshotPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Snapshot <azure.mgmt.netapp.models.Snapshot>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Snapshot]'}
    }

    def __init__(self, *args, **kwargs):

        super(SnapshotPaged, self).__init__(*args, **kwargs)