
MESSAGE_NOLINKS = '''
Usage: ytdownload <-(4320/2160/1440/1080/720/480/360/240)p>(optional) <-includeaudio/audioonly>(optional) <link1> <link2> <..>

    default resolution is 1080p or, if not available, the highest resolution of the video
    -includeaudio will  download both the video and its audio file, -audioonly will only download audio, 
        leave it out if you only want the video

---Please provide at least one valid youtube link or playlist---

More features coming soon! :P
'''

MESSAGE_INVALIDLINK = '''
Argument must be a valid YouTube link or Playlist link

If you inserted more than 2 optional '-' arguments, this error will be raised.'''

class NoLinksError(Exception):
    
    def __init__(self, val, message=MESSAGE_NOLINKS):
        self.val = val
        self.message = message
        super().__init__(self.message)

class NotaYTLinkOrPlayListError(Exception):
    
    def __init__(self, val, message=MESSAGE_INVALIDLINK):
        self.val = val
        self.message = message
        super().__init__(self.message)