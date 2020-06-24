#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
def validate_mask(maskstr):
    ippattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if not ippattern.match(maskstr):
        return False
    iparray = maskstr.split(".");
    ip1 = int(iparray[0])
    ip2 = int(iparray[1])
    ip3 = int(iparray[2])
    ip4 = int(iparray[3])
    if ip1<0 or ip1>255 or ip2<0 or ip2>255 or ip3<0 or ip3>255 or ip4<0 or ip4>255:
       return False
    ip_binary = decimal_to_binary(ip1) + decimal_to_binary(ip2) + decimal_to_binary(ip3) + decimal_to_binary(ip4);
    if -1 != ip_binary.find("01"):
        return False
    return True
def validate_ip(maskstr):
    ippattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if not ippattern.match(maskstr):
        return False
    iparray = maskstr.split(".");
    ip1 = int(iparray[0])
    ip2 = int(iparray[1])
    ip3 = int(iparray[2])
    ip4 = int(iparray[3])
    if ip1<0 or ip1>255 or ip2<0 or ip2>255 or ip3<0 or ip3>255 or ip4<0 or ip4>255:
       return False
    return True
def decimal_to_binary(n):
    b = []
    n = int(n)
    while True:
        s = n // 2
        y = n % 2
        b.append(str(y))
        if s == 0:
            break
        n = s
    b.reverse()
    b = "".join(b)
    b = b.zfill(8)
    return b
def binary_to_decimal(b):
    b = '0b' + str(b)
    return int(b,2)

def calculate_ip_network(ip,subnet):
    a  = []
    a1 = []
    for i in ip.split("."):
        a.append(decimal_to_binary(i))
    for i in subnet.split("."):
        a1.append(decimal_to_binary(i))
    a  = "".join(a)
    a1 = "".join(a1)

    result = []
    for i in range(32):
        if a[i] == '1' and a1[i] == '1':
            result.append('1')
        else:
            result.append('0')

    result_list = re.findall(r'.{8}',"".join(result))
    new_result = []
    for i in result_list:
        new_result.append(str(binary_to_decimal(i)))

    return ".".join(new_result)

def get_broadcast_addr(network,subnet):
    n  = []
    s = []
    for i in network.split("."):
        n.append(decimal_to_binary(i))
    for i in subnet.split("."):
        s.append(decimal_to_binary(i))
    n  = "".join(n)
    s = list("".join(s))
    s.reverse()
    l=0
    flag = True
    for i in s:
        if i!='0':
            flag = False
            break
        else:
            l = l+1
    n = n[0:(len(n)-l)]
    brd  = n+"1"*l
    brd = re.findall(r'.{8}',"".join(brd))
    result=[]
    for i in brd:
        result.append(str(binary_to_decimal(i)))
    return ".".join(result)
def get_first_ip(network,subnet):
    n  = []
    s = []
    for i in network.split("."):
        n.append(decimal_to_binary(i))
    for i in subnet.split("."):
        s.append(decimal_to_binary(i))
    n  = "".join(n)
    s = list("".join(s))
    s.reverse()
    l=0
    flag = True
    for i in s:
        if i!='0':
            flag = False
            break
        else:
            l = l+1
    n = n[0:(len(n)-l)]
    firstip  = n+"0"*(l-1)+"1"
    firstip = re.findall(r'.{8}',"".join(firstip))
    result=[]
    for i in firstip:
        result.append(str(binary_to_decimal(i)))
    return ".".join(result)
def get_last_ip(network,subnet):
    n  = []
    s = []
    for i in network.split("."):
        n.append(decimal_to_binary(i))
    for i in subnet.split("."):
        s.append(decimal_to_binary(i))
    n  = "".join(n)
    s = list("".join(s))
    s.reverse()
    l=0
    flag = True
    for i in s:
        if i!='0':
            flag = False
            break
        else:
            l = l+1
    n = n[0:(len(n)-l)]
    lastip  = n+"1"*(l-1)+"0"
    lastip = re.findall(r'.{8}',"".join(lastip))
    result=[]
    for i in lastip:
        result.append(str(binary_to_decimal(i)))
    return ".".join(result)
def get_ip_range(firstip,lastip):
    first = []
    last  = []
    for i in firstip.split('.'):
        first.append(i)
    for j in lastip.split('.'):
        last.append(j)
    one_range = ''
    two_range = ''
    three_range = ''
    four_range  = ''
    onelist=[]
    twolist=[]
    threelist=[]
    fourlist=[]
    if first[0] != last[0]:
        one_range = int(last[0]) - int(first[0])
        for one in range(one_range):
            onelist.append(str(int(first[0])+one))
    else:
        onelist = [first[0]]
    if first[1] != last[1]:
        two_range = int(last[1]) - int(first[1])
        for two in range(two_range):
            twolist.append(str(int(first[1])+two))
    else:
        twolist = [first[1]]
    if first[2] != last[2]:
        three_range = int(last[2]) - int(first[2])
        for three in range(three_range):
            threelist.append(str(int(first[2])+three))
    else:
        threelist = [first[2]]
    if first[3] != last[3]:
        four_range = int(last[3]) - int(first[3])
        for four in range(four_range):
            fourlist.append(str(int(first[3])+four))

    iplist=[]
    for i in onelist:
        for j in twolist:
            for k in threelist:
                for f in fourlist:
                    iplist.append(i+"."+j+"."+k+"."+f)
    return iplist
ip = raw_input('请输入IP(ex:192.168.1.1)：')
s = raw_input('请输入子网掩码(ex:255.255.255.0)：')

if validate_ip(ip) and validate_mask(s):
    r = calculate_ip_network(ip,s)
    bip = get_broadcast_addr(r,s)
    fip = get_first_ip(r,s)
    lip = get_last_ip(r,s)
    iprange = get_ip_range(fip,bip)
    s = '\n'
    for i in iprange:
        s += "%s\n"%i
    print "网络地址:%s"%r
    print "广播地址:%s"%bip
    print "起始地址:%s"%fip
    print "结束地址:%s"%lip
    print "可用地址:%s"%s
else:
    print "ip或子网掩码格式错误！"
