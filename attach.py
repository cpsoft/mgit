#!/usr/bin/env python
import os
from optparse import OptionParser
from project import Project
from subproject import SubProject

configFilename = "./.mgit/project.xml"

class Attach():
	def __init__(self):
		self.parser = OptionParser()
		self.parser.set_usage("mgit attach <subproject name>")

	def print_usage(self):
		self.parser.print_usage()

	def append_ignore_file(self, submodule):
		print submodule
		ignoreFile = open(".gitignore", "wa")
		for line in ignoreFile:
			if submodule == line[0:len(submodule)]:
				return
		ignoreFile.write(submodule)
		ignoreFile.close()
	
	def append_project_file(self, submodule, uri):
		self.project = Project()
		subproject = SubProject(submodule)
		subproject.set("uri", uri)
		self.project.append(subproject)
		self.project.save()

	def run(self, args):
		options, args = self.parser.parse_args(args[1:])
		if len(args) <= 0:
			self.parser.print_usage()
			return
	
		submodule = os.path.splitext(os.path.basename(args[0]))[0] if len(args) <= 1 else args[1]
		if not os.path.exists(submodule):
			print submodule+" not exists"
			return

		self.subproject = SubProject(submodule)
		
		self.append_ignore_file(submodule)
		self.append_project_file(submodule, args[0])	
		
		cmd = ["git", "clone"]
		cmd += args
		cmd = " ".join(cmd)
		
		ret = os.system(cmd)
		if 0 != ret:
			return -1

