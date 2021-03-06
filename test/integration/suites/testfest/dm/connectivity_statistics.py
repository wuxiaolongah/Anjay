# -*- coding: utf-8 -*-
#
# Copyright 2017 AVSystem <avsystem@avsystem.com>
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

from framework.lwm2m_test import *

from .utils import DataModel, ValueValidator


class Test901_ConnectivityStatistics_QueryingTheReadableResourcesOfObject(DataModel.Test):
    def runTest(self):
        # A READ operation from server on the resource has been received by the client.
        # This test has to be run on the following resources:
        # a) SMS Tx counter
        # b) SMS Rx counter
        # c) Tx data
        # d) Rx data
        # e) Max message size
        # f) Average message size

        self.test_read(ResPath.ConnectivityStatistics.SMSTxCounter,       ValueValidator.integer(), coap.ContentFormat.TEXT_PLAIN)
        self.test_read(ResPath.ConnectivityStatistics.SMSRxCounter,       ValueValidator.integer(), coap.ContentFormat.TEXT_PLAIN)
        self.test_read(ResPath.ConnectivityStatistics.TxData,             ValueValidator.integer(), coap.ContentFormat.TEXT_PLAIN)
        self.test_read(ResPath.ConnectivityStatistics.RxData,             ValueValidator.integer(), coap.ContentFormat.TEXT_PLAIN)
        self.test_read(ResPath.ConnectivityStatistics.MaxMessageSize,     ValueValidator.integer(), coap.ContentFormat.TEXT_PLAIN)
        self.test_read(ResPath.ConnectivityStatistics.AverageMessageSize, ValueValidator.integer(), coap.ContentFormat.TEXT_PLAIN)


class Test910_ConnectivityStatistics_ObservationAndNotificationOfObservableResources(DataModel.Test):
    def runTest(self):
        # The Server establishes an Observation relationship with the Client to acquire
        # condition notifications about observable resources. This test has to be run for
        # the following resources:
        # a) SMS Tx counter
        # b) SMS Rx counter
        # c) Tx data
        # d) Rx data
        # e) Max message size
        # f) Average message size

        self.test_observe(ResPath.ConnectivityStatistics.SMSTxCounter,       ValueValidator.integer())
        self.test_observe(ResPath.ConnectivityStatistics.SMSRxCounter,       ValueValidator.integer())
        self.test_observe(ResPath.ConnectivityStatistics.TxData,             ValueValidator.integer())
        self.test_observe(ResPath.ConnectivityStatistics.RxData,             ValueValidator.integer())
        self.test_observe(ResPath.ConnectivityStatistics.MaxMessageSize,     ValueValidator.integer())
        self.test_observe(ResPath.ConnectivityStatistics.AverageMessageSize, ValueValidator.integer())
