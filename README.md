PyUp
=====

PyUp automatically uploads screenshots to [imgur.com](http://imgur.com/) and adds the image-URL to your clipboard.

###Usage

``` $ python PyUp.py /path/to/screenshot/folder/```

PyUp needs the screenshots to be saved to a dedicated location other than the desktop, as it's uploading every file added to this folder. 
You can change the default location using these commands:


``` $ mkdir ~/pyup_screenshots/```<br>
``` $ defaults write com.apple.screencapture location ~/pyup_screenshots/```<br>
``` $ killall SystemUIServer ```
