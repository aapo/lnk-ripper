#!/usr/bin/python
# MS-SHLLINK.pdf, version 5.0, 2.1.1 LinkFlags, page 12
#Take hex-value as-it from lnk-file from offset 0x14
# Length is 8 bytes. It is big endian.
import sys
def parse_link_flags(p):
    if len(p) == 1 or len(p) != 8:
        return []

    LE=p[6:8]+p[4:6]+p[2:4]+p[0:2] #Convert to little endian
    number= int(LE,16)            #Convert to integer
    binary=format(number,'032b')  #Convert to binary
    b=str(binary)[::-1]           #Read backwards convert to string

    result=[]

    if b[0] == "1":
            result.append("A=HasLinkTargetIDList")
    if b[1] == "1":
            result.append("B=HasLinkInfo")
    if b[2] == "1":
            result.append("C=HasName")
    if b[3] == "1":
            result.append("D=HasRelativePath")
    if b[4] == "1":
            result.append("E=HasWorkingDir")
    if b[5] == "1":
            result.append("F=HasArguments")
    if b[6] == "1":
            result.append("G=HasIconLocation")
    if b[7] == "1":
            result.append("H=IsUnicode")
    if b[8] == "1":
            result.append("I=ForceNoLinkInfo")
    if b[9] == "1":
            result.append("J=HasExpString")
    if b[10] == "1":
            result.append("K=RunInSeparateProcess")
    if b[11] == "1":
            result.append("L=Unused1")
    if b[12] == "1":
            result.append("M=HasDarwinID")
    if b[13] == "1":
            result.append("N=RunAsUser")
    if b[14] == "1":
            result.append("O=HasExpIcon")
    if b[15] == "1":
            result.append("P=NoPidlAlias")
    if b[16] == "1":
            result.append("Q=Unused2")
    if b[17] == "1":
            result.append("R=RunWithShimLayer")
    if b[18] == "1":
            result.append("S=ForceNoLinkTrack")
    if b[19] == "1":
            result.append("T=EnableTargetMetadata")
    if b[20] == "1":
            result.append("U=DisableLinkPathTracking")
    if b[21] == "1":
            result.append("V=DisableKnownFolderTracking")
    if b[22] == "1":
            result.append("W=DisableKnownFolderAlias")
    if b[23] == "1":
            result.append("X=AllowLinkToLink")
    if b[24] == "1":
            result.append("Y=UnaliasOnSave")
    if b[25] == "1":
            result.append("Z=PreferEnvironmentPath")
    if b[26] == "1":
            result.append("AA=KeepLocalIDListForUNCTarget")
    if b[27] == "1":
            result.append("NotUsed1")
    if b[28] == "1":
            result.append("NotUsed2")
    if b[29] == "1":
            result.append("NotUsed3")
    if b[30] == "1":
            result.append("NotUsed4")
    if b[31] == "1":
            result.append("NotUsed5")

    return result

if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv[1]) != 8:
        print "Usage: python "+sys.argv[0]+" 9B002000"
        sys.exit(1)

    print parse_link_flags(sys.argv[1])
