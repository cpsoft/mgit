import os
from xml.dom import minidom

class SubProject():
	def __init__(self, dom):
		self.dom=dom
		self.item = dom.createElement('SubProject')

		
