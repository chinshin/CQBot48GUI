# -*- coding: utf-8 -*-
import configparser
import os
import csv

class member(object):

    def __init__(self):
        self.base_dir = os.path.dirname(__file__)
        self.roomid_path = os.path.join(self.base_dir, 'roomID.conf')
        self.member_path = os.path.join(self.base_dir, 'member.csv')

    def getroomidsections(self):
        cf = configparser.ConfigParser()
        with open(self.roomid_path, 'r', encoding='utf-8') as cfgfile:
            cf.read_file(cfgfile)
            return cf.sections()

    def getroomidtuples(self, section):
        cf = configparser.ConfigParser()
        with open(self.roomid_path, 'r', encoding='utf-8') as cfgfile:
            cf.read_file(cfgfile)
            return cf.items(str(section))

    def getroomid(self, section, option):
        cf = configparser.ConfigParser()
        with open(self.roomid_path, 'r', encoding='utf-8') as cfgfile:
            cf.read_file(cfgfile)
            return cf.get(str(section), str(option))

    def teamofgroup(self, group):
        pass




#

#
