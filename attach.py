#!/usr/bin/env python
import os
from optparse import OptionParser
import project

configFilename = "./.mgit/project.xml"

class Attach():
	def __init__(self):
		self.parser = OptionParser()
		self.parser.set_usage("mgit attach <url>")

	def print_usage(self):
		self.parser.print_usage()

	def append_ignore_file(self, args):
		subdir = os.path.splitext(os.path.basename(args[0]))[0] if len(args) <= 1 else args[1] 
		ignoreFile = open(".gitignore", "wa")
		ignoreFile.write(subdir)
		ignoreFile.close()

	def get_config_dom(self):
		if os.path.exists(configFilename):
			dom = minidom.parse(configFilename)
		else:
			if not os.path.exists("./.mgit"):
				os.mkdir("./.mgit")
			impl = minidom.getDOMImplementation()
			dom = impl.createDocument(None, 'Project', None)
		return dom

	def save_config_dom(self, dom):
		f = open(configFilename, 'w');
		dom.writexml(f, addindent='\t', newl='\n')
		f.close()
		

	def run(self, args):
		options, args = self.parser.parse_args(args[1:])
		if len(args) <= 0:
			self.parser.print_usage()
			return
		self.cmd = ["git", "clone"]
		self.cmd += args
		cmd = " ".join(self.cmd)
		"""
		ret = os.system(cmd)
		if 0 != ret:
			return -1
		self.append_ignore_file(args)
		"""
		self.project = project.Project()
		self.project.get_sub_project(, new=False):
		self.project.save()

