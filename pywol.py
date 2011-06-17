import socket
import struct
import re

MAC_PATT = re.compile('([a-fA-F0-9]{2}[:|\-]?){6}')
MAC_PARTS_PATT = re.compile('[a-fA-F0-9]{2}')

def wake(mac_addr, ip):
    """wake a computer given ip and mac address assuming wake
       on lan is enabled
    """
    
    #invalid ethernet address
    if MAC_PATT.match(mac_addr) == None: 
        return False

    byte_addr = MAC_PARTS_PATT.findAll(mac_addr)
    if len(byte_addr) != 6: 
        return false

    mac_addrB = struct.pack('BBBBBB', *map(int, byte_addr,[16, 16, 16, 16, 16, 16]))
    
    #construct the message for the wake on lan packet
    #WOL Magic Packet Format: 12 leading F's + target machines
    #MAC Address
    magic_packet = "F" * 12 + mac_addrB * 16
    
    #create a datagram socket and send out packet
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(packet, ip)
    sock.close()

