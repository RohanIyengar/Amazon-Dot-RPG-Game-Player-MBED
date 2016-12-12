'''
Class that allows Windows keyboard inputs to be hit programmatically.
Taken and modified from: http://stackoverflow.com/questions/11906925/python-simulate-keydown
'''
from httplib import HTTPConnection
import time
import sys
import keyboard

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import serial

global _serial
_serial = None
global writeChar
writeChar = ""

PORT_NUMBER = 8084

def initializeSerial():
    return serial.Serial(
            port='COM3',
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
        )

def keyPress():
    global writeChar
    for event in keyboard.keyboard_stream(writeChar):
        keyboard.SendInput(event)
        time.sleep(.1)
#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        # Send the html message
        self.wfile.write("Hello World !")
        return

    def do_POST(self):
        global writeChar
        global _serial
        # Doesn't do anything with posted data
        self.send_response(200)
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        print post_body
        if (post_body == "up"):
            cond = True
            while cond:
                try:
                    _serial = initializeSerial()
                    _serial.write('U\r\n')
                    cond = False
                    print "Printed to COM Port"
                    out = ''
                    time.sleep(1)
                    while _serial.inWaiting() > 0:
                        out += _serial.read(1)
                    if out !='':
                        print ">> " + out
                    writeChar = out
                    _serial.close()
                except Exception as e:
                    print e
                    print "Serial port in use -- waiting .5 seconds"
                    time.sleep(.01)
        if (post_body == "down"):
            cond = True
            while cond:
                try:
                    print writeChar
                    _serial = initializeSerial()
                    _serial.write('DDDDDDDDDDDDDDDD\r\n')
                    cond = False
                    print "Printed to COM Port"
                    out = ''
                    time.sleep(1)
                    while _serial.inWaiting() > 0:
                        out += _serial.read(1)
                    if out !='':
                        print ">> " + out
                    writeChar = out
                    print writeChar
                    _serial.close()
                except Exception as e:
                    print e
                    print "Serial port in use -- waiting .5 seconds"
                    time.sleep(.01)
        if (post_body == "left"):
            cond = True
            while cond:
                try:
                    _serial = initializeSerial()
                    _serial.write('LLLLLLLLLLLLLLLLLL\r\n')
                    cond = False
                    print "Printed to COM Port"
                    out = ''
                    time.sleep(1)
                    while _serial.inWaiting() > 0:
                        out += _serial.read(1)
                    if out !='':
                        print ">> " + out
                    writeChar = out
                    _serial.close()
                except Exception as e:
                    print e
                    print "Serial port in use -- waiting .5 seconds"
                    time.sleep(.01)
        if (post_body == "right"):
            cond = True
            while cond:
                try:
                    _serial = initializeSerial()
                    _serial.write('RRRRRRRRRRRRRRRRRR\r\n')
                    cond = False
                    print "Printed to COM Port"
                    out = ''
                    time.sleep(1)
                    while _serial.inWaiting() > 0:
                        out += _serial.read(1)
                    if out !='':
                        print ">> " + out
                    writeChar = out
                    _serial.close()
                except Exception as e:
                    print e
                    print "Serial port in use -- waiting .5 seconds"
                    time.sleep(.01)
        # Send the html message
        if (post_body == "a button"):
            cond = True
            while cond:
                try:
                    _serial = initializeSerial()
                    print _serial.isOpen()
                    _serial.write('A\r\n')
                    cond = False
                    print "Printed to COM Port"
                    out = ''
                    time.sleep(1)
                    while _serial.inWaiting() > 0:
                        out += _serial.read(1)
                    if out !='':
                        print ">> " + out
                    writeChar = out
                    _serial.close()
                except Exception as e:
                    print e
                    print "Serial port in use -- waiting .5 seconds"
                    time.sleep(.01)
        if (post_body == "b button"):
            cond = True
            while cond:
                try:
                    _serial = initializeSerial()
                    print _serial.isOpen()
                    _serial.write('BBBBBBBBBBBBBBBB\r\n')
                    cond = False
                    print "Printed to COM Port"
                    out = ''
                    time.sleep(.5)
                    while _serial.inWaiting() > 0:
                        out += _serial.read(1)
                    if out !='':
                        print ">> " + out
                    print out == "B"
                    writeChar = out
                    _serial.close()
                except Exception as e:
                    print e
                    print "Serial port in use -- waiting .5 seconds"
                    time.sleep(.05)
        keyPress()
        self.wfile.write("Hello World POST!")
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()