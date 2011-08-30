import os
from optparse import OptionParser
from project import Project
from subproject import SubProject

class Default():
	def __init__(self):
		return

	def print_usage(self):
		return

	def func(self, subproject):
		cmd = ['mgit'] + self.args
		os.system(" ".join(cmd))
	
	def run(self, args):
		for i in xrange(0, len(args)):
			if args[i].find(" ") > 0:
				args[i]="\"%s\"" % args[i]
		self.args = args
		self.project = Project()
		cmd = ['git'] + self.args
		os.system(" ".join(cmd))
		self.project.inSubProject(self)
