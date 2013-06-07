import os.path, time, sys, commands, inspect
from xml.dom.minidom import parse, parseString

UPLOADED_FILES = []
TARGET_FOLDER = sys.argv[1]
IMGUR_API_KEY = "47e4f6aa03fa0defcaa68bf188d8026e"

print 'Hej. PyUp is now watching: %s!' % TARGET_FOLDER

def copy(url):
	commands.getstatusoutput('echo "%s" | pbcopy' % url.strip())
	commands.getstatusoutput("osascript -e 'tell app \"System Events\" to display dialog \"Upload complete!\"' ")

def upload_file(filepath):
	
	output = os.popen('curl -F "image=@%s" -F "key=%s" http://api.imgur.com/2/upload.xml' % ( filepath, IMGUR_API_KEY ))
	for node in parse(output).getElementsByTagName('original'):
		copy(node.toxml()[10:-11])

while True:
	for filename in os.listdir(TARGET_FOLDER):
		file_created_at = os.path.getmtime(folder_to_watch + '/' + filename)
		if (time.time() - file_created_at) < 4:
			if filename not in UPLOADED_FILES:
				upload_file(TARGET_FOLDER + filename)
				UPLOADED_FILES.append(filename)
	time.sleep(1)
