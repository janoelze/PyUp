#!/usr/bin/env python
# -*- coding: utf8 -*-

import os.path
import time
import sys
import commands
import inspect
from xml.dom.minidom import parse, parseString
from pync import Notifier


class PyUp(object):

    def __init__(self, arg):
        self.IMGUR_API_KEY = "47e4f6aa03fa0defcaa68bf188d8026e"
        self.UPLOADED_FILES = []

    def start(self, TARGET_FOLDER):
        self.TARGET_FOLDER = TARGET_FOLDER
        print 'Hej. PyUp is now watching: "%s"!' % self.TARGET_FOLDER
        while True:
            for filename in os.listdir(TARGET_FOLDER):
                if (time.time() - os.path.getmtime(self.TARGET_FOLDER + '/' + filename)) < 4:
                    if filename not in self.UPLOADED_FILES:
                        upload_file(TARGET_FOLDER + '/' + filename)
                        self.UPLOADED_FILES.append(filename)
            time.sleep(1)

    def copy(self, url):
        commands.getstatusoutput( "echo '%s' | tr -d '\n' | pbcopy" % url.strip() )
        Notifier.notify( 'Copied ' + url, title='PyUp: Upload complete!', open=url )

    def upload_file(self, filepath):
        output = os.popen('curl -F "image=@%s" -F "key=%s" http://api.imgur.com/2/upload.xml' % ( filepath, self.IMGUR_API_KEY ) ).read()
        for node in parseString(output).getElementsByTagName('original'):
            copy(node.toxml()[10:-11])
