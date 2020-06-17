# -*- coding: utf-8 -*-#
# 随便提交
import datetime

def opt_date(number):
    new_time = datetime.datetime.now()
    if isinstance(number, int):
        cut_date = new_time + datetime.timedelta(days=number)
        old_date_str = datetime.datetime.strftime(cut_date, "%Y-%m-%d")
        # print(old_date_str)
        new_time = "这是今天的时间：{}".format(new_time)
        print(new_time)
        return old_date_str

 def SetType(datatype):
     Exeamplelist = datatype
     SetList = list(set(Exeamplelist))
     return SetList

if __name__ == '__main__':
    type_list = ["bc","bc","权限","leixing"]
    print(SetType(type_list))
    print(opt_date(-1))
