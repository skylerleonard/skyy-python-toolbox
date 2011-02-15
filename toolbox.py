#!/usr/bin/env python
"""
Here are a couple of scripts free to use.
  Copyright (C) 2011  Skyler Leonard, 
 
  These programs are free software: you can redistribute them and/or modify
  them under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
 
  These programs are distributed in the hope that they will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
  GNU General Public License for more details.
 
  You should have received a copy of the GNU General Public License
  along with these programs.  If not, see <http://www.gnu.org/licenses/>.
"""
 
"""
Indents are four spaces.
Any definition more than one line in length should have a docstring. (excl. __init__, etc.)
"""
 
class Lambda:
	"""Anonymous class declaration - with a L"""
	def __init__(self, **entries): self.__dict__.update(entries)
 
"""-------------------------------------------------------------"""
 
class Switch(object):
	"""A switch / case object"""
	def __init__(self):
		self.cases = {}
		def error():
			raise ValueError("No default for the tested case.")
		self.default = error
	def case(self, value, function):
		"""Make a new case for the switch"""
		self.cases[value] = function
	def default(self, function):
		"""Set the default option."""
		self.default = function
	def run(self, test_value):
		"""Run the switch"""
		try:
			self.cases[test_value]()
		except KeyError:
			self.default()
 
"""-------------------------------------------------------------"""
 
def add(*p):
	"""Add numbers together"""
	n = 0
	for i in p: n += i
	return n
 
"""-------------------------------------------------------------"""
 
def auto_socket(HOST, PORT):
	"""Automatically connect to a server"""
	s = None
	for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
		af, socktype, proto, canonname, sa = res
		try:
			s = socket.socket(af, socktype, proto)
		except socket.error as msg:
				s = None
				continue
		try:
				s.connect(sa)
		except socket.error as msg:
			s.close()
			s = None
				continue
		return s
 
"""-------------------------------------------------------------"""
 
# Geometry objects
 
class Geometry(object):
	"""base geometry object"""
	pass
 
class Point(Geometry):
	"""Geometry Point object"""
	def __init__(self, x, y):
		super(Point, self).__init__()
		self.x, self.y = x, y
	def __repr__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"
	#def __
 
# End Geometry objects
 
def adding_primes(bound=10):
	return [ sum(l)+1 for l in [[x for x in range(i+1)] for i in range(bound)]]