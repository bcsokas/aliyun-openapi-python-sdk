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
from aliyunsdkrds.endpoint import endpoint_data

class PreCheckCreateOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'PreCheckCreateOrder','rds')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DBInstanceStorage(self):
		return self.get_query_params().get('DBInstanceStorage')

	def set_DBInstanceStorage(self,DBInstanceStorage):
		self.add_query_param('DBInstanceStorage',DBInstanceStorage)

	def get_SystemDBCharset(self):
		return self.get_query_params().get('SystemDBCharset')

	def set_SystemDBCharset(self,SystemDBCharset):
		self.add_query_param('SystemDBCharset',SystemDBCharset)

	def get_CountryCode(self):
		return self.get_query_params().get('CountryCode')

	def set_CountryCode(self,CountryCode):
		self.add_query_param('CountryCode',CountryCode)

	def get_EngineVersion(self):
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self,EngineVersion):
		self.add_query_param('EngineVersion',EngineVersion)

	def get_CurrencyCode(self):
		return self.get_query_params().get('CurrencyCode')

	def set_CurrencyCode(self,CurrencyCode):
		self.add_query_param('CurrencyCode',CurrencyCode)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_DBInstanceDescription(self):
		return self.get_query_params().get('DBInstanceDescription')

	def set_DBInstanceDescription(self,DBInstanceDescription):
		self.add_query_param('DBInstanceDescription',DBInstanceDescription)

	def get_BusinessInfo(self):
		return self.get_query_params().get('BusinessInfo')

	def set_BusinessInfo(self,BusinessInfo):
		self.add_query_param('BusinessInfo',BusinessInfo)

	def get_AgentId(self):
		return self.get_query_params().get('AgentId')

	def set_AgentId(self,AgentId):
		self.add_query_param('AgentId',AgentId)

	def get_Resource(self):
		return self.get_query_params().get('Resource')

	def set_Resource(self,Resource):
		self.add_query_param('Resource',Resource)

	def get_BackupId(self):
		return self.get_query_params().get('BackupId')

	def set_BackupId(self,BackupId):
		self.add_query_param('BackupId',BackupId)

	def get_CommodityCode(self):
		return self.get_query_params().get('CommodityCode')

	def set_CommodityCode(self,CommodityCode):
		self.add_query_param('CommodityCode',CommodityCode)

	def get_EncryptionKey(self):
		return self.get_query_params().get('EncryptionKey')

	def set_EncryptionKey(self,EncryptionKey):
		self.add_query_param('EncryptionKey',EncryptionKey)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DBInstanceClass(self):
		return self.get_query_params().get('DBInstanceClass')

	def set_DBInstanceClass(self,DBInstanceClass):
		self.add_query_param('DBInstanceClass',DBInstanceClass)

	def get_SecurityIPList(self):
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self,SecurityIPList):
		self.add_query_param('SecurityIPList',SecurityIPList)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PrivateIpAddress(self):
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self,PrivateIpAddress):
		self.add_query_param('PrivateIpAddress',PrivateIpAddress)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_PromotionCode(self):
		return self.get_query_params().get('PromotionCode')

	def set_PromotionCode(self,PromotionCode):
		self.add_query_param('PromotionCode',PromotionCode)

	def get_RoleARN(self):
		return self.get_query_params().get('RoleARN')

	def set_RoleARN(self,RoleARN):
		self.add_query_param('RoleARN',RoleARN)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_TimeType(self):
		return self.get_query_params().get('TimeType')

	def set_TimeType(self,TimeType):
		self.add_query_param('TimeType',TimeType)

	def get_InstanceNetworkType(self):
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self,InstanceNetworkType):
		self.add_query_param('InstanceNetworkType',InstanceNetworkType)

	def get_ConnectionMode(self):
		return self.get_query_params().get('ConnectionMode')

	def set_ConnectionMode(self,ConnectionMode):
		self.add_query_param('ConnectionMode',ConnectionMode)

	def get_NodeType(self):
		return self.get_query_params().get('NodeType')

	def set_NodeType(self,NodeType):
		self.add_query_param('NodeType',NodeType)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_ZoneIdSlave1(self):
		return self.get_query_params().get('ZoneIdSlave1')

	def set_ZoneIdSlave1(self,ZoneIdSlave1):
		self.add_query_param('ZoneIdSlave1',ZoneIdSlave1)

	def get_ZoneIdSlave2(self):
		return self.get_query_params().get('ZoneIdSlave2')

	def set_ZoneIdSlave2(self,ZoneIdSlave2):
		self.add_query_param('ZoneIdSlave2',ZoneIdSlave2)

	def get_Engine(self):
		return self.get_query_params().get('Engine')

	def set_Engine(self,Engine):
		self.add_query_param('Engine',Engine)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_DBInstanceStorageType(self):
		return self.get_query_params().get('DBInstanceStorageType')

	def set_DBInstanceStorageType(self,DBInstanceStorageType):
		self.add_query_param('DBInstanceStorageType',DBInstanceStorageType)

	def get_DBInstanceNetType(self):
		return self.get_query_params().get('DBInstanceNetType')

	def set_DBInstanceNetType(self,DBInstanceNetType):
		self.add_query_param('DBInstanceNetType',DBInstanceNetType)

	def get_RestoreTime(self):
		return self.get_query_params().get('RestoreTime')

	def set_RestoreTime(self,RestoreTime):
		self.add_query_param('RestoreTime',RestoreTime)

	def get_Quantity(self):
		return self.get_query_params().get('Quantity')

	def set_Quantity(self,Quantity):
		self.add_query_param('Quantity',Quantity)

	def get_AutoPay(self):
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self,AutoPay):
		self.add_query_param('AutoPay',AutoPay)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_UsedTime(self):
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self,UsedTime):
		self.add_query_param('UsedTime',UsedTime)

	def get_InstanceUsedType(self):
		return self.get_query_params().get('InstanceUsedType')

	def set_InstanceUsedType(self,InstanceUsedType):
		self.add_query_param('InstanceUsedType',InstanceUsedType)

	def get_VPCId(self):
		return self.get_query_params().get('VPCId')

	def set_VPCId(self,VPCId):
		self.add_query_param('VPCId',VPCId)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)