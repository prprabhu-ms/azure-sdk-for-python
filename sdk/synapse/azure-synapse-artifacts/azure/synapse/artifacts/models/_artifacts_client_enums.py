# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AmazonRdsForOraclePartitionOption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    DYNAMIC_RANGE = "DynamicRange"

class AvroCompressionCodec(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    DEFLATE = "deflate"
    SNAPPY = "snappy"
    XZ = "xz"
    BZIP2 = "bzip2"

class AzureFunctionActivityMethod(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The list of HTTP methods supported by a AzureFunctionActivity.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    TRACE = "TRACE"

class AzureSearchIndexWriteBehaviorType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specify the write behavior when upserting documents into Azure Search Index.
    """

    MERGE = "Merge"
    UPLOAD = "Upload"

class BigDataPoolReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Big data pool reference type.
    """

    BIG_DATA_POOL_REFERENCE = "BigDataPoolReference"

class BlobEventType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    MICROSOFT_STORAGE_BLOB_CREATED = "Microsoft.Storage.BlobCreated"
    MICROSOFT_STORAGE_BLOB_DELETED = "Microsoft.Storage.BlobDeleted"

class CassandraSourceReadConsistencyLevels(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The consistency level specifies how many Cassandra servers must respond to a read request
    before returning data to the client application. Cassandra checks the specified number of
    Cassandra servers for data to satisfy the read request. Must be one of
    cassandraSourceReadConsistencyLevels. The default value is 'ONE'. It is case-insensitive.
    """

    ALL = "ALL"
    EACH_QUORUM = "EACH_QUORUM"
    QUORUM = "QUORUM"
    LOCAL_QUORUM = "LOCAL_QUORUM"
    ONE = "ONE"
    TWO = "TWO"
    THREE = "THREE"
    LOCAL_ONE = "LOCAL_ONE"
    SERIAL = "SERIAL"
    LOCAL_SERIAL = "LOCAL_SERIAL"

class CellOutputType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Execution, display, or stream outputs.
    """

    EXECUTE_RESULT = "execute_result"
    DISPLAY_DATA = "display_data"
    STREAM = "stream"
    ERROR = "error"

class CompressionCodec(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """All available compressionCodec values.
    """

    NONE = "none"
    LZO = "lzo"
    BZIP2 = "bzip2"
    GZIP = "gzip"
    DEFLATE = "deflate"
    ZIP_DEFLATE = "zipDeflate"
    SNAPPY = "snappy"
    LZ4 = "lz4"
    TAR = "tar"
    TAR_G_ZIP = "tarGZip"

class CopyBehaviorType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """All available types of copy behavior.
    """

    PRESERVE_HIERARCHY = "PreserveHierarchy"
    FLATTEN_HIERARCHY = "FlattenHierarchy"
    MERGE_FILES = "MergeFiles"

class CreateMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the mode of sql pool creation.
    
    Default: regular sql pool creation.
    
    PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql
    pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and
    restorePointInTime must be specified.
    
    Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId  must be specified as
    the recoverableDatabaseId to restore.
    
    Restore: Creates a sql pool by restoring a backup of a deleted sql  pool. SourceDatabaseId
    should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate
    must be specified.
    """

    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    RECOVERY = "Recovery"
    RESTORE = "Restore"

class DataFlowComputeType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Compute type of the cluster which will execute data flow job.
    """

    GENERAL = "General"
    MEMORY_OPTIMIZED = "MemoryOptimized"
    COMPUTE_OPTIMIZED = "ComputeOptimized"

class DataFlowDebugCommandType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The command type.
    """

    EXECUTE_PREVIEW_QUERY = "executePreviewQuery"
    EXECUTE_STATISTICS_QUERY = "executeStatisticsQuery"
    EXECUTE_EXPRESSION_QUERY = "executeExpressionQuery"

class DataFlowReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Data flow reference type.
    """

    DATA_FLOW_REFERENCE = "DataFlowReference"

class DatasetCompressionLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    OPTIMAL = "Optimal"
    FASTEST = "Fastest"

class DatasetReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Dataset reference type.
    """

    DATASET_REFERENCE = "DatasetReference"

class DayOfWeek(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"

class Db2AuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """AuthenticationType to be used for connection. It is mutually exclusive with connectionString
    property.
    """

    BASIC = "Basic"

class DependencyCondition(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    COMPLETED = "Completed"

class DynamicsAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """All available dynamicsAuthenticationType values.
    """

    OFFICE365 = "Office365"
    IFD = "Ifd"
    AAD_SERVICE_PRINCIPAL = "AADServicePrincipal"

class DynamicsDeploymentType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """All available dynamicsDeploymentType values.
    """

    ONLINE = "Online"
    ON_PREMISES_WITH_IFD = "OnPremisesWithIfd"

class DynamicsServicePrincipalCredentialType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The service principal credential type to use in Server-To-Server authentication.
    'ServicePrincipalKey' for key/secret, 'ServicePrincipalCert' for certificate. Type: string (or
    Expression with resultType string).
    """

    SERVICE_PRINCIPAL_KEY = "ServicePrincipalKey"
    SERVICE_PRINCIPAL_CERT = "ServicePrincipalCert"

class DynamicsSinkWriteBehavior(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Defines values for DynamicsSinkWriteBehavior.
    """

    UPSERT = "Upsert"

class EventSubscriptionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Event Subscription Status.
    """

    ENABLED = "Enabled"
    PROVISIONING = "Provisioning"
    DEPROVISIONING = "Deprovisioning"
    DISABLED = "Disabled"
    UNKNOWN = "Unknown"

class ExpressionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Expression type.
    """

    EXPRESSION = "Expression"

class FtpAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to be used to connect to the FTP server.
    """

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"

class GoogleAdWordsAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The OAuth 2.0 authentication mechanism used for authentication. ServiceAuthentication can only
    be used on self-hosted IR.
    """

    SERVICE_AUTHENTICATION = "ServiceAuthentication"
    USER_AUTHENTICATION = "UserAuthentication"

class GoogleBigQueryAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The OAuth 2.0 authentication mechanism used for authentication. ServiceAuthentication can only
    be used on self-hosted IR.
    """

    SERVICE_AUTHENTICATION = "ServiceAuthentication"
    USER_AUTHENTICATION = "UserAuthentication"

class HBaseAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication mechanism to use to connect to the HBase server.
    """

    ANONYMOUS = "Anonymous"
    BASIC = "Basic"

class HdiNodeTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """All available HdiNodeTypes values.
    """

    HEADNODE = "Headnode"
    WORKERNODE = "Workernode"
    ZOOKEEPER = "Zookeeper"

class HDInsightActivityDebugInfoOption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The HDInsightActivityDebugInfoOption settings to use.
    """

    NONE = "None"
    ALWAYS = "Always"
    FAILURE = "Failure"

class HiveAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication method used to access the Hive server.
    """

    ANONYMOUS = "Anonymous"
    USERNAME = "Username"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"

class HiveServerType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of Hive server.
    """

    HIVE_SERVER1 = "HiveServer1"
    HIVE_SERVER2 = "HiveServer2"
    HIVE_THRIFT_SERVER = "HiveThriftServer"

class HiveThriftTransportProtocol(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The transport protocol to use in the Thrift layer.
    """

    BINARY = "Binary"
    SASL = "SASL"
    HTTP = "HTTP "

class HttpAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to be used to connect to the HTTP server.
    """

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    DIGEST = "Digest"
    WINDOWS = "Windows"
    CLIENT_CERTIFICATE = "ClientCertificate"

class ImpalaAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to use.
    """

    ANONYMOUS = "Anonymous"
    SASL_USERNAME = "SASLUsername"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"

class IntegrationRuntimeEdition(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The edition for the SSIS Integration Runtime
    """

    STANDARD = "Standard"
    ENTERPRISE = "Enterprise"

class IntegrationRuntimeEntityReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of this referenced entity.
    """

    INTEGRATION_RUNTIME_REFERENCE = "IntegrationRuntimeReference"
    LINKED_SERVICE_REFERENCE = "LinkedServiceReference"

class IntegrationRuntimeLicenseType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """License type for bringing your own license scenario.
    """

    BASE_PRICE = "BasePrice"
    LICENSE_INCLUDED = "LicenseIncluded"

class IntegrationRuntimeReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of integration runtime.
    """

    INTEGRATION_RUNTIME_REFERENCE = "IntegrationRuntimeReference"

class IntegrationRuntimeSsisCatalogPricingTier(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The pricing tier for the catalog database. The valid values could be found in
    https://azure.microsoft.com/en-us/pricing/details/sql-database/
    """

    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PREMIUM_RS = "PremiumRS"

class IntegrationRuntimeState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The state of integration runtime.
    """

    INITIAL = "Initial"
    STOPPED = "Stopped"
    STARTED = "Started"
    STARTING = "Starting"
    STOPPING = "Stopping"
    NEED_REGISTRATION = "NeedRegistration"
    ONLINE = "Online"
    LIMITED = "Limited"
    OFFLINE = "Offline"
    ACCESS_DENIED = "AccessDenied"

class IntegrationRuntimeType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of integration runtime.
    """

    MANAGED = "Managed"
    SELF_HOSTED = "SelfHosted"

class JsonFormatFilePattern(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """JSON format file pattern. A property of JsonFormat.
    """

    SET_OF_OBJECTS = "setOfObjects"
    ARRAY_OF_OBJECTS = "arrayOfObjects"

class JsonWriteFilePattern(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """All available filePatterns.
    """

    SET_OF_OBJECTS = "setOfObjects"
    ARRAY_OF_OBJECTS = "arrayOfObjects"

class LivyStates(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The batch state
    """

    NOT_STARTED = "not_started"
    STARTING = "starting"
    IDLE = "idle"
    BUSY = "busy"
    SHUTTING_DOWN = "shutting_down"
    ERROR = "error"
    DEAD = "dead"
    KILLED = "killed"
    SUCCESS = "success"
    RUNNING = "running"
    RECOVERING = "recovering"

class MongoDbAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to be used to connect to the MongoDB database.
    """

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"

class NetezzaPartitionOption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for Netezza read in parallel.
    """

    NONE = "None"
    DATA_SLICE = "DataSlice"
    DYNAMIC_RANGE = "DynamicRange"

class NodeSize(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The level of compute power that each node in the Big Data pool has.
    """

    NONE = "None"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    X_LARGE = "XLarge"
    XX_LARGE = "XXLarge"
    XXX_LARGE = "XXXLarge"

class NodeSizeFamily(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of nodes that the Big Data pool provides.
    """

    NONE = "None"
    MEMORY_OPTIMIZED = "MemoryOptimized"

class NotebookParameterType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Notebook parameter type.
    """

    STRING = "string"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"

class NotebookReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Synapse notebook reference type.
    """

    NOTEBOOK_REFERENCE = "NotebookReference"

class ODataAadServicePrincipalCredentialType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specify the credential type (key or cert) is used for service principal.
    """

    SERVICE_PRINCIPAL_KEY = "ServicePrincipalKey"
    SERVICE_PRINCIPAL_CERT = "ServicePrincipalCert"

class ODataAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of authentication used to connect to the OData service.
    """

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    WINDOWS = "Windows"
    AAD_SERVICE_PRINCIPAL = "AadServicePrincipal"
    MANAGED_SERVICE_IDENTITY = "ManagedServiceIdentity"

class OraclePartitionOption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for Oracle read in parallel.
    """

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    DYNAMIC_RANGE = "DynamicRange"

class OrcCompressionCodec(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    ZLIB = "zlib"
    SNAPPY = "snappy"
    LZO = "lzo"

class ParameterType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Parameter type.
    """

    OBJECT = "Object"
    STRING = "String"
    INT = "Int"
    FLOAT = "Float"
    BOOL = "Bool"
    ARRAY = "Array"
    SECURE_STRING = "SecureString"

class ParquetCompressionCodecEnum(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    GZIP = "gzip"
    SNAPPY = "snappy"
    LZO = "lzo"

class PhoenixAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication mechanism used to connect to the Phoenix server.
    """

    ANONYMOUS = "Anonymous"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"

class PipelineReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Pipeline reference type.
    """

    PIPELINE_REFERENCE = "PipelineReference"

class PluginCurrentState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    PREPARATION = "Preparation"
    RESOURCE_ACQUISITION = "ResourceAcquisition"
    QUEUED = "Queued"
    SUBMISSION = "Submission"
    MONITORING = "Monitoring"
    CLEANUP = "Cleanup"
    ENDED = "Ended"

class PolybaseSettingsRejectType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether the RejectValue property is specified as a literal value or a percentage.
    """

    VALUE = "value"
    PERCENTAGE = "percentage"

class PrestoAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication mechanism used to connect to the Presto server.
    """

    ANONYMOUS = "Anonymous"
    LDAP = "LDAP"

class RecurrenceFrequency(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates possible frequency option for the schedule trigger.
    """

    NOT_SPECIFIED = "NotSpecified"
    MINUTE = "Minute"
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"

class RequestStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates possible request statuses.
    """

    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"

class ResourceIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of managed identity for the workspace
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"

class ResourceStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates possible Status of the resource.
    """

    CREATING = "Creating"
    CREATED = "Created"
    FAILED = "Failed"

class RestServiceAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of authentication used to connect to the REST service.
    """

    ANONYMOUS = "Anonymous"
    BASIC = "Basic"
    AAD_SERVICE_PRINCIPAL = "AadServicePrincipal"
    MANAGED_SERVICE_IDENTITY = "ManagedServiceIdentity"

class RunQueryFilterOperand(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Parameter name to be used for filter. The allowed operands to query pipeline runs are
    PipelineName, RunStart, RunEnd and Status; to query activity runs are ActivityName,
    ActivityRunStart, ActivityRunEnd, ActivityType and Status, and to query trigger runs are
    TriggerName, TriggerRunTimestamp and Status.
    """

    PIPELINE_NAME = "PipelineName"
    STATUS = "Status"
    RUN_START = "RunStart"
    RUN_END = "RunEnd"
    ACTIVITY_NAME = "ActivityName"
    ACTIVITY_RUN_START = "ActivityRunStart"
    ACTIVITY_RUN_END = "ActivityRunEnd"
    ACTIVITY_TYPE = "ActivityType"
    TRIGGER_NAME = "TriggerName"
    TRIGGER_RUN_TIMESTAMP = "TriggerRunTimestamp"
    RUN_GROUP_ID = "RunGroupId"
    LATEST_ONLY = "LatestOnly"

class RunQueryFilterOperator(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Operator to be used for filter.
    """

    EQUALS = "Equals"
    NOT_EQUALS = "NotEquals"
    IN_ENUM = "In"
    NOT_IN = "NotIn"

class RunQueryOrder(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Sorting order of the parameter.
    """

    ASC = "ASC"
    DESC = "DESC"

class RunQueryOrderByField(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Parameter name to be used for order by. The allowed parameters to order by for pipeline runs
    are PipelineName, RunStart, RunEnd and Status; for activity runs are ActivityName,
    ActivityRunStart, ActivityRunEnd and Status; for trigger runs are TriggerName,
    TriggerRunTimestamp and Status.
    """

    RUN_START = "RunStart"
    RUN_END = "RunEnd"
    PIPELINE_NAME = "PipelineName"
    STATUS = "Status"
    ACTIVITY_NAME = "ActivityName"
    ACTIVITY_RUN_START = "ActivityRunStart"
    ACTIVITY_RUN_END = "ActivityRunEnd"
    TRIGGER_NAME = "TriggerName"
    TRIGGER_RUN_TIMESTAMP = "TriggerRunTimestamp"

class SalesforceSinkWriteBehavior(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The write behavior for the operation. Default is Insert.
    """

    INSERT = "Insert"
    UPSERT = "Upsert"

class SalesforceSourceReadBehavior(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The read behavior for the operation. Default is Query.
    """

    QUERY = "Query"
    QUERY_ALL = "QueryAll"

class SapCloudForCustomerSinkWriteBehavior(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The write behavior for the operation. Default is 'Insert'.
    """

    INSERT = "Insert"
    UPDATE = "Update"

class SapHanaAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to be used to connect to the SAP HANA server.
    """

    BASIC = "Basic"
    WINDOWS = "Windows"

class SapHanaPartitionOption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for SAP HANA read in parallel.
    """

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    SAP_HANA_DYNAMIC_RANGE = "SapHanaDynamicRange"

class SapTablePartitionOption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for SAP table read in parallel.
    """

    NONE = "None"
    PARTITION_ON_INT = "PartitionOnInt"
    PARTITION_ON_CALENDAR_YEAR = "PartitionOnCalendarYear"
    PARTITION_ON_CALENDAR_MONTH = "PartitionOnCalendarMonth"
    PARTITION_ON_CALENDAR_DATE = "PartitionOnCalendarDate"
    PARTITION_ON_TIME = "PartitionOnTime"

class SchedulerCurrentState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    QUEUED = "Queued"
    SCHEDULED = "Scheduled"
    ENDED = "Ended"

class ScriptActivityLogDestination(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The destination of logs. Type: string.
    """

    ACTIVITY_OUTPUT = "ActivityOutput"
    EXTERNAL_STORE = "ExternalStore"

class ScriptActivityParameterDirection(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The direction of the parameter.
    """

    INPUT = "Input"
    OUTPUT = "Output"
    INPUT_OUTPUT = "InputOutput"

class ScriptActivityParameterType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the parameter.
    """

    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    DATE_TIME_OFFSET = "DateTimeOffset"
    DECIMAL = "Decimal"
    DOUBLE = "Double"
    GUID = "Guid"
    INT16 = "Int16"
    INT32 = "Int32"
    INT64 = "Int64"
    SINGLE = "Single"
    STRING = "String"
    TIMESPAN = "Timespan"

class ScriptType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the query. Type: string.
    """

    QUERY = "Query"
    NON_QUERY = "NonQuery"

class ServiceNowAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to use.
    """

    BASIC = "Basic"
    O_AUTH2 = "OAuth2"

class SftpAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to be used to connect to the FTP server.
    """

    BASIC = "Basic"
    SSH_PUBLIC_KEY = "SshPublicKey"

class SparkAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication method used to access the Spark server.
    """

    ANONYMOUS = "Anonymous"
    USERNAME = "Username"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"

class SparkBatchJobResultType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The Spark batch job result.
    """

    UNCERTAIN = "Uncertain"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"

class SparkErrorSource(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    SYSTEM = "System"
    USER = "User"
    UNKNOWN = "Unknown"
    DEPENDENCY = "Dependency"

class SparkJobReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Synapse spark job reference type.
    """

    SPARK_JOB_DEFINITION_REFERENCE = "SparkJobDefinitionReference"

class SparkJobType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The job type.
    """

    SPARK_BATCH = "SparkBatch"
    SPARK_SESSION = "SparkSession"

class SparkServerType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of Spark server.
    """

    SHARK_SERVER = "SharkServer"
    SHARK_SERVER2 = "SharkServer2"
    SPARK_THRIFT_SERVER = "SparkThriftServer"

class SparkThriftTransportProtocol(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The transport protocol to use in the Thrift layer.
    """

    BINARY = "Binary"
    SASL = "SASL"
    HTTP = "HTTP "

class SqlConnectionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the connection.
    """

    SQL_ON_DEMAND = "SqlOnDemand"
    SQL_POOL = "SqlPool"

class SqlPartitionOption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for Sql read in parallel.
    """

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    DYNAMIC_RANGE = "DynamicRange"

class SqlPoolReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SQL pool reference type.
    """

    SQL_POOL_REFERENCE = "SqlPoolReference"

class SqlScriptType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the SQL script.
    """

    SQL_QUERY = "SqlQuery"

class SsisLogLocationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of SSIS log location.
    """

    FILE = "File"

class SsisPackageLocationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of SSIS package location.
    """

    SSISDB = "SSISDB"
    FILE = "File"
    INLINE_PACKAGE = "InlinePackage"
    PACKAGE_STORE = "PackageStore"

class StoredProcedureParameterType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Stored procedure parameter type.
    """

    STRING = "String"
    INT = "Int"
    INT64 = "Int64"
    DECIMAL = "Decimal"
    GUID = "Guid"
    BOOLEAN = "Boolean"
    DATE = "Date"

class SybaseAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """AuthenticationType to be used for connection.
    """

    BASIC = "Basic"
    WINDOWS = "Windows"

class TeamDeskAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to use.
    """

    BASIC = "Basic"
    TOKEN = "Token"

class TeradataAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """AuthenticationType to be used for connection.
    """

    BASIC = "Basic"
    WINDOWS = "Windows"

class TeradataPartitionOption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for teradata read in parallel.
    """

    NONE = "None"
    HASH = "Hash"
    DYNAMIC_RANGE = "DynamicRange"

class TriggerReferenceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Trigger reference type.
    """

    TRIGGER_REFERENCE = "TriggerReference"

class TriggerRunStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Trigger run status.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    INPROGRESS = "Inprogress"

class TriggerRuntimeState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates possible state of Triggers.
    """

    STARTED = "Started"
    STOPPED = "Stopped"
    DISABLED = "Disabled"

class TumblingWindowFrequency(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates possible frequency option for the tumbling window trigger.
    """

    MINUTE = "Minute"
    HOUR = "Hour"
    MONTH = "Month"

class Type(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Linked service reference type.
    """

    LINKED_SERVICE_REFERENCE = "LinkedServiceReference"

class VariableType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Variable type.
    """

    STRING = "String"
    BOOL = "Bool"
    BOOLEAN = "Boolean"
    ARRAY = "Array"

class WebActivityMethod(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The list of HTTP methods supported by a WebActivity.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

class WebAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of authentication used to connect to the web table source.
    """

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    CLIENT_CERTIFICATE = "ClientCertificate"

class WebHookActivityMethod(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The list of HTTP methods supported by a WebHook activity.
    """

    POST = "POST"

class ZendeskAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to use.
    """

    BASIC = "Basic"
    TOKEN = "Token"
