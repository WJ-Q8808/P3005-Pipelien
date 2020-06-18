# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         Circle.py

Circle = "圈复杂度"

ThreeKingdoms = [[{"曹操":["司马懿","曹植","曹呸"]}],
                 [{"刘备":["诸葛亮","关羽","张飞","赵云"]}],
                 [{"孙权":["周瑜","鲁肃","吕蒙","黄盖"]}]]

for Kingdoms in ThreeKingdoms:
    celebrity_list = []
    if len(Kingdoms) > 0:
        for Kingdom in Kingdoms:
            if len(Kingdom) > 0:
                Kingdom_people_list = list(Kingdom.values())
                if len(Kingdom_people_list) > 0:
                    for Kingdom_people in Kingdom_people_list:
                        if len(Kingdom_people) > 0:
                            for celebrity in Kingdom_people:
                                celebrity_list.append(celebrity)
    print(celebrity_list)