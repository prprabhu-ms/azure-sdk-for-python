# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.6.6, generator: @autorest/python@5.12.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AcrAccessToken
    from ._models_py3 import AcrErrorInfo
    from ._models_py3 import AcrErrors
    from ._models_py3 import AcrManifests
    from ._models_py3 import AcrRefreshToken
    from ._models_py3 import Annotations
    from ._models_py3 import ArtifactManifestPlatform
    from ._models_py3 import ArtifactManifestProperties
    from ._models_py3 import ArtifactTagProperties
    from ._models_py3 import ContainerRepositoryProperties
    from ._models_py3 import DeleteRepositoryResult
    from ._models_py3 import Descriptor
    from ._models_py3 import FsLayer
    from ._models_py3 import History
    from ._models_py3 import ImageSignature
    from ._models_py3 import JWK
    from ._models_py3 import JWKHeader
    from ._models_py3 import Manifest
    from ._models_py3 import ManifestAttributesBase
    from ._models_py3 import ManifestAttributesManifest
    from ._models_py3 import ManifestList
    from ._models_py3 import ManifestListAttributes
    from ._models_py3 import ManifestWrapper
    from ._models_py3 import ManifestWriteableProperties
    from ._models_py3 import OCIIndex
    from ._models_py3 import OCIManifest
    from ._models_py3 import Paths108HwamOauth2ExchangePostRequestbodyContentApplicationXWwwFormUrlencodedSchema
    from ._models_py3 import PathsV3R3RxOauth2TokenPostRequestbodyContentApplicationXWwwFormUrlencodedSchema
    from ._models_py3 import Platform
    from ._models_py3 import Repositories
    from ._models_py3 import RepositoryTags
    from ._models_py3 import RepositoryWriteableProperties
    from ._models_py3 import TagAttributesBase
    from ._models_py3 import TagAttributesTag
    from ._models_py3 import TagList
    from ._models_py3 import TagWriteableProperties
    from ._models_py3 import V1Manifest
    from ._models_py3 import V2Manifest
except (SyntaxError, ImportError):
    from ._models import AcrAccessToken  # type: ignore
    from ._models import AcrErrorInfo  # type: ignore
    from ._models import AcrErrors  # type: ignore
    from ._models import AcrManifests  # type: ignore
    from ._models import AcrRefreshToken  # type: ignore
    from ._models import Annotations  # type: ignore
    from ._models import ArtifactManifestPlatform  # type: ignore
    from ._models import ArtifactManifestProperties  # type: ignore
    from ._models import ArtifactTagProperties  # type: ignore
    from ._models import ContainerRepositoryProperties  # type: ignore
    from ._models import DeleteRepositoryResult  # type: ignore
    from ._models import Descriptor  # type: ignore
    from ._models import FsLayer  # type: ignore
    from ._models import History  # type: ignore
    from ._models import ImageSignature  # type: ignore
    from ._models import JWK  # type: ignore
    from ._models import JWKHeader  # type: ignore
    from ._models import Manifest  # type: ignore
    from ._models import ManifestAttributesBase  # type: ignore
    from ._models import ManifestAttributesManifest  # type: ignore
    from ._models import ManifestList  # type: ignore
    from ._models import ManifestListAttributes  # type: ignore
    from ._models import ManifestWrapper  # type: ignore
    from ._models import ManifestWriteableProperties  # type: ignore
    from ._models import OCIIndex  # type: ignore
    from ._models import OCIManifest  # type: ignore
    from ._models import Paths108HwamOauth2ExchangePostRequestbodyContentApplicationXWwwFormUrlencodedSchema  # type: ignore
    from ._models import PathsV3R3RxOauth2TokenPostRequestbodyContentApplicationXWwwFormUrlencodedSchema  # type: ignore
    from ._models import Platform  # type: ignore
    from ._models import Repositories  # type: ignore
    from ._models import RepositoryTags  # type: ignore
    from ._models import RepositoryWriteableProperties  # type: ignore
    from ._models import TagAttributesBase  # type: ignore
    from ._models import TagAttributesTag  # type: ignore
    from ._models import TagList  # type: ignore
    from ._models import TagWriteableProperties  # type: ignore
    from ._models import V1Manifest  # type: ignore
    from ._models import V2Manifest  # type: ignore

from ._container_registry_enums import (
    ArtifactArchitecture,
    ArtifactManifestOrderBy,
    ArtifactOperatingSystem,
    ArtifactTagOrderBy,
    PostContentSchemaGrantType,
    TokenGrantType,
)

__all__ = [
    'AcrAccessToken',
    'AcrErrorInfo',
    'AcrErrors',
    'AcrManifests',
    'AcrRefreshToken',
    'Annotations',
    'ArtifactManifestPlatform',
    'ArtifactManifestProperties',
    'ArtifactTagProperties',
    'ContainerRepositoryProperties',
    'DeleteRepositoryResult',
    'Descriptor',
    'FsLayer',
    'History',
    'ImageSignature',
    'JWK',
    'JWKHeader',
    'Manifest',
    'ManifestAttributesBase',
    'ManifestAttributesManifest',
    'ManifestList',
    'ManifestListAttributes',
    'ManifestWrapper',
    'ManifestWriteableProperties',
    'OCIIndex',
    'OCIManifest',
    'Paths108HwamOauth2ExchangePostRequestbodyContentApplicationXWwwFormUrlencodedSchema',
    'PathsV3R3RxOauth2TokenPostRequestbodyContentApplicationXWwwFormUrlencodedSchema',
    'Platform',
    'Repositories',
    'RepositoryTags',
    'RepositoryWriteableProperties',
    'TagAttributesBase',
    'TagAttributesTag',
    'TagList',
    'TagWriteableProperties',
    'V1Manifest',
    'V2Manifest',
    'ArtifactArchitecture',
    'ArtifactManifestOrderBy',
    'ArtifactOperatingSystem',
    'ArtifactTagOrderBy',
    'PostContentSchemaGrantType',
    'TokenGrantType',
]
