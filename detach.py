#!/usr/bin/env python
import os
from optparse import OptionParser
from project import Project
from git import Git

class Detach():
	def __init__(self):
		self.git = Git()
		self.parser = OptionParser()
		self.parser.set_usage("mgit attach <subproject name>")

	def print_usage(self):
		self.parser.print_usage()

	def run(self, args):
		options, args = self.parser.parse_args(args[1:])
		if len(args) <= 0:
			self.parser.print_usage()
			return

		if len(args) > 1:
			module = args[1]
		else:
			module = self.git.module_name(args[0])
		if module == None or len(module) <= 0:
			return

		if not os.path.exists(module):
			print("module %s not exists." % module)
			return
		project = Project()
		project.remove(module)
