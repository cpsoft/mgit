
from attach import Attach
from detach import Detach
from clean import Clean
from sync import Sync
from clone import Clone
from default import Default

class Commands():
	cmds={"attach":lambda:Attach(),
		"detach":lambda:Detach(),
		"clean":lambda:Clean(),
		"sync":lambda:Sync(),
		"clone":lambda:Clone()
		}
	def __init__(self, cmd_name):
		if cmd_name in self.cmds.keys():
			self.cmd = self.cmds[cmd_name]()
		else:
			self.cmd = Default()
	
	def print_usages(self):
		for k,v in self.cmds.items():
			if v:
				v().print_usage()
	
	def run(self, args):
		if not self.cmd:
			return;
			
		self.cmd.run(args)
