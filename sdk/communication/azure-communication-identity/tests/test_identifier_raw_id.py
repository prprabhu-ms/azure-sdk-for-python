# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
import unittest
from azure.communication.identity import *

class IdentifierRawIdTest(unittest.TestCase):
    def test_raw_id(self):
        _assert_raw_id(
            CommunicationUserIdentifier(
                id='8:acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130'
            ),
            '8:acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130'
        )
        _assert_raw_id(
            CommunicationUserIdentifier(
                id='8:gcch-acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130'
            ),
            '8:gcch-acs:bbbcbc1e-9f06-482a-b5d8-20e3f26ef0cd_45ab2481-1c1c-4005-be24-0ffb879b1130'
        )
        _assert_raw_id(
            CommunicationUserIdentifier(
                id='someFutureFormat'
            ),
            'someFutureFormat'
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(
                user_id='45ab2481-1c1c-4005-be24-0ffb879b1130'
            ),
            '8:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130'
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(
                user_id='45ab2481-1c1c-4005-be24-0ffb879b1130',
                cloud='PUBLIC'
            ),
            '8:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130'
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(
                user_id='45ab2481-1c1c-4005-be24-0ffb879b1130',
                cloud='DOD'
            ),
            '8:dod:45ab2481-1c1c-4005-be24-0ffb879b1130'
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(
                user_id='45ab2481-1c1c-4005-be24-0ffb879b1130',
                cloud='GCCH'
            ),
            '8:gcch:45ab2481-1c1c-4005-be24-0ffb879b1130'
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(
                user_id='45ab2481-1c1c-4005-be24-0ffb879b1130',
                is_anonymous=False
            ),
            '8:orgid:45ab2481-1c1c-4005-be24-0ffb879b1130'
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(
                user_id='45ab2481-1c1c-4005-be24-0ffb879b1130',
                is_anonymous=True
            ),
            '8:teamsvisitor:45ab2481-1c1c-4005-be24-0ffb879b1130'
        )
        _assert_raw_id(
            MicrosoftTeamsUserIdentifier(
                user_id='45ab2481-1c1c-4005-be24-0ffb879b1130',
                raw_id='8:orgid:legacyFormat'
            ),
            '8:orgid:legacyFormat'
        )
        _assert_raw_id(
            PhoneNumberIdentifier(
                value='+112345556789'
            ),
            '4:112345556789'
        )
        _assert_raw_id(
            PhoneNumberIdentifier(
                value='+112345556789',
                raw_id='4:otherFormat'
            ),
            '4:otherFormat'
        )
        _assert_raw_id(
            UnknownIdentifier(
                identifier='28:45ab2481-1c1c-4005-be24-0ffb879b1130'
            ),
            '28:45ab2481-1c1c-4005-be24-0ffb879b1130'
        )


def _assert_raw_id(identifier, raw_id):
    # type: (CommunicationIdentifier, str) -> None
    assert identifier.raw_id == raw_id
