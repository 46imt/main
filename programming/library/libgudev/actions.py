#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():

   options = "--disable-umockdev  \
             "

   if get.buildTYPE() == "emul32":
      options += "--disable-introspection \
                  --disable-gtk-doc \
                 "
   else:
      options += "--enable-introspection \
                  --enable-gtk-doc \
                 "
   

   autotools.configure(options)
    
   pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dodoc("AUTHORS", "COPYING")
