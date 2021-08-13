# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import BatchRequest
    from ._models_py3 import DocumentFilter
    from ._models_py3 import DocumentStatus
    from ._models_py3 import DocumentsStatus
    from ._models_py3 import FileFormat
    from ._models_py3 import Glossary
    from ._models_py3 import InnerTranslationError
    from ._models_py3 import SourceInput
    from ._models_py3 import StartTranslationDetails
    from ._models_py3 import StatusSummary
    from ._models_py3 import SupportedFileFormats
    from ._models_py3 import SupportedStorageSources
    from ._models_py3 import TargetInput
    from ._models_py3 import TranslationError
    from ._models_py3 import TranslationErrorResponse
    from ._models_py3 import TranslationStatus
    from ._models_py3 import TranslationsStatus
except (SyntaxError, ImportError):
    from ._models import BatchRequest  # type: ignore
    from ._models import DocumentFilter  # type: ignore
    from ._models import DocumentStatus  # type: ignore
    from ._models import DocumentsStatus  # type: ignore
    from ._models import FileFormat  # type: ignore
    from ._models import Glossary  # type: ignore
    from ._models import InnerTranslationError  # type: ignore
    from ._models import SourceInput  # type: ignore
    from ._models import StartTranslationDetails  # type: ignore
    from ._models import StatusSummary  # type: ignore
    from ._models import SupportedFileFormats  # type: ignore
    from ._models import SupportedStorageSources  # type: ignore
    from ._models import TargetInput  # type: ignore
    from ._models import TranslationError  # type: ignore
    from ._models import TranslationErrorResponse  # type: ignore
    from ._models import TranslationStatus  # type: ignore
    from ._models import TranslationsStatus  # type: ignore

from ._batch_document_translation_client_enums import (
    Status,
    StorageInputType,
    StorageSource,
    TranslationErrorCode,
)

__all__ = [
    'BatchRequest',
    'DocumentFilter',
    'DocumentStatus',
    'DocumentsStatus',
    'FileFormat',
    'Glossary',
    'InnerTranslationError',
    'SourceInput',
    'StartTranslationDetails',
    'StatusSummary',
    'SupportedFileFormats',
    'SupportedStorageSources',
    'TargetInput',
    'TranslationError',
    'TranslationErrorResponse',
    'TranslationStatus',
    'TranslationsStatus',
    'Status',
    'StorageInputType',
    'StorageSource',
    'TranslationErrorCode',
]