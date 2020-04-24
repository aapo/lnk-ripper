#!/usr/bin/python
# A FILETIME structure ([MS-DTYP] section 2.3.3)
import sys
def parse_filetime(p):
    if len(p) != 16:
        return []

    temp_array=(p[0:2],p[2:4],p[4:6],p[6:8],p[8:10],p[10:12],p[12:14],p[14:16])
    number = int("".join(temp_array[::-1]), 16)

    from datetime import datetime, timedelta, tzinfo
    from calendar import timegm

    #EPOCH_AS_FILETIME = 116444736000000000
    #HUNDREDS_OF_NANOSECONDS = 10000000
    (s, ns100) = divmod(number - 116444736000000000, 10000000)
    dt = datetime.utcfromtimestamp(s)
    dt = dt.replace(microsecond=(ns100 // 10))

    return dt

if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv[1]) != 16:
        print "Usage: python "+sys.argv[0]+" a0dbc6609e7bd201"
        sys.exit(1)

    print parse_filetime(sys.argv[1])
