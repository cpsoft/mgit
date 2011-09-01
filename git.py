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
			cmd = """git config --get branch.%s.remote""" % branch
			remote = os.popen(cmd).read()
			if remote != None:
				cmd = """git config --get remote.%s.url""" % remote.strip()
				uri = os.popen(cmd).read()
		if uri == None:
			cmd = """git config --get remote.origin.url"""
			uri = os.popen(cmd).read()
		return uri.strip()

	def is_repo(self):
		cmd = """git rev-parse --git-dir >/dev/null 2>&1"""
		return os.system(cmd) == 0

if __name__ == "__main__":
	git = Git()
	print git.is_repo()

