#!/usr/bin/env python
import sys
import socket
import platform
import json
import pyperclip as clip
import rc4
from daemon import Daemon
import config

message_stack = []

def process_message(msg):
    global message_stack
    try:
        msg = json.loads(msg)
    except:
        return None
    if msg.get('username') != config.username or msg.get('node') == platform.node():
        return None
    if msg.get('first'):
        message_stack = []
    message_stack.append(msg)
    if msg.get('last'):
        message_stack.sort(key=lambda x: x.get('order'))
        message = ''
        for m in message_stack:
            message += m['msg']
        message = rc4.decrypt(message, config.password)
        message_stack = []
        return message
    return None

def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    my_socket.bind(('', config.port))

    print 'start service ...'

    while True:
        message, address = my_socket.recvfrom(8192)
        message = process_message(message)
        if message:
            print 'message (%s ...) from : %s' % (message[:50], address[0])
            clip.copy(message)

class ClipDaemon(Daemon):
    def run(self):
        main()

if __name__ == "__main__" :
    if len(sys.argv) == 1:
        main()
    else:
        action = sys.argv[1]
        clip_daemon = ClipDaemon('/tmp/clipcast.pid')
        if action == 'start':
            clip_daemon.start()
        elif action == 'stop':
            clip_daemon.stop()
        elif action == 'restart':
            clip_daemon.restart()
