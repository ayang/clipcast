# Clipcast

Clipboard share tool in LAN via UDP broadcast for multiple computer users. datas are encrypted by rc4.

# Usage

Modify `config.py` as you like.

Run `clipserver.py start` as a daemon for reciving clipboard text. Run `sendclip.py` to send current clipboard text to every machine in LAN. Only servers with same `username` config will recieve the clipboard.

# Installation

You need to install `pyperclip` using pip.

This program is tested under python 2.7.
