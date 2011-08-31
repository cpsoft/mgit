import os
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from subproject import SubProject

PROJECT_CONFIG_PATH="./.mgit"
PROJECT_CONFIG_FILE=PROJECT_CONFIG_PATH + "/project.xml"

class Project():
	def __init__(self):
		self.tree = ElementTree();
		if not os.path.exists(PROJECT_CONFIG_PATH):
			os.mkdir(PROJECT_CONFIG_PATH)
		try:
			self.tree.parse(PROJECT_CONFIG_FILE)
		except:
			root = Element('Project', {'name':os.path.basename(os.getcwd())})
			self.tree._setroot(root)

	def save(self):
		self.tree.write(PROJECT_CONFIG_FILE, xml_declaration=True, method="xml")

	def find(self, name):
		for i in self.tree.iter('SubProject'):
			if i.get('name') == name:
				return i

	def append(self, subproject):
		if subproject == None or subproject.obj == None:
			return
		node = self.find(subproject.get('name'))
		root = self.tree.getroot()
		if node != None:
			root.remove(node)
		root.append(subproject.obj)

	def iter(self):
		subproject = SubProject()
		for i in self.tree.iter('SubProject'):
			subproject._setObj(i)
			yield subproject

	def inSubProject(self, cmd):
		cwd = os.getcwd()
		for i in self.iter():
			print("On:" + i.get("name") + ":")
			os.chdir("/".join([cwd, i.get("name")]))
			cmd.func(i)
			
