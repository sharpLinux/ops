#!/usr/bin/python 
import xmlrpclib

server = xmlrpclib.Server('http://localhost:8000')
print server.query('rankd')
