ImgUp
=====

PyUp automatically uploads screenshots to [imgur.com](http://imgur.com/) and adds the image-URL to the clipboard.

###Usage

``` $ python PyUp.py /path/to/screenshot/folder/```

PyUp needs the screenshots to be saved to a dedicated location other than the desktop, as it's uplaoding every file added to this folder. 
You can change the default location using this command:


``` $ mkdir ~/pyup_screenshots/```<br>
``` $ defaults write com.apple.screencapture location ~/pyup_screenshots/```
