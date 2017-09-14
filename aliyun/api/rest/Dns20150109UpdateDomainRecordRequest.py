'''
Created by auto_sdk on 2015.09.21
'''
from aliyun.api.base import RestApi
import datetime

class Dns20150109UpdateDomainRecordRequest(RestApi):
	def __init__(self,address,recordid,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Line = "default"
		self.Priority = None
		self.RR = "@"
		self.RecordId = recordid
		self.Timestamp = datetime.datetime.utcnow().isoformat()
		self.TTL = None
		self.Type = "A"
		self.Value = address

	def getapiname(self):
		return 'dns.aliyuncs.com.UpdateDomainRecord.2015-01-09'

	def getIp(self):
		print self.Value
