# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Youtube Channel
# (c) 2015 - Simple TechNerd
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.myyoutubeAddon'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("spoonfed productions", "user/pctech9990", 'https://i.ytimg.com/vi/LTaaPe_tScA/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLCai5yabp8WUAZyRA0SyiTiIUXv6A'),
        ("DaButcher", "channel/UC-jBkGiRokRd-B2ylx1VqJQ", 'https://i.ytimg.com/vi/oymJEnjlcoQ/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLBjcCVyhRuHeEKrEqoNNYOgV8qgFg'),
        ("Dimitrology", "user/dimitrology", 'https://i.ytimg.com/vi/YHPpbiqvsNw/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLAJ2AGMnC9kq7J9NeXjel08isMujw'),				
        ("Husham", "/channel/UCKox-lD5VFKXJ3Jg_Vcu9Og", 'https://i.ytimg.com/vi/vWLChYSxmr8/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLBwVNdS2bMeE6lVVi9csy398aZ3Eg'),
        ("Simple Kore", "/channel/UCgC_gjO6044hDD6RRm5o7Iw", 'https://i.ytimg.com/vi/W0xqyL0XxAo/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLAZASj7TRVomnxdVVqQOG7aLkUBMQ'),
        ("Kodi Canal", "/channel/UCdJXx-oVdpiz4bW_0ljR2rg",  'https://i.ytimg.com/vi/nfvbZDlCrg4/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLBlJn7t_31Eol4yK5nZoRW3JEzdgQ'),
        ("Hollis & Nancy's Homestead", "/channel/UCPVn9bDOp3DfMMKjPrEsIOw",  'https://i.ytimg.com/vi/q8dAqiKX6Zg/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLCn3NhBh99c3NmjTAq_yI-BBHP18g'),
        ("OFF GRID with DOUG & STACY", "/user/growinginfaithfarm",  'https://i.ytimg.com/vi/ny0NFEa_cLw/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLBBaqNwEGvwLFQN5IO9AjFLAMFCTA'),
        ("WWE", "/user/WWEFanNation",  'https://i.ytimg.com/vi/VEH0PG-VEzk/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLC20IzRdON-DDqo_t7iQsF1lwBIpQ'),
        ("Bob Ross", "/user/BobRossInc",  'https://i.ytimg.com/vi/rDs3o1uLEdU/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLDgM0jZuixidLT6nMEdlXEphRFsNg'),
        ("Britec09", "/channel/UC_M-iWYpQbgo4rK1YfewI5w",  'https://i.ytimg.com/vi/Y-eVh4PGxOA/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLDCoRkRSubo5PDfFRAsw2wf7TwX5w'),
        ("Eli the Computer Guy", "/user/elithecomputerguy",  'https://i.ytimg.com/vi/H-x5UeHEIvA/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLDT9OMcqOKyQVXsQGXaFUUCwnTBTg'),
        ("TheBeginnerGuy", "/user/TheBeginnerGuy24",  'https://i.ytimg.com/vi/h8AsOFQpEeQ/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLAzORAw0gSn-omDDrWCIQCF8kKB5Q'),
        ("Plant Abundance", "/channel/UCEFpzAuyFlLzshQR4_dkCsQ",  'https://i.ytimg.com/vi/lQI1LBSsifc/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLDu2bTGB-XPw5HvXhJ2izqv1Cq3wg'),
        ("Tantrum Dev", "/channel/UCs_Ci64Q3vz8h8rBhOkPMYw",  'https://i.ytimg.com/vi/4erYg7Rejgw/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLAVCmJjQg6-nCuHCnjHaSBEiutipw'),
        ("Epic Gardening", "/user/EpicGardening",  'https://i.ytimg.com/vi/NU8iM4WTC8c/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLB7FTR42Ta7HsILMhUFyzpsOdbFsg'),
        ("Maxin TV", "/channel/UCNSn42GHh65f9F94e3DCBIQ",  'https://i.ytimg.com/vi/AflHeKwe7gE/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLDoo77S7QWGFlwEy9yX7JXha_LIIw'),
        ("Gardining With Leon", "/channel/UCSDYs9sd2_BlLuWSiEr7TJQ",  'https://i.ytimg.com/vi/1TX2U-3r2wk/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&amp;rs=AOn4CLDIO9c7GjIweTYH_wZBM-pE3c40Wg'),





]

# Entry point
def run():
    plugintools.log("myyoutubeAddon.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("myyoutubeAddon.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.myyoutube/"+id+"/",thumbnail=icon,folder=True )



run()