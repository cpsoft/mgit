import os
from optparse import OptionParser
from project import Project

class Default():
	def __init__(self):
		return

	def print_usage(self):
		return

	def run(self, args):
		for i in range(0, len(args)):
			if args[i].find(" ") > 0:
				args[i]="\"%s\"" % args[i]
		self.args = args
		self.project = Project()
		cmd = ['git'] + self.args
		os.system(" ".join(cmd))
		for i in self.project.inSubProject():
			cmd = ['mgit'] + self.args
			os.system(" ".join(cmd))
