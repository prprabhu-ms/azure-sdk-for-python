# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class Access(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the traffic is allowed or denied.
    """

    ALLOW = "Allow"
    DENY = "Deny"

class ApplicationGatewayBackendHealthServerHealth(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Health of backend server. Possible values are: 'Unknown', 'Up', 'Down', and 'Partial'.
    """

    UNKNOWN = "Unknown"
    UP = "Up"
    DOWN = "Down"
    PARTIAL = "Partial"

class ApplicationGatewayCookieBasedAffinity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Cookie based affinity. Possible values are: 'Enabled' and 'Disabled'.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ApplicationGatewayFirewallMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Web application firewall mode. Possible values are: 'Detection' and 'Prevention'.
    """

    DETECTION = "Detection"
    PREVENTION = "Prevention"

class ApplicationGatewayOperationalState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operational state of the application gateway resource. Possible values are: 'Stopped',
    'Started', 'Running', and 'Stopping'.
    """

    STOPPED = "Stopped"
    STARTING = "Starting"
    RUNNING = "Running"
    STOPPING = "Stopping"

class ApplicationGatewayProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Protocol. Possible values are: 'Http' and 'Https'.
    """

    HTTP = "Http"
    HTTPS = "Https"

class ApplicationGatewayRequestRoutingRuleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Rule type. Possible values are: 'Basic' and 'PathBasedRouting'.
    """

    BASIC = "Basic"
    PATH_BASED_ROUTING = "PathBasedRouting"

class ApplicationGatewaySkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of an application gateway SKU. Possible values are: 'Standard_Small', 'Standard_Medium',
    'Standard_Large', 'WAF_Medium', and 'WAF_Large'.
    """

    STANDARD_SMALL = "Standard_Small"
    STANDARD_MEDIUM = "Standard_Medium"
    STANDARD_LARGE = "Standard_Large"
    WAF_MEDIUM = "WAF_Medium"
    WAF_LARGE = "WAF_Large"

class ApplicationGatewaySslProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    TL_SV1_0 = "TLSv1_0"
    TL_SV1_1 = "TLSv1_1"
    TL_SV1_2 = "TLSv1_2"

class ApplicationGatewayTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tier of an application gateway. Possible values are: 'Standard' and 'WAF'.
    """

    STANDARD = "Standard"
    WAF = "WAF"

class AssociationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The association type of the child resource to the parent resource.
    """

    ASSOCIATED = "Associated"
    CONTAINS = "Contains"

class AuthorizationUseStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AuthorizationUseStatus. Possible values are: 'Available' and 'InUse'.
    """

    AVAILABLE = "Available"
    IN_USE = "InUse"

class BgpPeerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The BGP peer state
    """

    UNKNOWN = "Unknown"
    STOPPED = "Stopped"
    IDLE = "Idle"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"

class Direction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The direction of the packet represented as a 5-tuple.
    """

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"

class EffectiveRouteSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Who created the route. Possible values are: 'Unknown', 'User', 'VirtualNetworkGateway', and
    'Default'.
    """

    UNKNOWN = "Unknown"
    USER = "User"
    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    DEFAULT = "Default"

class EffectiveRouteState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The value of effective route. Possible values are: 'Active' and 'Invalid'.
    """

    ACTIVE = "Active"
    INVALID = "Invalid"

class ExpressRouteCircuitPeeringAdvertisedPublicPrefixState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AdvertisedPublicPrefixState of the Peering resource. Possible values are 'NotConfigured',
    'Configuring', 'Configured', and 'ValidationNeeded'.
    """

    NOT_CONFIGURED = "NotConfigured"
    CONFIGURING = "Configuring"
    CONFIGURED = "Configured"
    VALIDATION_NEEDED = "ValidationNeeded"

class ExpressRouteCircuitPeeringState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of peering. Possible values are: 'Disabled' and 'Enabled'
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"

class ExpressRouteCircuitPeeringType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The PeeringType. Possible values are: 'AzurePublicPeering', 'AzurePrivatePeering', and
    'MicrosoftPeering'.
    """

    AZURE_PUBLIC_PEERING = "AzurePublicPeering"
    AZURE_PRIVATE_PEERING = "AzurePrivatePeering"
    MICROSOFT_PEERING = "MicrosoftPeering"

