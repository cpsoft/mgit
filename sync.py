import os
from optparse import OptionParser
from project import Project
from subproject import SubProject

class Sync():
	def __init__(self):
		self.parser = OptionParser()
		self.parser.add_option("-b", "--branch", dest="branch", help="with checkout branch")
		self.parser.add_option("-C", "--repo-dir", dest="repodir", help="repo directory")
		self.parser.add_option("-R", "--recursive", dest="recursive", help="sync project and subproject recursively")
		self.parser.set_usage("mgit sync")

	def print_usage(self):
		self.parser.print_usage()

	def func(self, subproject):
		cmd = ['git', 'clone', subproject.get("uri"), subproject.get("name")]
		branch = subproject.get("branch")
		if branch != None:
			cmd += ["-b", branch]
		os.system(" ".join(cmd))

	def run(self, args):
		self.options,args = self.parser.parse_args(args)
		cwd = os.getcwd()
		if self.options.repodir != None:
			os.chdir("/".join([cwd, self.options.repodir]))
		self.project = Project()
		for i in self.project.iter():
			self.func(i)
		os.chdir(cwd)
		