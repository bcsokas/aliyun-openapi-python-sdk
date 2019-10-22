# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkros.endpoint import endpoint_data

class CreateChangeSetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ROS', '2019-09-10', 'CreateChangeSet')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TimeoutInMinutes(self):
		return self.get_query_params().get('TimeoutInMinutes')

	def set_TimeoutInMinutes(self,TimeoutInMinutes):
		self.add_query_param('TimeoutInMinutes',TimeoutInMinutes)

	def get_StackPolicyDuringUpdateBody(self):
		return self.get_query_params().get('StackPolicyDuringUpdateBody')

	def set_StackPolicyDuringUpdateBody(self,StackPolicyDuringUpdateBody):
		self.add_query_param('StackPolicyDuringUpdateBody',StackPolicyDuringUpdateBody)

	def get_StackName(self):
		return self.get_query_params().get('StackName')

	def set_StackName(self,StackName):
		self.add_query_param('StackName',StackName)

	def get_ChangeSetType(self):
		return self.get_query_params().get('ChangeSetType')

	def set_ChangeSetType(self,ChangeSetType):
		self.add_query_param('ChangeSetType',ChangeSetType)

	def get_DisableRollback(self):
		return self.get_query_params().get('DisableRollback')

	def set_DisableRollback(self,DisableRollback):
		self.add_query_param('DisableRollback',DisableRollback)

	def get_Parameterss(self):
		return self.get_query_params().get('Parameterss')

	def set_Parameterss(self,Parameterss):
		for i in range(len(Parameterss)):	
			if Parameterss[i].get('ParameterValue') is not None:
				self.add_query_param('Parameters.' + str(i + 1) + '.ParameterValue' , Parameterss[i].get('ParameterValue'))
			if Parameterss[i].get('ParameterKey') is not None:
				self.add_query_param('Parameters.' + str(i + 1) + '.ParameterKey' , Parameterss[i].get('ParameterKey'))


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_TemplateBody(self):
		return self.get_query_params().get('TemplateBody')

	def set_TemplateBody(self,TemplateBody):
		self.add_query_param('TemplateBody',TemplateBody)

	def get_StackId(self):
		return self.get_query_params().get('StackId')

	def set_StackId(self,StackId):
		self.add_query_param('StackId',StackId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_TemplateURL(self):
		return self.get_query_params().get('TemplateURL')

	def set_TemplateURL(self,TemplateURL):
		self.add_query_param('TemplateURL',TemplateURL)

	def get_NotificationURLss(self):
		return self.get_query_params().get('NotificationURLss')

	def set_NotificationURLss(self,NotificationURLss):
		for i in range(len(NotificationURLss)):	
			if NotificationURLss[i] is not None:
				self.add_query_param('NotificationURLs.' + str(i + 1) , NotificationURLss[i]);

	def get_StackPolicyBody(self):
		return self.get_query_params().get('StackPolicyBody')

	def set_StackPolicyBody(self,StackPolicyBody):
		self.add_query_param('StackPolicyBody',StackPolicyBody)

	def get_StackPolicyDuringUpdateURL(self):
		return self.get_query_params().get('StackPolicyDuringUpdateURL')

	def set_StackPolicyDuringUpdateURL(self,StackPolicyDuringUpdateURL):
		self.add_query_param('StackPolicyDuringUpdateURL',StackPolicyDuringUpdateURL)

	def get_UpdateAllowPolicy(self):
		return self.get_query_params().get('UpdateAllowPolicy')

	def set_UpdateAllowPolicy(self,UpdateAllowPolicy):
		self.add_query_param('UpdateAllowPolicy',UpdateAllowPolicy)

	def get_UsePreviousParameters(self):
		return self.get_query_params().get('UsePreviousParameters')

	def set_UsePreviousParameters(self,UsePreviousParameters):
		self.add_query_param('UsePreviousParameters',UsePreviousParameters)

	def get_OrderSource(self):
		return self.get_query_params().get('OrderSource')

	def set_OrderSource(self,OrderSource):
		self.add_query_param('OrderSource',OrderSource)

	def get_ActivityId(self):
		return self.get_query_params().get('ActivityId')

	def set_ActivityId(self,ActivityId):
		self.add_query_param('ActivityId',ActivityId)

	def get_StackPolicyURL(self):
		return self.get_query_params().get('StackPolicyURL')

	def set_StackPolicyURL(self,StackPolicyURL):
		self.add_query_param('StackPolicyURL',StackPolicyURL)

	def get_ChangeSetName(self):
		return self.get_query_params().get('ChangeSetName')

	def set_ChangeSetName(self,ChangeSetName):
		self.add_query_param('ChangeSetName',ChangeSetName)

	def get_ChannelId(self):
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self,ChannelId):
		self.add_query_param('ChannelId',ChannelId)