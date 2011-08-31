#!/usr/bin/env python

import os

class GitConfig():
	data={}
	head={}
	params={}

	def __addparams(self):
		if self.head != None:
			if len(self.head) == 1:
				self.data[self.head[0]] = self.params
			elif len(self.head) == 2:
				subhead={}
				subhead[self.head[1].strip("\"")]=self.params
				self.data[self.head[0]]=subhead
			self.params={}

		
	def __init__(self, module):
		head=None
		for i in open(module + "/.git/config", "r"):
			i = i.strip()
			if len(i) == 0:
				continue
			if i[0] == '[':
				self.__addparams()
				i = i.strip("[]")
				self.head = i.split(" ")
				continue
			param = i.split(" ")
			self.params[param[0]]=param[2]
		self.__addparams()
		self.params=None
		self.head=None
		#print self.data

	def branch(self):
		branchs = self.data["branch"]
		return list(branchs.keys())[0]

	def uri(self):
		branchs = self.data["branch"]
		branch = branchs[list(branchs.keys())[0]]
		remotes = self.data["remote"]
		return remotes[branch["remote"]]["url"]

if __name__ == "__main__":
	gconf = GitConfig("this")
	print(gconf.branch())
	print(gconf.uri())
