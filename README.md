# siftap-py
Basically just holds open an ADB shell running [minitouch](https://github.com/openstf/minitouch) to allow you to quickly hack together fun things that tap on an Android device

Example included: a Discord bot to do a "Discord plays SIF" thing

## Preparation

First get minitouch and put the file in the same folder as these scripts, the scripts will automatically upload and start it. Easiest way is to grab then [prebuilt minitouch package from npm](https://www.npmjs.com/package/minitouch-prebuilt-beta) and just grabbing the binary from there.

Then you probably have to change the coordinates at the top of ``siftap.py``.

There's a simple test thing reading digits from the command line if you run ``siftap.py`` directly, to test your positions. After that just import the ``siftap`` module in anything you want and go ham.
