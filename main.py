import sys

import xbmcgui
import xbmcplugin

handle = int(sys.argv[1])

# fmt: off
channels = [
    ("https://euc-live.fl.freecaster.net/live/eucom/ebs-audio_eng=96000-video=1600000.m3u8", xbmcgui.ListItem("EbS")),
    ("https://euc-live.fl.freecaster.net/live/eucom/ebsp-audio_eng=96000-video=1600000.m3u8", xbmcgui.ListItem("EbS+"))
]
# fmt: on

xbmcplugin.addDirectoryItems(handle, channels)
xbmcplugin.endOfDirectory(handle)
