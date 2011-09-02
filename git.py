#!/usr/bin/env python

import os
from xml.etree.ElementTree import Element

class Git():
	def __init__(self):
		self.git='git'
		return

	def clone(self, module):
		name = module.get('name')
		uri = module.get('uri')
		branch = module.get('branch')
		if name == None or uri == None:
			return -1
		cmd=[self.git, 'clone', uri, name, '-b', branch]
		os.system(" ".join(cmd))

	def current_branch(self):
		cmd = """git branch --no-color | grep '^\* ' | grep -v 'no branch' | sed 's/^* //g'"""
		return os.popen(cmd).read().strip()
		

	def current_remote_uri(self, branch=None, remote=None):
		if branch != None:
			branch = branch.strip()
			cmd = """git config --get branch.%s.remote""" % branch
			remote = os.popen(cmd).read().strip()
			if len(remote) > 0:
				cmd = """git config --get remote.%s.url""" % remote
				uri = os.popen(cmd).read().strip()
		if len(uri) > 0:
			cmd = """git config --get remote.origin.url"""
			uri = os.popen(cmd).read().strip()
		return uri

	def is_repo(self):
		cmd = """git rev-parse --git-dir >/dev/null 2>&1"""
		return os.system(cmd) == 0
	
	def module_name(self, uri):
		if uri == None or len(uri) <= 0:
			return None
		module=os.path.basename(uri.split(':')[-1])
		temp = os.path.splitext(module)
		return temp[0] if temp[-1] == ".git" else module

if __name__ == "__main__":
	git = Git()
	print git.is_repo()

