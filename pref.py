# -*- coding: utf-8 -*-
import random
import configparser
import os
import requests
import json
import urllib3


class Preferences(object):
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.base_dir = os.path.dirname(__file__)
        self.file_path = os.path.join(self.base_dir, 'preferences.conf')
        if not os.path.exists(self.file_path):
            self.createconf()

    def createconf(self):
        cf = configparser.ConfigParser()
        with open(self.file_path, 'w+', encoding='utf-8') as cfgfile:
            cf.read_file(cfgfile)
            cf.add_section('coolq')
            cf.add_section('idol')
            cf.add_section('modian')
            cf.add_section('koudai48')
            cf.set('koudai48', 'msgtime', '0')
            cf.set('koudai48', 'token', '')
            cf.add_section('qqqun')
            cf.add_section('weibo')
            cf.add_section('proxy')
            cf.write(cfgfile)

    def writecf(self, section, option, value):
        cf = configparser.ConfigParser()
        with open(self.file_path, 'r', encoding='utf-8') as cfgfile:
            cf.read_file(cfgfile)
            with open(self.file_path, 'w+', encoding='utf-8') as cfgfile2:
                cf.set(str(section), str(option), str(value))
                cf.write(cfgfile2)

    def readcf(self, section, option):
        cf = configparser.ConfigParser()
        with open(self.file_path, 'r', encoding='utf-8') as cfgfile:
            cf.read_file(cfgfile)
            try:
                result = cf.get(str(section), str(option))
            except:
                return None
            else:
                return result

    def writeapi_root_port(self, port):
        self.writecf('coolq', 'api_root_port', port)

    def getapi_root_port(self):
        return self.readcf('coolq', 'api_root_port')

    def writeaccess_token(self, token):
        self.writecf('coolq', 'access_token', token)

    def getaccess_token(self):
        return self.readcf('coolq', 'access_token')

    def writesecret(self, secret):
        self.writecf('coolq', 'secret', secret)

    def getsecret(self):
        return self.readcf('coolq', 'secret')

    def writepost_url_port(self, port):
        self.writecf('coolq', 'post_url_port', port)

    def getpost_url_port(self):
        return self.readcf('coolq', 'post_url_port')

    def writeidolgroup(self, group):
        self.writecf('idol', 'group', group)

    def getidolgroup(self):
        return self.readcf('idol', 'group')

    def writeidolname(self, idolnick):
        self.writecf('idol', 'idolname', str(idolnick))

    def getidolname(self):
        return self.readcf('idol', 'idolname')

    def writeidolnick(self, idolnick):
        self.writecf('idol', 'idolnick', str(idolnick))

    def getidolnick(self):
        return self.readcf('idol', 'idolnick')

    def writeroomid(self, roomid):
        self.writecf('idol', 'roomid', roomid)

    def getroomid(self):
        return self.readcf('idol', 'roomid')

    def writeproid(self, pro_id):
        self.writecf('modian', 'pro_id', str(pro_id))

    def getproid(self):
        return self.readcf('modian', 'pro_id')

    def getproidarray(self):
        proid_str = self.readcf('modian', 'pro_id')
        array = list(map(int, proid_str.split(',')))
        return array

    def writemdinterval(self, seconds):
        self.writecf('modian', 'interval', str(seconds))

    def getmdinterval(self):
        return self.readcf('modian', 'interval')

    def writekdaccount(self, user, password):
        self.writecf('koudai48', 'user', str(user))
        self.writecf('koudai48', 'password', str(password))

    def getkduser(self):
        return self.readcf('koudai48', 'user')

    def getkdpassword(self):
        return self.readcf('koudai48', 'password')

    def gettoken(self):
        return self.readcf('koudai48', 'token')

    def tokenverify(self):
        url = 'https://puser.48.cn/usersystem/api/user/v1/show/cardInfo'
        header = {
            'Host': 'puser.48.cn',
            'version': '5.0.1',
            'os': 'android',
            'Accept-Encoding': 'gzip',
            'IMEI': '866716037125810',
            'User-Agent': 'Mobile_Pocket',
            'Content-Length': '0',
            'Connection': 'Keep-Alive',
            'Content-Type': 'application/json;charset=utf-8',
            'token': self.gettoken()
        }
        response = requests.post(
            url,
            headers=header,
            verify=False
        ).json()
        if response['status'] == 200:
            return True
        else:
            return False

    def requesttoken(self):
        url = 'https://puser.48.cn/usersystem/api/user/v1/login/phone'
        header = {
            'Host': 'puser.48.cn',
            'version': '5.0.1',
            'os': 'android',
            'Accept-Encoding': 'gzip',
            'IMEI': '866716037125810',
            'User-Agent': 'Mobile_Pocket',
            'Content-Length': '75',
            'Connection': 'Keep-Alive',
            'Content-Type': 'application/json;charset=utf-8',
            'token': '0'
        }
        form = {
            "latitude": 0,
            "longitude": 0,
            "password": self.readcf('koudai48', 'password'),
            "account": self.readcf('koudai48', 'user')
        }
        response = requests.post(
            url,
            data=json.dumps(form),
            headers=header,
            verify=False
        ).json()
        if response['status'] == 200:
            newtoken = response['content']['token']
            self.writecf('koudai48', 'token', str(newtoken))
            return True
        else:
            return False

    def writekdinterval(self, seconds):
        self.writecf('koudai48', 'interval', str(seconds))

    def getkdinterval(self):
        return self.readcf('koudai48', 'interval')

    def writekdmsgtime13(self, time13):
        self.writecf('koudai48', 'msgtime', time13)

    def getkdmsgtime13(self):
        return self.readcf('koudai48', 'msgtime')

    def writeqqid(self, qunid):
        self.writecf('qqqun', 'id', str(qunid))

    def getqqid(self):
        return self.readcf('qqqun', 'id')

    def getqqidarray(self):
        strids = self.readcf('qqqun', 'id')
        array = list(map(int, strids.split(',')))
        return array

    def writewelcome(self, sentence):
        self.writecf('qqqun', 'welcome', str(sentence))

    def getwelcome(self):
        return self.readcf('qqqun', 'welcome')

    def writeshutwords(self, words):
        self.writecf('qqqun', 'shutword', words)

    def getshutwords(self):
        return self.readcf('qqqun', 'shutword')

    def getshutwordslist(self):
        words = self.readcf('qqqun', 'shutword')
        array = list(map(str, words.split(',')))
        return array

    def writeweiboid(self, wbid):
        self.writecf('weibo', 'container_id', wbid)

    def getweiboid(self):
        return self.readcf('weibo', 'container_id')

    def getweibourl(self):
        try:
            url = 'https://m.weibo.cn/api/container/getIndex?containerid=' + self.readcf('weibo', 'container_id')
        except:
            return None
        else:
            return url

    def writewbinterval(self, interval):
        self.writecf('weibo', 'interval', interval)

    def getwbinterval(self):
        return self.readcf('weibo', 'interval')

    def writeproxy(self, ip):
        self.writecf('proxy', 'https', ip)

    def getproxy(self):
        return self.readcf('proxy', 'https')

    def chooseproxy(self):
        ips = self.readcf('proxy', 'https')
        array = list(map(str, ips.split(',')))
        return random.choice(array)








#
def get_short_url(long_url_str):
    url = 'http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long=' + str(long_url_str)
    response = requests.get(
        url,
        verify=False
        ).json()
    return response[0]['url_short']
#
