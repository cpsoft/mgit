import os
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from git import Git

PROJECT_CONFIG_PATH="./.mgit"
PROJECT_CONFIG_FILE=PROJECT_CONFIG_PATH + "/project.xml"

class Project():
	def __init__(self):
		self.tree = ElementTree();
		self.git = Git()
		if not os.path.exists(PROJECT_CONFIG_PATH):
			os.mkdir(PROJECT_CONFIG_PATH)
		try:
			self.tree.parse(PROJECT_CONFIG_FILE)
		except:
			root = Element('Project', {'name':os.path.basename(os.getcwd())})
			self.tree._setroot(root)

	def save(self):
		self.tree.write(PROJECT_CONFIG_FILE, xml_declaration=True, method="xml")

	def iter(self):
		return self.tree.iter('SubProject')

	def find(self, name):
		for i in self.iter():
			if i.get('name') == name:
				return i

	def inSubProject(self):
		cwd = os.getcwd()
		for node in self.iter():
			name = node.get('name')
			print("")
			print("On:%s" % name)
			print("***************************************")
			os.chdir("/".join([cwd, name]))
			yield
			print("***************************************")

	def clone(self):
		for module in self.iter():
			self.git.clone(module)

	def __init_module(self, module):
		if not os.path.exists(module):
			print("module %s not exists." % module)
			return None
		cwd = os.getcwd()
		os.chdir("/".join([cwd, module]))
		if self.git.is_repo():
			node = Element('SubProject')
			node.set("name", module)
			current_branch = self.git.current_branch()
			if current_branch != None:
				node.set("branch", current_branch)
			remote_uri = self.git.current_remote_uri(branch=current_branch)
			if remote_uri != None:
				node.set("uri", remote_uri)
			else:
				node = None
		else:
			print("fatal: Not a git repository")
			node = None
				
		os.chdir(cwd)
		return node

	def __append_ignore_file(self, module):
		if os.path.exists(".gitignore"):
			ignoreFile = open(".gitignore","r")
			for line in ignoreFile:
				if module == line.strip():
					return
			ignoreFile.close()
		ignoreFile = open(".gitignore", "a")
		ignoreFile.write(module + "\n")
		ignoreFile.close()

	def __remove_ignore_file(self, modules):
		if os.path.exists(".gitignore"):
			ignoreFile = open(".gitignore","r")
			print modules
			data = [line.strip() for line in ignoreFile if not (line.strip() in modules)]
			ignoreFile = open(".gitignore", "w")
			ignoreFile.write("\n".join(data))
			ignoreFile.close()
			data = None


	def append(self, module):
		if module == None:
			return -1
		node = self.find(module)
		root = self.tree.getroot()
		if node != None:
			root.remove(node)
		node = self.__init_module(module)
		if node == None:
			return -1
		else:
			root.append(node)
			self.__append_ignore_file(module)
		self.save()
		return 0

	def remove(self, module=None):
		if module != None:
			node = self.find(module)
			root = self.tree.getroot()
			if node != None:
				root.remove(node)
				self.__remove_ignore_file(module)
				self.save()
		else:
			data = [node.get('name') for node in self.iter()]
			self.__remove_ignore_file(data)
