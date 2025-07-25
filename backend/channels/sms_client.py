# Copyright 2025 Ashwin Raj
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
import json
import streamlit as st
from twilio.rest import Client


class NotificationSMS:
    def __init__(self):
        account_sid = st.secrets["TWILIO_ACCOUNT_SID"]
        auth_token = st.secrets["TWILIO_AUTH_TOKEN"]

        self.client = Client(account_sid, auth_token)

        self.sender_phone_number = st.secrets["TWILIO_PHONE_NUMBER"]
        self.messaging_service_sid = st.secrets["TWILIO_MESSAGING_SERVICE_SID"]

    def send_onsite_service_request_confirmation_sms(
        self, receivers_phone_number, service_request_id
    ):
        sms_body = f"""
        Request Id: {service_request_id} confirmed!
        We'll assign an engineer soon and update you with their details
         - LogIQ Support Team
        """

        receivers_phone_number = receivers_phone_number.replace("+91", "")

        try:
            message = self.client.messages.create(
                body=sms_body,
                to=f"+91{receivers_phone_number}",
                messaging_service_sid=self.messaging_service_sid,
            )

            return True

        except Exception as error:
            return False

    def send_onsite_service_request_engineer_assigned_sms(
        self, 
        receivers_phone_number, 
        service_request_id, 
        engineer_id, 
        engineer_name,
    ):
        sms_body = f"""
        Engineer {engineer_name} (Id: {engineer_id}) assigned to
        Request Id: {service_request_id} - LogIQ Support Team
        """

        receivers_phone_number = receivers_phone_number.replace("+91", "")

        try:
            message = self.client.messages.create(
                body=sms_body,
                to=f"+91{receivers_phone_number}",
                messaging_service_sid=self.messaging_service_sid,
            )

            return True

        except Exception as error:
            return False

    def send_onsite_service_request_resolution_started_sms(
        self,
        receivers_phone_number,
        service_request_id,
        engineer_id,
        engineer_name,
    ):
        sms_body = f"""
        Engineer {engineer_name} (Id: {engineer_id}) has started working
        on resolving Request Id {service_request_id} - LogIQ Support Team
        """

        receivers_phone_number = receivers_phone_number.replace("+91", "")

        try:
            message = self.client.messages.create(
                body=sms_body,
                to=f"+91{receivers_phone_number}",
                messaging_service_sid=self.messaging_service_sid,
            )

            return True

        except Exception as error:
            return False

    def send_onsite_service_request_resolved_sms(
        self,
        receivers_phone_number,
        service_request_id,
        engineer_name,
    ):
        sms_body = f"""
        Request Id {service_request_id} successfully resolved by
        Engineer {engineer_name} - LogIQ Support Team
        """

        receivers_phone_number = receivers_phone_number.replace("+91", "")

        try:
            message = self.client.messages.create(
                body=sms_body,
                to=f"+91{receivers_phone_number}",
                messaging_service_sid=self.messaging_service_sid,
            )

            return True

        except Exception as error:
            return False
