import os
from optparse import OptionParser
from project import Project
from subproject import SubProject

class Clone():
	def __init__(self):
		self.parser = OptionParser()
		self.parser.add_option("-b", "--branch", dest="branch", help="with checkout branch")
		self.parser.add_option("-C", "--repo-dir", dest="repodir", help="repo directory")
		self.parser.add_option("-R", "--recursive", dest="recursive", help="clone project and subproject recursively")
		self.parser.set_usage("mgit clone <url> [-b <branch>]")

	def print_usage(self):
		self.parser.print_usage()
	
	def run(self, args):
		options,args = self.parser.parse_args(args)
		args = args[1:]
		if len(args) <= 0:
			self.print_usage()
			return
		cwd = os.path.splitext(os.path.basename(args[0]))[0] if len(args) <= 1 else args[1]
		cmd = ['git', 'clone'] + args
		if options.branch != None:
			cmd += ["-b", options.branch]
		if 0 != os.system(" ".join(cmd)):
			return
		cmd = ['mgit', 'sync', "-C", cwd]
		if 0 != os.system(" ".join(cmd)):
			return
