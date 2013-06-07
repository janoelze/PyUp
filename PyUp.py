#!/usr/bin/python

import os.path, time, sys, commands, inspect
from xml.dom.minidom import parse, parseString
from pync import Notifier

UPLOADED_FILES = []
try:
	TARGET_FOLDER = sys.argv[1]
except:
	raise ValueError('You must specify a screenshots folder.')  
IMGUR_API_KEY = "47e4f6aa03fa0defcaa68bf188d8026e"

def copy(url):
	commands.getstatusoutput("echo '"+url.strip()+"' | tr -d '\n' | pbcopy")
	Notifier.notify('Copied ' + url, title='PyUp: Upload complete!', open=url)


def upload_file(filepath):
	output = os.popen('curl -F "image=@%s" -F "key=%s" http://api.imgur.com/2/upload.xml' % ( filepath, IMGUR_API_KEY ))
	for node in parse(output).getElementsByTagName('original'):
		copy(node.toxml()[10:-11])

def main():
	print 'Hej. PyUp is now watching: "%s"!' % TARGET_FOLDER
	while True:
		for filename in os.listdir(TARGET_FOLDER):
			file_created_at = os.path.getmtime(TARGET_FOLDER + '/' + filename)
			if (time.time() - file_created_at) < 4:
				if filename not in UPLOADED_FILES:
					upload_file(TARGET_FOLDER + filename)
					UPLOADED_FILES.append(filename)
		time.sleep(1)

if __name__ == '__main__':
	main()
