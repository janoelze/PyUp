---
CURRENTLY NOT WORKING
---

PyUp
=====

PyUp automatically uploads screenshots to [imgur.com](http://imgur.com/) and adds the image-URL to your clipboard. It uses OS X 10.8+'s Notification Center via ``pync``.

### Installation

PyUp needs the screenshots to be saved to a dedicated location other than the desktop, as it's uploading every file added to this folder. 
You can change the default location using these commands:


``` $ mkdir ~/pyup_screenshots/```<br>
``` $ defaults write com.apple.screencapture location ~/pyup_screenshots/```<br>
``` $ killall SystemUIServer ```

###Usage

``` $ python PyUp.py /path/to/screenshot/folder/```
