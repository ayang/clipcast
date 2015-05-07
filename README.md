# Clipcast

Clipboard share tool in LAN via UDP broadcast for multiple computer users. datas are encrypted by rc4.

**This Project will not be maintenanced, Now I use another tool which is also developed by me,  https://github.com/ayang/sendclip.**
# Usage

Modify `config.py` as you like.

Run `clipserver.py start` as a daemon for reciving clipboard text. Run `sendclip.py` to send current clipboard text to every machine in LAN. Only servers with same `username` config will recieve the clipboard.

You can make an soft link in your PATH to `sendclip.py` or add an alias to it for simple. I have not found a method to make a short key to run a script.

# Installation

This program is tested under python 2.7, ubuntu 14.04 and osx 10.9.

## OSX

1. Copy brc.clipserver.plist to `~/Library/LaunchAgent/brc.clipserver.plist`
2. Edit `~/Library/LaunchAgent/brc.clipserver.plist`, modify `/Path/to/clipcast/clipserver.py` to your `clipserver.py` path.
3. `launchctl load ~/Library/LaunchAgent/brc.clipserver.plist`
4. `launchctl start brc.clipserver`

## Ubuntu (Gnome or Unity)

1. run `gnome-session-properties`
2. Add a startup program, Name is "Clipserver", Command is "/Path/to/clipcast/clipserver.py start"
3. Save. Clipserver will start in your next gnome session.