class ExpressRouteCircuitSkuFamily(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The family of the SKU. Possible values are: 'UnlimitedData' and 'MeteredData'.
    """

    UNLIMITED_DATA = "UnlimitedData"
    METERED_DATA = "MeteredData"

class ExpressRouteCircuitSkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The tier of the SKU. Possible values are 'Standard' and 'Premium'.
    """

    STANDARD = "Standard"
    PREMIUM = "Premium"

class IPAllocationMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PrivateIP allocation method. Possible values are: 'Static' and 'Dynamic'.
    """

    STATIC = "Static"
    DYNAMIC = "Dynamic"

class IPVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Available from Api-Version 2016-03-30 onwards, it represents whether the specific
    ipconfiguration is IPv4 or IPv6. Default is taken as IPv4.  Possible values are: 'IPv4' and
    'IPv6'.
    """

    I_PV4 = "IPv4"
    I_PV6 = "IPv6"

class LoadDistribution(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The load distribution policy for this rule. Possible values are 'Default', 'SourceIP', and
    'SourceIPProtocol'.
    """

    DEFAULT = "Default"
    SOURCE_IP = "SourceIP"
    SOURCE_IP_PROTOCOL = "SourceIPProtocol"

class NetworkOperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the Azure async operation. Possible values are: 'InProgress', 'Succeeded', and
    'Failed'.
    """

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class NextHopType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Next hop type.
    """

    INTERNET = "Internet"
    VIRTUAL_APPLIANCE = "VirtualAppliance"
    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    VNET_LOCAL = "VnetLocal"
    HYPER_NET_GATEWAY = "HyperNetGateway"
    NONE = "None"

class PcError(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    INTERNAL_ERROR = "InternalError"
    AGENT_STOPPED = "AgentStopped"
    CAPTURE_FAILED = "CaptureFailed"
    LOCAL_FILE_FAILED = "LocalFileFailed"
    STORAGE_FAILED = "StorageFailed"

class PcProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Protocol to be filtered on.
    """

    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"

class PcStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the packet capture session.
    """

    NOT_STARTED = "NotStarted"
    RUNNING = "Running"
    STOPPED = "Stopped"
    ERROR = "Error"
    UNKNOWN = "Unknown"

class ProbeProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The protocol of the end point. Possible values are: 'Http' or 'Tcp'. If 'Tcp' is specified, a
    received ACK is required for the probe to be successful. If 'Http' is specified, a 200 OK
    response from the specifies URI is required for the probe to be successful.
    """

    HTTP = "Http"
    TCP = "Tcp"

class ProcessorArchitecture(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VPN client Processor Architecture. Possible values are: 'AMD64' and 'X86'.
    """

    AMD64 = "Amd64"
    X86 = "X86"

class Protocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Protocol to be verified on.
    """

    TCP = "TCP"
    UDP = "UDP"

class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the resource.
    """

    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"

class RouteNextHopType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of Azure hop the packet should be sent to. Possible values are:
    'VirtualNetworkGateway', 'VnetLocal', 'Internet', 'VirtualAppliance', and 'None'.
    """

    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    VNET_LOCAL = "VnetLocal"
    INTERNET = "Internet"
    VIRTUAL_APPLIANCE = "VirtualAppliance"
    NONE = "None"

class SecurityRuleAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether network traffic is allowed or denied. Possible values are: 'Allow' and 'Deny'.
    """

    ALLOW = "Allow"
    DENY = "Deny"

class SecurityRuleDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The direction of the rule. Possible values are: 'Inbound and Outbound'.
    """

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"

class SecurityRuleProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The network protocol this rule applies to. Possible values are: 'Tcp', 'Udp', and '*'.
    """

    TCP = "Tcp"
    UDP = "Udp"
    ASTERISK = "*"

class ServiceProviderProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The ServiceProviderProvisioningState state of the resource. Possible values are
    'NotProvisioned', 'Provisioning', 'Provisioned', and 'Deprovisioning'.
    """

    NOT_PROVISIONED = "NotProvisioned"
    PROVISIONING = "Provisioning"
    PROVISIONED = "Provisioned"
    DEPROVISIONING = "Deprovisioning"

class TransportProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The transport protocol for the external endpoint. Possible values are 'Udp' or 'Tcp'
    """

    UDP = "Udp"
    TCP = "Tcp"

class UsageUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An enum describing the unit of measurement.
    """

    COUNT = "Count"

class VirtualNetworkGatewayConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Virtual network Gateway connection status
    """

    UNKNOWN = "Unknown"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    NOT_CONNECTED = "NotConnected"

class VirtualNetworkGatewayConnectionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gateway connection type. Possible values are: 'IPsec','Vnet2Vnet','ExpressRoute', and
    'VPNClient.
    """

    I_PSEC = "IPsec"
    VNET2_VNET = "Vnet2Vnet"
    EXPRESS_ROUTE = "ExpressRoute"
    VPN_CLIENT = "VPNClient"

class VirtualNetworkGatewaySkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gateway SKU name. Possible values are: 'Basic', 'HighPerformance','Standard', and
    'UltraPerformance'.
    """

    BASIC = "Basic"
    HIGH_PERFORMANCE = "HighPerformance"
    STANDARD = "Standard"
    ULTRA_PERFORMANCE = "UltraPerformance"

class VirtualNetworkGatewaySkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gateway SKU tier. Possible values are: 'Basic', 'HighPerformance','Standard', and
    'UltraPerformance'.
    """

    BASIC = "Basic"
    HIGH_PERFORMANCE = "HighPerformance"
    STANDARD = "Standard"
    ULTRA_PERFORMANCE = "UltraPerformance"

class VirtualNetworkGatewayType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of this virtual network gateway. Possible values are: 'Vpn' and 'ExpressRoute'.
    """

    VPN = "Vpn"
    EXPRESS_ROUTE = "ExpressRoute"

class VirtualNetworkPeeringState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the virtual network peering. Possible values are 'Initiated', 'Connected', and
    'Disconnected'.
    """

    INITIATED = "Initiated"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"

class VpnType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of this virtual network gateway. Possible values are: 'PolicyBased' and 'RouteBased'.
    """

    POLICY_BASED = "PolicyBased"
    ROUTE_BASED = "RouteBased"
