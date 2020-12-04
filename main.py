import sys

import xbmc
import xbmcgui
import xbmcplugin

addon_path = xbmc.translatePath("special://home/addons/plugin.video.EuropebyKodi/")
handle = int(sys.argv[1])


def li(name):
    listitem = xbmcgui.ListItem(name)
    listitem.setArt({'icon': addon_path + "resources/icon.png"})
    return listitem


channels = [
    ("https://euc-live.fl.freecaster.net/live/eucom/ebs-audio_eng=96000-video=1600000.m3u8", li("EbS")),
    ("https://euc-live.fl.freecaster.net/live/eucom/ebsp-audio_eng=96000-video=1600000.m3u8", li("EbS+"))
]

xbmcplugin.addDirectoryItems(handle, channels)
xbmcplugin.endOfDirectory(handle)
