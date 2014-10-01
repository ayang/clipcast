# Clipcast

Clipboard share tool in LAN via UDP broadcast for multiple computer users. datas are encrypted by rc4.

# Usage

Modify `config.py` as you like.

Run `clipserver.py start` as a daemon for reciving clipboard text. Run `sendclip.py` to send current clipboard text to every machine in LAN. Only servers with same `username` config will recieve the clipboard.

You can make an soft link in your PATH to `sendclip.py` or add an alias to it for simple. I have not found a method to make a short key to run a script.

# Installation

You need to install `pyperclip` using pip.

This program is tested under python 2.7, ubuntu 14.04 and osx 10.9.
