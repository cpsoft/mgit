import os
from xml.dom import minidom
import subproject

PROJECT_CONFIG_PATH="./.mgit"
PROJECT_CONFIG_FILE=PROJECT_CONFIG_PATH + "/project.xml"

class Project():
	def __init__(self):
		if os.path.exists(PROJECT_CONFIG_FILE):
			self.dom = minidom.parse(PROJECT_CONFIG_FILE)
		else:
			if not os.path.exists(PROJECT_CONFIG_PATH):
				os.mkdir(PROJECT_CONFIG_PATH)
			impl = minidom.getDOMImplementation()
			self.dom = impl.createDocument(None, 'Project', None)

	def save(self):
		f = open(PROJECT_CONFIG_FILE, 'w');
		self.dom.writexml(f, addindent='\t', newl='\n')
		f.close()

	def get_sub_project(self, name, new=False):
		for item in self.dom.getElementByTagName("SubProject"):
			if item.getAttribute("name") == name:
				print item
