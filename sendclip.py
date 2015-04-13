#!/usr/bin/env python
import socket
import sys
import platform
import json
import zlib
import pyperclip as clip
import rc4
import config

MESSAGE_SIZE = 500

def main():
    message = clip.paste()
    if not message:
        return
    message = rc4.encrypt(message.encode('utf-8'), config.password)
    thunks = [message[i:i+MESSAGE_SIZE] for i in range(0, len(message), MESSAGE_SIZE)]
    thunk_count = len(thunks)
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    for i, thunk in enumerate(thunks):
        msg = {'username': config.username, 'node': platform.node(), 'order': i, 'msg': thunk}
        if i == 0:
            msg['first'] = True
        if i + 1 == thunk_count:
            msg['last'] = True
        msg = json.dumps(msg)
        # print 'Length of message is %d.' % len(msg)
        my_socket.sendto(msg, (config.broadcast_network, config.port))
    my_socket.close()

if __name__ == '__main__':
    main()
