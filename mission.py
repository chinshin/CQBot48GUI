# -*- coding: utf-8 -*-
from PyQt5.QtCore import QThread
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from pref import Preferences
from CQLog import INFO, WARN
from koudai48 import Koudai
from modian import newOrder, md_init, rank, result
from weibo import Weibo
from cqhttp import CQHttp


class ListenGroup(QThread):

    def __init__(self):
        super(QThread, self).__init__()
        self.pref5 = Preferences()
        self.api_root_url = 'http://127.0.0.1:%s/' % self.pref5.getapi_root_port()
        self.post_port = int(self.pref5.getpost_url_port())
        self.bot = CQHttp(api_root=self.api_root_url)

    def run(self):
        @self.bot.on_message('group')
        def handle_msg(context):
            if context['group_id'] in self.pref5.getqqidarray() and context['user_id'] != context['self_id']:
                # 关键词禁言
                if self.pref5.getshutwordslist():
                    for word in self.pref5.getshutwordslist():
                        if word in context['message']:
                            self.bot.set_group_ban(group_id=context['group_id'], user_id=context['user_id'], duration=30*60)
                # 关键词回复
                if context['message'] == '集资' or context['message'] == 'jz' or context['message'] == '打卡' or context['message'] == 'dk':
                    jz = ''
                    jz_array = md_init(self.pref5.getproidarray())
                    for jz_dict in jz_array:
                        jz += jz_dict['name'] + '\n' + jz_dict['url_short'] + '\n'
                    self.bot.send(context, jz)
                elif context['message'] == 'wds20' or context['message'] == 'jz20' or context['message'] == 'rank' or context['message'] == '聚聚榜' or context['message'] == 'jzb' or context['message'] == '集资榜':
                    rank1_array = rank(1)
                    for rank1_msg in rank1_array:
                        self.bot.send(context, rank1_msg)
                elif context['message'] == 'dkb' or context['message'] == '打卡榜' or context['message'] == 'dk20' or context['message'] == 'dakabang':
                    rank2_array = rank(2)
                    for rank2_msg in rank2_array:
                        self.bot.send(context, rank2_msg)
                elif "独占" in context['message']:
                    dz = ''
                    dz_array = md_init(self.pref5.getproidarray())
                    for dz_dict in dz_array:
                        dz += dz_dict['name'] + '\n' + dz_dict['url_short'] + '\n'
                    duzhan = "独占请集资" + '\n' + dz
                    self.bot.send(context, duzhan)
                elif context['message'] == '欢迎新人':
                    self.bot.send(context, self.pref5.getwelcome())
                elif context['message'] == '项目进度' or context['message'] == '进度':
                    jd_array = result(self.pref5.getproidarray())
                    jd = ''
                    for jd_msg in jd_array:
                        jd += jd_msg + '\n'
                    self.bot.send(context, jd)

        # 新人加群提醒
        @self.bot.on_event('group_increase')
        def handle_group_increase(context):
            if context['group_id'] == self.pref5.getqqidarray[0]:
                # ret = bot.get_stranger_info(user_id=context['user_id'], no_cache=False)
                # welcome = '欢迎新聚聚：@' + ret['nickname'] + ' 加入本群\n\n' + setting.welcome()
                welcome = [{'type': 'text', 'data': {'text': '欢迎新聚聚：'}},
                {'type': 'at', 'data': {'qq': str(context['user_id'])}},
                {'type': 'text', 'data': {'text': ' 加入本群\n\n%s' % self.pref5.getwelcome()}}
                ]
                self.bot.send(context, message=welcome, is_raw=True)  # 发送欢迎新人

        # 如果修改了端口，请修改http-API插件的配置文件中对应的post_url
        self.bot.run(host='127.0.0.1', port=self.post_port)


