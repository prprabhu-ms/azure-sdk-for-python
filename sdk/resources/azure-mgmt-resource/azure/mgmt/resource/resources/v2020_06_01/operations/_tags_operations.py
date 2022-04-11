# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_delete_value_request(
    tag_name: str,
    tag_value: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue}')
    path_format_arguments = {
        "tagName": _SERIALIZER.url("tag_name", tag_name, 'str'),
        "tagValue": _SERIALIZER.url("tag_value", tag_value, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_or_update_value_request(
    tag_name: str,
    tag_value: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue}')
    path_format_arguments = {
        "tagName": _SERIALIZER.url("tag_name", tag_name, 'str'),
        "tagValue": _SERIALIZER.url("tag_value", tag_value, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_or_update_request(
    tag_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/tagNames/{tagName}')
    path_format_arguments = {
        "tagName": _SERIALIZER.url("tag_name", tag_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_request(
    tag_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/tagNames/{tagName}')
    path_format_arguments = {
        "tagName": _SERIALIZER.url("tag_name", tag_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/tagNames')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_or_update_at_scope_request(
    scope: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2020-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/{scope}/providers/Microsoft.Resources/tags/default')
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_update_at_scope_request(
    scope: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2020-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/{scope}/providers/Microsoft.Resources/tags/default')
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_get_at_scope_request(
    scope: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/{scope}/providers/Microsoft.Resources/tags/default')
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_at_scope_request(
    scope: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/{scope}/providers/Microsoft.Resources/tags/default')
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class TagsOperations(object):
    """TagsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.resources.v2020_06_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def delete_value(
        self,
        tag_name: str,
        tag_value: str,
        **kwargs: Any
    ) -> None:
        """Deletes a predefined tag value for a predefined tag name.

        This operation allows deleting a value from the list of predefined values for an existing
        predefined tag name. The value being deleted must not be in use as a tag value for the given
        tag name for any resource.

        :param tag_name: The name of the tag.
        :type tag_name: str
        :param tag_value: The value of the tag to delete.
        :type tag_value: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_value_request(
            tag_name=tag_name,
            tag_value=tag_value,
            subscription_id=self._config.subscription_id,
            template_url=self.delete_value.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_value.metadata = {'url': '/subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue}'}  # type: ignore


    @distributed_trace
    def create_or_update_value(
        self,
        tag_name: str,
        tag_value: str,
        **kwargs: Any
    ) -> "_models.TagValue":
        """Creates a predefined value for a predefined tag name.

        This operation allows adding a value to the list of predefined values for an existing
        predefined tag name. A tag value can have a maximum of 256 characters.

        :param tag_name: The name of the tag.
        :type tag_name: str
        :param tag_value: The value of the tag to create.
        :type tag_value: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TagValue, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2020_06_01.models.TagValue
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TagValue"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_create_or_update_value_request(
            tag_name=tag_name,
            tag_value=tag_value,
            subscription_id=self._config.subscription_id,
            template_url=self.create_or_update_value.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('TagValue', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('TagValue', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update_value.metadata = {'url': '/subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue}'}  # type: ignore


    @distributed_trace
    def create_or_update(
        self,
        tag_name: str,
        **kwargs: Any
    ) -> "_models.TagDetails":
        """Creates a predefined tag name.

        This operation allows adding a name to the list of predefined tag names for the given
        subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag
        names cannot have the following prefixes which are reserved for Azure use: 'microsoft',
        'azure', 'windows'.

        :param tag_name: The name of the tag to create.
        :type tag_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TagDetails, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2020_06_01.models.TagDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TagDetails"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_create_or_update_request(
            tag_name=tag_name,
            subscription_id=self._config.subscription_id,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('TagDetails', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('TagDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/tagNames/{tagName}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        tag_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a predefined tag name.

        This operation allows deleting a name from the list of predefined tag names for the given
        subscription. The name being deleted must not be in use as a tag name for any resource. All
        predefined values for the given name must have already been deleted.

        :param tag_name: The name of the tag.
        :type tag_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            tag_name=tag_name,
            subscription_id=self._config.subscription_id,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/tagNames/{tagName}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        **kwargs: Any
    ) -> Iterable["_models.TagsListResult"]:
        """Gets a summary of tag usage under the subscription.

        This operation performs a union of predefined tags, resource tags, resource group tags and
        subscription tags, and returns a summary of usage for each tag name and value under the given
        subscription. In case of a large number of tags, this operation may return a previously cached
        result.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TagsListResult or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.resource.resources.v2020_06_01.models.TagsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TagsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("TagsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/tagNames'}  # type: ignore

    @distributed_trace
    def create_or_update_at_scope(
        self,
        scope: str,
        parameters: "_models.TagsResource",
        **kwargs: Any
    ) -> "_models.TagsResource":
        """Creates or updates the entire set of tags on a resource or subscription.

        This operation allows adding or replacing the entire set of tags on the specified resource or
        subscription. The specified entity can have a maximum of 50 tags.

        :param scope: The resource scope.
        :type scope: str
        :param parameters:
        :type parameters: ~azure.mgmt.resource.resources.v2020_06_01.models.TagsResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TagsResource, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2020_06_01.models.TagsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TagsResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'TagsResource')

        request = build_create_or_update_at_scope_request(
            scope=scope,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update_at_scope.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TagsResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update_at_scope.metadata = {'url': '/{scope}/providers/Microsoft.Resources/tags/default'}  # type: ignore


    @distributed_trace
    def update_at_scope(
        self,
        scope: str,
        parameters: "_models.TagsPatchResource",
        **kwargs: Any
    ) -> "_models.TagsResource":
        """Selectively updates the set of tags on a resource or subscription.

        This operation allows replacing, merging or selectively deleting tags on the specified resource
        or subscription. The specified entity can have a maximum of 50 tags at the end of the
        operation. The 'replace' option replaces the entire set of existing tags with a new set. The
        'merge' option allows adding tags with new names and updating the values of tags with existing
        names. The 'delete' option allows selectively deleting tags based on given names or name/value
        pairs.

        :param scope: The resource scope.
        :type scope: str
        :param parameters:
        :type parameters: ~azure.mgmt.resource.resources.v2020_06_01.models.TagsPatchResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TagsResource, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2020_06_01.models.TagsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TagsResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'TagsPatchResource')

        request = build_update_at_scope_request(
            scope=scope,
            content_type=content_type,
            json=_json,
            template_url=self.update_at_scope.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TagsResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_at_scope.metadata = {'url': '/{scope}/providers/Microsoft.Resources/tags/default'}  # type: ignore


    @distributed_trace
    def get_at_scope(
        self,
        scope: str,
        **kwargs: Any
    ) -> "_models.TagsResource":
        """Gets the entire set of tags on a resource or subscription.

        Gets the entire set of tags on a resource or subscription.

        :param scope: The resource scope.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TagsResource, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2020_06_01.models.TagsResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TagsResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_at_scope_request(
            scope=scope,
            template_url=self.get_at_scope.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TagsResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_at_scope.metadata = {'url': '/{scope}/providers/Microsoft.Resources/tags/default'}  # type: ignore


    @distributed_trace
    def delete_at_scope(
        self,
        scope: str,
        **kwargs: Any
    ) -> None:
        """Deletes the entire set of tags on a resource or subscription.

        Deletes the entire set of tags on a resource or subscription.

        :param scope: The resource scope.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_at_scope_request(
            scope=scope,
            template_url=self.delete_at_scope.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_at_scope.metadata = {'url': '/{scope}/providers/Microsoft.Resources/tags/default'}  # type: ignore

