# -*-coding: utf-8-*-


def bao_shi(basic, num):
    for x in range(num):
        basic *= 1.03
    return basic

print bao_shi(30, 8)