import os.path, time, sys, commands, inspect
from xml.dom.minidom import parse, parseString

uploaded_files = []
folder_to_watch = sys.argv[1]
upload = False

print 'Hej. PyUp is now watching: %s!' % folder_to_watch

def copy(url):
	commands.getstatusoutput('echo "%s" | pbcopy' % url.strip())
	commands.getstatusoutput("osascript -e 'tell app \"System Events\" to display dialog \"Upload complete!\"' ")

def upload_file(filepath):
	api_key = "47e4f6aa03fa0defcaa68bf188d8026e"
	output = os.popen('curl -F "image=@%s" -F "key=%s" http://api.imgur.com/2/upload.xml' % ( filepath, api_key ))
	for node in parse(output).getElementsByTagName('original'):
		copy(node.toxml()[10:-11])

while upload != True:
	for filename in os.listdir(folder_to_watch):
		file_created_at = os.path.getmtime(folder_to_watch + '/' + filename)
		if (time.time() - file_created_at) < 4:
			if filename not in uploaded_files:
				upload_file(folder_to_watch + filename)
				uploaded_files.append(filename)
	time.sleep(1)
