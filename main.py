import sys
import xbmcgui
import xbmcplugin

EbS_URL = "https://audiovisual.ec.europa.eu"
handle = int(sys.argv[1])


def li(item):
    return xbmcgui.ListItem(item)


xbmcplugin.addDirectoryItems(handle, [("EbS", li("EbS")), ("EbS2", li("EbS+"))])
xbmcplugin.endOfDirectory(handle)
