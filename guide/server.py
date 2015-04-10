#!/usr/bin/python
# do: the requeted data stored in xml
import SimpleXMLRPCServer
import xml.etree.ElementTree as ET

class Query:
    def __init__(self):
        pass
    def query(self, astr):
        retn = []
        tree = ET.parse('data.xml')
        root = tree.getroot()
        for r in root.findall(astr):
            retn.append(r.text)
        return astr + ": " + ','.join(retn)


server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(Query())
server.serve_forever()
