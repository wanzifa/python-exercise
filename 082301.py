# -*- coding: utf-8 -*-
# 7-9

def tr(srcstr, dststr, string, ignore = True):
    if(ignore == False):
        for i in range(len(srcstr)):
            for j in range(len(string)):
                if srcstr[i] == string[j]:
                     stringlist[j] = dststr[i]

    else :
        for i in range(len(srcstr)):
            for j in range(len(string)):
                if srcstr[i].upper() == string[j].upper():
                     stringlist[j] = dststr[i]

    newstring=''.join(stringlist)
    return newstring


def delete(srcstr, dststr, string):
    len1 = len(srcstr)
    len2 = len(dststr)
    srcstr = srcstr[0:len2]
    string = srcstr + string[len1:]
    transportation = tr(srcstr, dststr, sting, ignore = True)
    return transportation


srcstr = raw_input('please input srcstr:')
dststr = raw_input('please input dststr:')
string = raw_input('please input string:')
ignore = raw_input('ignore the size writing or not?(enter True or False):')
stringlist = list(string)
if len (srcstr) > len(dststr) :
    print 'the result is %s' % delete(srcstr, dststr, string)
else:

    print 'the result is %s' % tr(srcstr, dststr, string, ignore = True)
