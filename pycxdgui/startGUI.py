import pkg_resources

from PyQt5 import QtGui
from pycxdgui.gui.SAXSMainGUI import SAXSGUI
import sys

''' The GUI for reading images and some simple analysis
    Note: The xcoordinate is taken to be the fastest varying dimension (rightermost)
        Since pyqt rather takes x to be the other way, I need to transpose everything
        when displaying.
'''


DDIR = "/media/xray/NSLSII_Data/CHX"
SDIR = "../storage"
sxsdesc = "B002.sxs"


def is_interactive():
    import __main__ as main
    return not hasattr(main, '__file__')

if __name__ == "__main__":
    # Necessary for a pyQt application to work
    print("starting GUI")
    configfile = pkg_resources.resource_filename("pycxdgui", "saxsgui-config.yml")
    app = QtGui.QApplication(sys.argv)
    sxgui = SAXSGUI(configfile=configfile, verbose=True)
    sxgui.show()
    if not is_interactive():
        sys.exit(app.exec_())

def run(configfile=None):
    if configfile is None:
        # TODO : replace with search path
        configfile = pkg_resources.resource_filename("pycxdgui", "saxsgui-config.yml")
    # Necessary for a pyQt application to work
    print("starting GUI")
    app = QtGui.QApplication(sys.argv)
    sxgui = SAXSGUI(configfile=configfile, verbose=True)
    sxgui.show()
    sys.exit(app.exec_())
