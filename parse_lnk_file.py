#!/usr/bin/python
import sys

if len(sys.argv) == 1:
      print "Usage: python "+sys.argv[0]+" file.lnk"
      sys.exit(1)

d=open(sys.argv[1], "rb").read()

def byte_to_hex(byte):
    '''
    Parameter: 0x9a
    Returns: "9a"
    '''
    ret=str(hex(ord(byte)))[2:4]
    if len(ret) == 1:
        ret="0"+ret
    return ret

#SHELL LINK HEADER (should be bytes from 0 to 75)
header_size=ord(d[0])
print "Checking Header size"
if d[0:4]=="\x4c\x00\x00\x00":
    print " Header size match (76 in decimal)"
else:
    print " Header size not 76! (in decimal)"

print "Checking Class identifier"
if d[4:20]=="\x01\x14\x02\x00\x00\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x46":
    print " Class identifier match"

print "Parse LinkFlags"
linkflags=byte_to_hex(d[20])+byte_to_hex(d[21])+byte_to_hex(d[22])+byte_to_hex(d[23])
import parse_link_flags
print " ",parse_link_flags.parse_link_flags(linkflags)


print "Parse FileAttributes"
fileattributes=byte_to_hex(d[24])+byte_to_hex(d[25])+byte_to_hex(d[26])+byte_to_hex(d[27])
import parse_file_attributes
print " ",parse_file_attributes.parse_file_attributes(fileattributes)

import parse_filetime
print "Parse CreationTime"
c_time=byte_to_hex(d[28])+byte_to_hex(d[29])+byte_to_hex(d[30])+byte_to_hex(d[31])+byte_to_hex(d[32])+byte_to_hex(d[33])+byte_to_hex(d[34])+byte_to_hex(d[35])
print " ",parse_filetime.parse_filetime(c_time)

print "Parse AccesTime"
a_time=byte_to_hex(d[36])+byte_to_hex(d[37])+byte_to_hex(d[38])+byte_to_hex(d[39])+byte_to_hex(d[40])+byte_to_hex(d[41])+byte_to_hex(d[42])+byte_to_hex(d[43])
print " ",parse_filetime.parse_filetime(a_time)

print "Parse WriteTime"
w_time=byte_to_hex(d[44])+byte_to_hex(d[45])+byte_to_hex(d[46])+byte_to_hex(d[47])+byte_to_hex(d[48])+byte_to_hex(d[49])+byte_to_hex(d[50])+byte_to_hex(d[51])
print " ",parse_filetime.parse_filetime(w_time)


print "Parse filesize (directories will be 0)"
print " ",int(byte_to_hex(d[55])+byte_to_hex(d[54])+byte_to_hex(d[53])+byte_to_hex(d[52]),16)

print "Parse iconindex"
print " ",int(byte_to_hex(d[59])+byte_to_hex(d[58])+byte_to_hex(d[57])+byte_to_hex(d[56]),16)

print "Parse ShowCommand (1=yes)"
print " ",int(byte_to_hex(d[63])+byte_to_hex(d[62])+byte_to_hex(d[61])+byte_to_hex(d[60]),16)

print "Parse HotKey (0=no shortcut key is defined)"
print " ",int(byte_to_hex(d[65])+byte_to_hex(d[64]),16)
#TODO: parse hotkey if defined (MS-SHLLINK.pdf, version 5.0, 2.1.3 HotKeyFlags, page 15)

#Reserved1, MUST be zero.
if d[66:68] != "\x00\x00":
    print "Reserved1 not zero!", byte_to_hex(d[66]),byte_to_hex(d[67])

#Reserved2, MUST be zero.
if d[68:72] != "\x00\x00\x00\x00":
    print "Reserved2 not zero!", byte_to_hex(d[68]),byte_to_hex(d[69]),byte_to_hex(d[70]),byte_to_hex(d[71])

#Reserved3, MUST be zero.
if d[72:76] != "\x00\x00\x00\x00":
    print "Reserved3 not zero!", byte_to_hex(d[72]),byte_to_hex(d[73]),byte_to_hex(d[74]),byte_to_hex(d[75])

#End of SHELL LINK HEADER

#To be continued...
#LINKTARGET IDLIST (if fileattribute HasLinkTargetIDList is specified)
#print "Parse IDListSize"
#idlistsize=int(byte_to_hex(d[77])+byte_to_hex(d[76]),16)
#print " ",idlistsize


