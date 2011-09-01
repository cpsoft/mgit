#!/usr/bin/env python
import os
from optparse import OptionParser
from project import Project

class Clean():
	def __init__(self):
		self.parser = OptionParser()
		self.parser.set_usage("mgit clean")

	def print_usage(self):
		self.parser.print_usage()

	def run(self, args):
		project = Project()
		project.remove()		
		os.system('rm -rf .mgit')
		

