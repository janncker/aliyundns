import aliyun.api
import urllib2
import json

class DNS:
    jsonfile = file('/home/aliyun/key.json')
    s = json.load(jsonfile)
    aliyun.setDefaultAppInfo(str(s['id']),str(s['secret']))
    def getDNSIp(self):
        b = aliyun.api.Dns20150109DescribeDomainRecordInfoRequest(str(self.s['RecordId']))
        try:
            f = b.getResponse()
            return (str(f.get('Value')))
        except Exception,e:
            print('getDNSIp:',e)
            return None
    def addDNSIp(self,ip):
        b = aliyun.api.Dns20150109AddDomainRecordRequest(ip)
        try:
            f = b.getResponse()
            return (str(f.get('RecordId')))
        except Exception,e:
            print('addDNSIp:',e)
            return None

    def getMyIp(self):
        try:
            u = urllib2.urlopen('http://members.3322.org/dyndns/getip')
            return u.read().strip('\n')
        except HTTPError as e:
            print('getMyIp:',e)
            return None;

    def saveJson(self):
        with open("key.json","w") as jsonfile:
            json.dump(self.s, jsonfile)

    def main(self,newIp):
        a = aliyun.api.Dns20150109UpdateDomainRecordRequest(newIp, self.s["RecordId"]);
        a.DBInstanceId = ""
        try:
            print("start")
            f = a.getResponse();
            print(f)
        except Exception , e:
            print('main:',e)


if __name__ =='__main__':
    d = DNS()
    newip = d.getMyIp()
    if not d.s.get("RecordId"):
        recordid = d.addDNSIp(newip)
        if recordid:
            d.s["RecordId"] = recordid
            d.saveJson()

    oldip = d.getDNSIp()
    if(oldip != newip and oldip is not None):
        print('oldIp:',oldip)
        print('newIp:',newip)
        d.main(newip)
