#!/usr/bin/env python
import os
from optparse import OptionParser
from project import Project

class Detach():
	def __init__(self):
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
			module = os.path.basename(args[0])
			test = os.path.splitext(module)
			if len(test) > 1 and test[1] == ".git":
				module=test[0]
		if not os.path.exists(module):
			print("module %s not exists." % module)
			return
		project = Project()
		project.remove(module)
