import sublime
import sublime_plugin
from base64 import b64encode
import re
from sys import exit

class HrefToB64Command(sublime_plugin.TextCommand):
	def run(self, edit):
		# all the href in the file
		hrefRegions = self.view.find_all('href="([^"]*)"')[::-1]

		# once we get all the regions
		# we loop on them
		for href in hrefRegions:
			# the full text (href="...")
			text = self.view.substr(href)

			# the link in the text
			link = re.match('href="([^"]*)"', text).group(1)

			# the link base64 encoded
			link = str(b64encode(bytes(link, 'utf-8')), 'utf-8')

			# the final href encoded
			finalHref = 'href="'+link+'"'

			# the replace
			self.view.replace(edit, href, finalHref)
		
