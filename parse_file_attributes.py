#!/usr/bin/python
# MS-SHLLINK.pdf, version 5.0, 2.1.2 FileAttributesFlags, page 14
#Take hex-value as-it from lnk-file from offset 0x18
# Length is 8 bytes.
import sys
def parse_file_attributes(p):
    if len(p) == 1 or len(p) != 8:
            return []

    LE=p[6:8]+p[4:6]+p[2:4]+p[0:2] #Convert to little endian
    number= int(LE,16)             #Convert to integer
    binary=format(number,'032b')   #Convert to binary
    b=str(binary)[::-1]            #Read backwards convert to string

    result=[]

    if b[0] == "1":
            result.append("A=FILE_ATTRIBUTE_READONLY")
    if b[1] == "1":
            result.append("B=FILE_ATTRIBUTE_HIDDEN")
    if b[2] == "1":
            result.append("C=FILE_ATTRIBUTE_SYSTEM")
    if b[3] == "1":
            result.append("D=Reserved1")
    if b[4] == "1":
            result.append("E=FILE_ATTRIBUTE_DIRECTORY")
    if b[5] == "1":
            result.append("F=FILE_ATTRIBUTE_ARCHIVE")
    if b[6] == "1":
            result.append("G=Reserved2")
    if b[7] == "1":
            result.append("H=FILE_ATTRIBUTE_NORMAL")
    if b[8] == "1":
            result.append("I=FILE_ATTRIBUTE_TEMPORARY")
    if b[9] == "1":
            result.append("J=FILE_ATTRIBUTE_SPARSE_FILE")
    if b[10] == "1":
            result.append("K=FILE_ATTRIBUTE_REPARSE_POINT")
    if b[11] == "1":
            result.append("L=FILE_ATTRIBUTE_COMPRESSED")
    if b[12] == "1":
            result.append("M=FILE_ATTRIBUTE_OFFLINE")
    if b[13] == "1":
            result.append("N=FILE_ATTRIBUTE_NOT_CONTENT_INDEXED")
    if b[14] == "1":
            result.append("O=FILE_ATTRIBUTE_ENCRYPTED")
    if b[15] == "1":
            result.append("NotUsed1")
    if b[16] == "1":
            result.append("NotUsed2")
    if b[17] == "1":
            result.append("NotUsed3")
    if b[18] == "1":
            result.append("NotUsed4")
    if b[19] == "1":
            result.append("NotUsed5")
    if b[20] == "1":
            result.append("NotUsed6")
    if b[21] == "1":
            result.append("NotUsed7")
    if b[22] == "1":
            result.append("NotUsed8")
    if b[23] == "1":
            result.append("NotUsed9")
    if b[24] == "1":
            result.append("NotUsed10")
    if b[25] == "1":
            result.append("NotUsed11")
    if b[26] == "1":
            result.append("NotUsed12")
    if b[27] == "1":
            result.append("NotUsed13")
    if b[28] == "1":
            result.append("NotUsed14")
    if b[29] == "1":
            result.append("NotUsed15")
    if b[30] == "1":
            result.append("NotUsed16")
    if b[31] == "1":
            result.append("NotUsed17")

    return result

if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv[1]) != 8:
      print "Usage: python "+sys.argv[0]+" 10000000"
      sys.exit(1)

    print parse_file_attributes(sys.argv[1])
