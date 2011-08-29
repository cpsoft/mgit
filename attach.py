#!/usr/bin/env python
from optparse import OptionParser

class Attach():
	def __init__(self):
		self.parser = OptionParser()
		self.parser.set_usage("%prog <url>")

	def print_usage(self):
		self.parser.print_usage()

def main():
	attach = Attach()
	attach.print_usage()

if __name__ == "__main__":
	main()
