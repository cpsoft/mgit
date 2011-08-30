import os
from optparse import OptionParser
from project import Project
from subproject import SubProject

class Default():
	def __init__(self):
		self.parser = OptionParser()
		self.parser.add_option("-C", "--repo-dir", dest="repodir", help="repo directory")
		self.parser.set_usage("mgit <command>")

	def print_usage(self):
		self.parser.print_usage()
	
	def func(self, subproject):
		cmd = ['mgit'] + self.args
		os.system(" ".join(cmd))
	
	def run(self, args):
		self.options,self.args = self.parser.parse_args(args)
		cwd = os.getcwd()
		if self.options.repodir != None:
			os.chdir("/".join([cwd, self.options.repodir]))
		cmd = ['git'] + self.args
		cmd = " ".join(cmd)
		os.system(cmd)

		self.project = Project()
		self.project.inSubProject(self)
		os.chdir(cwd)
		
