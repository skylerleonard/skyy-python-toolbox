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

# Imports:
import random , string , getopt


"""-------------------------------------------------------------"""
 
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

"""-------------------------------------------------------------"""
 
def adding_primes(bound=10):
	return [ sum(l)+1 for l in [[x for x in range(i+1)] for i in range(bound)]]
	
"""-------------------------------------------------------------"""

class Colors(object):
	"""Class for creating ansi colored text out of CSS-like readable strings
	
	Note that it is not meant to be very cross platform, more just to let strings be more human readable."""
	def __init__(self):
		# Basic Colors
		self.colors =  {"gray" : "7",
						"black" : "0",
						"red" : "1",
						"green" : "2",
						"yellow" : "3",
						"blue" : "4",
						"purple" : "5",
						"cyan" : "6"}
		# Modifiers
		self.bright = "1"
		self.blink = "5" 
		self.sep = ";"
		self.background = "4"
		self.foreground = "3"
		# Part of the esc seq
		self.esc = "\033"
		self.pre = "["
		self.prefix = self.esc + self.pre
		self.postfix = "m"
		# Normalize
		self.normal = self.prefix + '0' + self.postfix
	def __getitem__(self, key):
		try:
			if key in ("normal", "normal;"): return self.normal
			string = self.prefix
			if "bright;" == key[:7]:
				string += self.bright + self.sep
				key = key[7:]
			if "blink;" == key[:6]:
				string += self.blink + self.sep
				key = key[6:]
			if "background:" == key[:11]:
				end_color = key.index(";", 11)
				color = key[11:end_color]
				string += self.background + self.colors[color] + self.sep
				key = key[end_color+1:]
			if "foreground:" == key[:11]:
				end_color = key.index(";", 11)
				color = key[11:end_color]
				string += self.foreground + self.colors[color] + self.sep
				key = key[end_color+1:]
			if key:
				raise KeyError
			string = string[:-1]
			string += self.postfix
			return string
		except Exception:
			raise KeyError("Invalid Key.")
		
"""-------------------------------------------------------------"""

def random_sort(l):
	"""Sort a list randomly"""
	nl = []
	length = len(l)
	for i in range(length):
		nl.append(l.pop(random.randrange(len(l))))
	return nl

"""-------------------------------------------------------------"""

def randstr(length, letters=string.printable):
	"""print a random string"""
	s = ""
	for i in range(length):
		s += random.choice(letters)
	return s
	
"""-------------------------------------------------------------"""

class ManyFunction(object):
	"""Call many functions with the same arguments"""
	def __init__(self, *functions):
		self.functions = functions
	def __call__(self, *args):
		results = ()
		for function in self.functions:
			results += function(*args),
		return results

"""-------------------------------------------------------------"""

class Curses_screen:
	"""Nice curses screen for use in 'with' statements.
	
	https://www.ironalbatross.net/wiki/index.php5?title=Python_Curses"""
    def __enter__(self):
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(1)
        return self.stdscr
    def __exit__(self,a,b,c):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

"""-------------------------------------------------------------"""

def biasedRandom(lo, hi, target, steps=1):
    if lo >= hi:
        raise ValueError("lo should be less than hi")
    elif target < lo or target >= hi:
        raise ValueError("target not in range(lo, hi)")
    else:
        num = random.randint(lo, hi)
        for i in range(steps):
            num += int(random.random() * (target - num))
        return num

"""-------------------------------------------------------------"""

class Instaopts(options):
	"""docstring for instaopts
	
	depends: getopt, string"""
	def __init__(self, options):
		self.options = options
		self.__checkoptions()
		self.shorts = self.__makeshort()
	def __checkoptions(self):
		"""Make sure all options are strings and not empty."""
		for opt in self.options:
			if not isinstance(opt, str) and opt:
				raise ValueError("Invalid Option: %s" % repr({opt: self.options[opt]}))
	def __makeshort(self):
		shorts = {}
		for name in self.options:
			yes = False
			for let in name:
				if let in shorts:
					continue
				else:
					shorts[let] = name
					yes = True
			if not yes:
				for let in string.ascii_lowercase:
					if let in shorts:
						continue
					else:
						shorts[let] = name
						yes = True
			if not yes:
				raise ValueError("Too many options!")
		return shorts
	def __condensed(self):
		bools = values = ""
		for short in self.shorts:
			if self.options[self.shorts[short]] in (True, False):
				bools += short
			else:
				values += short
		for short in bools:
			pass
	def check(self, args):
		"""Check args and return a new dict"""
		getopt

"""-------------------------------------------------------------"""

def bytes_from_human_readable(string):
	string = string.lower()
	units = ["k", "m", "g"]
	if string[-1] == "b":
		string = string[:-1]
	if not string[-1] in units:
		try:
			return int(string)
		except ValueError:
			raise ValueError("Invalid Size String")
	try:
		return int(string[:-1]) * (KILOBYTESIZE ** ((units.index(string[-1])) + 1))
	except ValueError:
		raise ValueError("Invalid Size String")

"""-------------------------------------------------------------"""
