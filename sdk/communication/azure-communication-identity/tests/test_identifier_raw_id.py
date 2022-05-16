# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
import unittest
from azure.communication.identity import identifier_from_raw_id

class IdentifierRawIdTest(unittest.TestCase):
    def test_hello(self):
        with pytest.raises(NotImplementedError):
            identifier_from_raw_id('blah')