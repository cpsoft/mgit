#!/usr/bin/env python
import os
from optparse import OptionParser
from project import Project
from subproject import SubProject
from gitconfig import GitConfig

class Attach():
	def __init__(self):
		self.parser = OptionParser()
		self.parser.set_usage("mgit attach <subproject name>")

	def print_usage(self):
		self.parser.print_usage()

	def append_ignore_file(self, submodule):
		if os.path.exists(".gitignore"):
			ignoreFile = open(".gitignore","r")
			for line in ignoreFile:
				if submodule == line.strip():
					return
			ignoreFile.close()
		ignoreFile = open(".gitignore", "a")
		ignoreFile.write(submodule + "\n")
		ignoreFile.close()
	
	def append_project_file(self, submodule):
		self.project = Project()
		subproject = SubProject(submodule)
		gitconf = GitConfig(submodule)
		subproject.set("uri", gitconf.uri())
		subproject.set("branch", gitconf.branch())
		self.project.append(subproject)
		self.project.save()

	def run(self, args):
		options, args = self.parser.parse_args(args[1:])
		if len(args) <= 0:
			self.parser.print_usage()
			return
	
		if len(args) > 1:
			submodule = args[1]
		else:
			submodule = os.path.basename(args[0])
			test = os.path.splitext(submodule)
			if len(test) > 1 and test[1] == ".git":
				submodule=test[0]

		if not os.path.exists(submodule):
			print(submodule+" not exists")
			return

		self.subproject = SubProject(submodule)
		
		self.append_ignore_file(submodule)
		self.append_project_file(submodule)	