class ListenKdMdWb(QThread):

    def __init__(self, kd, md, wb):
        super(QThread, self).__init__()
        self.switch_kd = kd
        self.switch_md = md
        self.switch_wb = wb
        self.sched = BlockingScheduler()
        self.weibo_id_array = []
        self.firstcheck_weibo = True
        self.pref3 = Preferences()
        self.api_root_url = 'http://127.0.0.1:%s/' % self.pref3.getapi_root_port()
        self.bot = CQHttp(api_root=self.api_root_url)
        self.version_dict = self.bot.get_version_info()
        self.version = self.version_dict['coolq_edition']

    def run(self):
        if self.switch_md:
            self.interval_md = int(self.pref3.getmdinterval())
            self.sched.add_job(self.getmodian, 'interval', seconds=self.interval_md,
                               misfire_grace_time=10, coalesce=True, max_instances=2)
        if self.switch_wb:
            self.interval_wb = int(self.pref3.getwbinterval())
            self.sched.add_job(self.getweibo, 'interval', seconds=self.interval_wb,
                               misfire_grace_time=10, coalesce=True, max_instances=2)
        if self.switch_kd:
            self.interval_kd = int(self.pref3.getkdinterval())
            self.sched.add_job(self.getkoudai, 'interval', seconds=self.interval_kd,
                               misfire_grace_time=10, coalesce=True, max_instances=2)
        self.sched.start()

    def getmodian(self):
        try:
            INFO('check modian')
            stampTime = int(time.time())
            msgDict_array = newOrder(stampTime, int(self.interval_md))
            for msgDict in msgDict_array[0:-1]:
                if msgDict:
                    for msg in msgDict['msg']:
                        msg += msgDict['end']
                        print(msg)
                        for grpid in self.pref3.getqqidarray():
                            self.bot.send_group_msg_async(
                                group_id=grpid, message=msg, auto_escape=False)
                            time.sleep(0.1)
        except Exception as e:
            WARN('error when getModian', e, "modian dict:", msgDict_array[-1])
        finally:
            INFO('modian check completed')

    def getweibo(self):
        try:
            weibo = Weibo()
            INFO('check weibo')
            # 初次启动记录前十条微博id
            if self.firstcheck_weibo is True:
                INFO('first check weibo')
                self.weibo_id_array = weibo.IdArray
                self.firstcheck_weibo = False
            if self.firstcheck_weibo is False:
                # 取最新的前三条微博
                for idcount in range(0, 3):
                    # 广告位微博id为0，忽略
                    if int(weibo.IdArray[idcount]) == 0:
                        continue
                    # 微博id不在记录的id列表里，判断为新微博
                    if weibo.IdArray[idcount] not in self.weibo_id_array:
                        msg = []
                        # 将id计入id列表
                        self.weibo_id_array.append(weibo.IdArray[idcount])
                        # 检查新微博是否是转发
                        if weibo.checkRetweet(idcount):
                            msg.append(
                                {
                                    'type': 'text',
                                    'data': {'text': '小偶像刚刚转发了一条微博：\n'}})
                            msg.append(
                                {
                                    'type': 'text',
                                    'data': {'text': '%s\n' % weibo.getRetweetWeibo(idcount)}})
                        # 原创微博
                        else:
                            msg.append(
                                {
                                    'type': 'text',
                                    'data': {'text': '小偶像刚刚发了一条新微博：\n'}})
                            msg.append(
                                {
                                    'type': 'text',
                                    'data': {'text': '%s\n' % weibo.getWeibo(idcount)}})
                            # 检查原创微博是否带图
                            if weibo.checkPic(idcount):
                                # 只取第一张图，pro可以直接发图，air则无
                                msg.append(
                                    {
                                        'type': 'image',
                                        'data': {'file': '%s' % weibo.getPic(idcount)[0]}})
                                # 播报图的总数
                                if len(weibo.getPic(idcount)) > 1:
                                    msg.append(
                                        {
                                            'type': 'text',
                                            'data': {'text': '\n(一共有%d张图喔)\n' % len(weibo.getPic(idcount))}})
                        msg.append(
                            {
                                'type': 'text',
                                'data': {'text': '传送门：%s' % weibo.getScheme(idcount)}})
                        for grpid in self.pref3.getqqidarray():
                            self.bot.send_group_msg_async(
                                group_id=grpid, message=msg, auto_escape=False)
                            time.sleep(0.5)
                        print(msg)
        except Exception as e:
            WARN('error when getWeibo', e)
        finally:
            INFO('weibo check completed')

    def getkoudai(self):
        try:
            INFO('check koudai room')
            koudai = Koudai()
            # 检查是否有新消息
            if koudai.checkNew():
                INFO('have new room msg')
                # 判断酷Q版本
                if self.version == 'air':
                    msgArray = koudai.msgAir()
                elif self.version == 'pro':
                    msgArray = koudai.msgPro()
                # 消息序列反向排序
                msgArray.reverse()
                for msg in msgArray:
                    print(msg)
                    for grpid in self.pref3.getqqidarray():
                        self.bot.send_group_msg_async(
                            group_id=grpid, message=msg, auto_escape=False)
                        time.sleep(0.5)
        except Exception as e:
            WARN('error when getRoomMsg', e)
            raise e
        finally:
            INFO('koudai check completed')


#
