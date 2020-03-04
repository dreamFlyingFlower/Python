'''
Created on 2020年2月28日

@author: wanyang
解析xml文件
'''
import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
root.findall("country") # 从根下查找所有的country标签
first=root.find("country")    # 只查找第一个country标签
root.remove(first)  # 删除某个标签,删除之后要调用write写入
# 遍历xml文档,xml有多少层就写多少层for循环,需要优化修改
for node1 in root:
    print(node1.tag, node1.attrib)
    for node2 in node1:
        print(node2.tag, node2.text,node2.attrib)   # 节点的标签,文档,属性
# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)
# 修改
for node in root.iter('year'):
    node.text = "2030"  # 修改文本内容
    node.set("attr1","343") # 设置属性
tree.write("xmltest.xml")   # 重新写入
# xml的生成
new_xml = ET.Element("personinfolist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
name.text = "paradise"
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
sex = ET.SubElement(personinfo, "sex")
age.text = '56'
personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
name.text = "Oldboy Ran"
age = ET.SubElement(personinfo2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式