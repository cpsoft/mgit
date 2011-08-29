import sys

class ArgParser():
	def __init__(self, usage, version):
		self.usage = usage
		self.version = version

	def parse(self, args):
		l = len(args)
		if l <= 1:
			print self.usage
			sys.exit(-1)
		else:
			cmd = args[1]
			arg = args[1:]
		return cmd, arg

	def print_usage(self):
		print self.usage 
		

