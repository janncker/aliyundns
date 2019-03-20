'''
Created by auto_sdk on 2015.09.21
'''
from aliyun.api.base import RestApi
import datetime

class Dns20150109AddDomainRecordRequest(RestApi):
	def __init__(self,address,host="adascore.com", domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Line = "default"
		self.Priority = None
		self.RR = "@"
		self.DomainName=host
                self.Timestamp = datetime.datetime.utcnow().isoformat()
                self.TTL = None
		self.Type = "A"
		self.Value = address
                print("add-----domain")
	def getapiname(self):
		return 'dns.aliyuncs.com.AddDomainRecord.2015-01-09'

	def getIp(self):
		print self.Value
