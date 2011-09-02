import os
from optparse import OptionParser
from project import Project
from sync import Sync
from git import Git

class Clone():
	def __init__(self):
		self.git = Git()
		self.parser = OptionParser()
		self.parser.add_option("-b", "--branch", dest="branch", help="with checkout branch")
		self.parser.add_option("-C", "--repo-dir", dest="repodir", help="repo directory")
		self.parser.add_option("-R", "--recursive", dest="recursive", help="clone project and subproject recursively")
		self.parser.set_usage("mgit clone <url> [-b <branch>]")

	def print_usage(self):
		self.parser.print_usage()
	
	def run(self, orig_args):
		options,args = self.parser.parse_args(orig_args)
		args = args[1:]
		if len(args) <= 0:
			self.print_usage()
			return
		project_dir = self.git.module_name(args[0])
		if project_dir == None or len(project_dir) <= 0:
			print("Unknow project name.Please use git clone, then use mgit sync in the project dir.")
			return
		cmd = ['git', 'clone'] + args
		if options.branch != None:
			cmd += ["-b", options.branch]
		if 0 != os.system(" ".join(cmd)):
			return
		cwd = os.getcwd()
		os.chdir("/".join([cwd, project_dir]))
		sync = Sync()
		sync.run(['sync'] + orig_args[1:])
		os.chdir(cwd)
