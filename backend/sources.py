class source:
    def __init__(self): pass
    def getVideo(self,tmdbId): raise NoVideo
    def getSubtitles(self,tmdbId): raise NoSubtitles

class NoSubs(source):
    def __init__(self):
        pass

    def getVideo(self,tmdbId):
        return 'Displaying Video for '+str(tmdbId)

class Subs(source):
    def __init__(self):
        pass

    def getVideo(self,tmdbId):
        return 'Displaying Video for '+str(tmdbId)
    
    def getSubtitles(self, tmdbId):
        return 'Displaying Subtitles for '+str(tmdbId)

class NoSubtitles(BaseException): pass
class NoVideo(BaseException): pass

sources: list[source] = [NoSubs, Subs]