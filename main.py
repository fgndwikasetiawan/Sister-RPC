from SimpleXMLRPCServer import SimpleXMLRPCServer as xmlserver
from xmlrpclib import Binary
import numpy as np
import cv2

alamat = raw_input('Alamat bind: ')
port = int(raw_input('Port: '))

server = xmlserver((alamat, port), logRequests=True, allow_none=True)
server.register_introspection_functions()
server.register_multicall_functions()

class MyService:
    def rgb_to_grayscale(self, arr):
        images = []
        for ele in arr:
            data = ele.data
            grayscale_m = cv2.imdecode(np.asarray(bytearray(data), dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
            images.append(Binary(cv2.imencode('.png', grayscale_m)[1]))
        return images

server.register_instance(MyService())

server.serve_forever()
