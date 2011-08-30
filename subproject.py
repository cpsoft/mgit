import os
from xml.etree.ElementTree import Element

class SubProject():
	def __init__(self, name):
		self.obj = Element('SubProject', {'name':name})

	def __setObj(self, obj):
		self.obj = obj

	def get(self, key):
		return self.obj.get(key)
	
	def set(self, key, value):
		return self.obj.set(key, value)

		
