# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class Change(Resource):
    """The detected change.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param properties: The properties of a change.
    :type properties: ~Microsoft.ChangeAnalysis.models.ChangeProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ChangeProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Change, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class ChangeList(msrest.serialization.Model):
    """The list of detected changes.

    :param value: The list of changes.
    :type value: list[~Microsoft.ChangeAnalysis.models.Change]
    :param next_link: The URI that can be used to request the next page of changes.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Change]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChangeList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class ChangeProperties(msrest.serialization.Model):
    """The properties of a change.

    :param resource_id: The resource id that the change is attached to.
    :type resource_id: str
    :param time_stamp: The time when the change is detected.
    :type time_stamp: ~datetime.datetime
    :param initiated_by_list: The list of identities who might initiated the change.
     The identity could be user name (email address) or the object ID of the Service Principal.
    :type initiated_by_list: list[str]
    :param change_type: The type of the change. Possible values include: "Add", "Remove", "Update".
    :type change_type: str or ~Microsoft.ChangeAnalysis.models.ChangeType
    :param property_changes: The list of detailed changes at json property level.
    :type property_changes: list[~Microsoft.ChangeAnalysis.models.PropertyChange]
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'time_stamp': {'key': 'timeStamp', 'type': 'iso-8601'},
        'initiated_by_list': {'key': 'initiatedByList', 'type': '[str]'},
        'change_type': {'key': 'changeType', 'type': 'str'},
        'property_changes': {'key': 'propertyChanges', 'type': '[PropertyChange]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ChangeProperties, self).__init__(**kwargs)
        self.resource_id = kwargs.get('resource_id', None)
        self.time_stamp = kwargs.get('time_stamp', None)
        self.initiated_by_list = kwargs.get('initiated_by_list', None)
        self.change_type = kwargs.get('change_type', None)
        self.property_changes = kwargs.get('property_changes', None)


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(msrest.serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~Microsoft.ChangeAnalysis.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~Microsoft.ChangeAnalysis.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :param error: The error object.
    :type error: ~Microsoft.ChangeAnalysis.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class PropertyChange(msrest.serialization.Model):
    """Data of a property change.

    :param change_type: The type of the change. Possible values include: "Add", "Remove", "Update".
    :type change_type: str or ~Microsoft.ChangeAnalysis.models.ChangeType
    :param change_category: The change category. Possible values include: "User", "System".
    :type change_category: str or ~Microsoft.ChangeAnalysis.models.ChangeCategory
    :param json_path: The json path of the changed property.
    :type json_path: str
    :param display_name: The enhanced display name of the json path. E.g., the json path
     value[0].properties will be translated to something meaningful like
     slots["Staging"].properties.
    :type display_name: str
    :param level:  Possible values include: "Noisy", "Normal", "Important".
    :type level: str or ~Microsoft.ChangeAnalysis.models.Level
    :param description: The description of the changed property.
    :type description: str
    :param old_value: The value of the property before the change.
    :type old_value: str
    :param new_value: The value of the property after the change.
    :type new_value: str
    :param is_data_masked: The boolean indicating whether the oldValue and newValue are masked. The
     values are masked if it contains sensitive information that the user doesn't have access to.
    :type is_data_masked: bool
    """

    _attribute_map = {
        'change_type': {'key': 'changeType', 'type': 'str'},
        'change_category': {'key': 'changeCategory', 'type': 'str'},
        'json_path': {'key': 'jsonPath', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'level': {'key': 'level', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'old_value': {'key': 'oldValue', 'type': 'str'},
        'new_value': {'key': 'newValue', 'type': 'str'},
        'is_data_masked': {'key': 'isDataMasked', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PropertyChange, self).__init__(**kwargs)
        self.change_type = kwargs.get('change_type', None)
        self.change_category = kwargs.get('change_category', None)
        self.json_path = kwargs.get('json_path', None)
        self.display_name = kwargs.get('display_name', None)
        self.level = kwargs.get('level', None)
        self.description = kwargs.get('description', None)
        self.old_value = kwargs.get('old_value', None)
        self.new_value = kwargs.get('new_value', None)
        self.is_data_masked = kwargs.get('is_data_masked', None)


class ProxyResource(Resource):
    """The resource model definition for a Azure Resource Manager proxy resource. It will not have tags and a location.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProxyResource, self).__init__(**kwargs)


class ResourceProviderOperationDefinition(msrest.serialization.Model):
    """The resource provider operation definition.

    :param name: The resource provider operation name.
    :type name: str
    :param display: The resource provider operation details.
    :type display: ~Microsoft.ChangeAnalysis.models.ResourceProviderOperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationDefinition, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """The resource provider operation details.

    :param provider: Name of the resource provider.
    :type provider: str
    :param resource: Name of the resource type.
    :type resource: str
    :param operation: Name of the resource provider operation.
    :type operation: str
    :param description: Description of the resource provider operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class ResourceProviderOperationList(msrest.serialization.Model):
    """The resource provider operation list.

    :param value: Resource provider operations list.
    :type value: list[~Microsoft.ChangeAnalysis.models.ResourceProviderOperationDefinition]
    :param next_link: The URI that can be used to request the next page for list of Azure
     operations.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperationDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)