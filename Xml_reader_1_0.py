#coding=utf-8
import  xml.dom.minidom
# xml reader version 1.0
sadsadsdsa
#open the xml document
dom = xml.dom.minidom.parse('movie.xml')

#get the xml object
root = dom.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE
111
111
'''
print "*****Object*****"
object_Type = sub_Object.getElementsByTagName('name')[0]
print "Type: %s" % object_Type.childNodes[0].data

format = movie.getElementsByTagName('format')[0]
   print "Format: %s" % format.childNodes[0].data
   rating = movie.getElementsByTagName('rating')[0]
   print "Rating: %s" % rating.childNodes[0].data
   description = movie.getElementsByTagName('description')[0]
   print "Description: %s" % description.childNodes[0].data
'''

'''
# 使用minidom解析器打开 XML 文档 Element 对象 Attribute 注解 TagName 标签
DOMTree = xml.dom.minidom.parse("/home/xg/桌面/工程/XML Copyer/test2.xml") # xml index
xml_Object = DOMTree.documentElement # xml object
if xml_Object.hasAttribute("shelf"):
   print "Root element: %s" % xml_Object.getAttribute("shelfx")

# 在集合中获取所有电影的迭代器
movies = xml_Object.getElementsByTagName("movie")
 
# 打印每部电影的详细信息
for movie in movies:
   print "*****Movie*****"
   if movie.hasAttribute("title"):
      print "Title: %s" % movie.getAttribute("title")
 
   type = movie.getElementsByTagName('type')[0]
   print "Type: %s" % type.childNodes[0].data
   format = movie.getElementsByTagName('format')[0]
   print "Format: %s" % format.childNodes[0].data
   rating = movie.getElementsByTagName('rating')[0]
   print "Rating: %s" % rating.childNodes[0].data
   description = movie.getElementsByTagName('description')[0]
   print "Description: %s" % description.childNodes[0].data
'''
