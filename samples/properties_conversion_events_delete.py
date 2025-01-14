#!/usr/bin/env python

# Copyright 2021 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Analytics Admin API sample application which deletes a conversion
event for the Google Analytics 4 property.


See https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/properties.conversionEvents/delete
for more information.
"""
# [START analyticsadmin_properties_conversion_events_delete]
from google.analytics.admin import AnalyticsAdminServiceClient


def run_sample():
    """Runs the sample."""

    # !!! ATTENTION !!!
    #  Running this sample may change/delete your Google Analytics account
    #  configuration. Make sure to not use the Google Analytics property ID from
    #  your production environment below.

    # TODO(developer): Replace this variable with your Google Analytics 4
    #  property ID (e.g. "123456") before running the sample.
    property_id = "YOUR-GA4-PROPERTY-ID"

    # TODO(developer): Replace this variable with your conversion event ID
    #  (e.g. "123456") before running the sample.
    conversion_event_id = "YOUR-CONVERSION-EVENT-ID"

    delete_conversion_event(property_id, conversion_event_id)


def delete_conversion_event(property_id, conversion_event_id):
    """Deletes the conversion event for the Google Analytics 4 property."""
    client = AnalyticsAdminServiceClient()
    client.delete_conversion_event(
        name=f"properties/{property_id}/conversionEvents/{conversion_event_id}"
    )
    print("Conversion event deleted")


# [END analyticsadmin_properties_conversion_events_delete]


if __name__ == "__main__":
    run_sample()
