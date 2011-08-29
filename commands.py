
import attach

class Commands():
	cmds={"attach":lambda:attach.Attach()}
	def __init__(self, cmd_name):
		self.cmd = self.cmds[cmd_name]()

	def print_usages(self):
		for k,v in self.cmds.items():
			if v:
				v().print_usage()
	
	def run(self, args):
		if not self.cmd:
			return;
		self.cmd.run(args)
