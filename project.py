import os
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import subproject

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
			print os.path.basename(os.getcwd())
			root = Element('Project', {'name':os.path.basename(os.getcwd())})
			self.tree._setroot(root)

	def save(self):
		self.tree.write(PROJECT_CONFIG_FILE, xml_declaration=True, method="xml")
		#self.tree.write(PROJECT_CONFIG_FILE, method="xml")

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
