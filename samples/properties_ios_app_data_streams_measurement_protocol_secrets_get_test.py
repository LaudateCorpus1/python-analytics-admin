# Copyright 2021 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import properties_ios_app_data_streams_measurement_protocol_secrets_get

TEST_PROPERTY_ID = os.getenv("GA_TEST_PROPERTY_ID")
TEST_STREAM_ID = os.getenv("GA_TEST_IOS_APP_DATA_STREAM_ID")
TEST_SECRET_ID = os.getenv("GA_TEST_IOS_APP_DATA_SECRET_ID")


def test_properties_ios_app_data_streams_measurement_protocol_secrets_get(capsys):
    properties_ios_app_data_streams_measurement_protocol_secrets_get.get_measurement_protocol_secret(
        TEST_PROPERTY_ID, TEST_STREAM_ID, TEST_SECRET_ID
    )
    out, _ = capsys.readouterr()
    assert "Result" in out
