import shutil
import os
import sys
import urllib2
import zipfile
        
def p(o, b):
    if 'win' in sys.platform:
        dest = o['location']
        bin = os.path.join(dest, 'bin')
        if not os.path.exists(bin): os.makedirs(bin)
        for dll in [libdll 
                    for libdll in os.listdir(bin) 
                    if( libdll.endswith('dll') 
                    and not libdll.startswith('lib')
                    and not libdll.startswith('cyg') )]:
            for pref in 'cyg', 'lib':        
                orig = os.path.join(bin, dll)
                ldest = os.path.join(bin, '%s%s' % (pref, dll))
                if os.path.exists(ldest):
                    os.remove(ldest)
                shutil.copy2(orig, ldest)

    
# vim:set ts=4 sts=4 et  :
