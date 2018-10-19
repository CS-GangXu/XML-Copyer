#!/usr/bin/python
# -*- coding: UTF-8 -*-
sadsasa
222
import os
import xml.dom.minidom

source_Path = '/home/xg/桌面/工程/Git/XML-Copyer/source.xml' # 提供素材的xml文件地址
need_Path = '/home/xg/桌面/工程/Git/XML-Copyer/need.xml' # 需要素材的xml文件地址
des_Path = '/home/xg/桌面/工程/Git/XML-Copyer/des.xml' # 最后生成的xml文件地址

def xml_Reader(source_Path):
    DOMTree = xml.dom.minidom.parse(source_Path) # 得到xml引用
    source_Xml = DOMTree.documentElement # 得到xml对象
    return source_Xml.getElementsByTagName('object') # 返回所有的‘object'迭代器对象

def xml_Appender(need_Path,source_Objs):
    DOMTree = xml.dom.minidom.parse(need_Path)
    need_Xml = DOMTree.documentElement
    need_Objs = need_Xml.getElementsByTagName('object')
    for source_Obj in source_Objs: # 对‘object’迭代器对象中依次遍历每一个Node节点
        need_Xml.appendChild(source_Obj)  # 添加字节点
    return need_Xml

def xml_Writer(des_Path,des_Xml):
    fileHandle = open(des_Path,'w') # 得到文件引用
    #des_Xml.writexml(fileHandle, addindent="   ", newl="\n")
    fileHandle.write(des_Xml.toxml()) # 写入文件
    fileHandle.close() # 关闭文件引用
    return

source_Objs = xml_Reader(source_Path)
des_Xml = xml_Appender(need_Path,source_Objs)
xml_Writer(des_Path,des_Xml)
print 'change complete'
print os.path.realpath(__file__)
