import sources

class Backend:
    def __init__(self):
        pass

    def getVideo(self,tmdbId,subs=False):
        for source in sources.sources:
            source: sources.source = source()

            if subs:
                if source.getSubtitles(tmdbId):
                    print(source.getVideo(tmdbId))
                    print(source.getSubtitles(tmdbId))
                else:
                    continue
            else:
                print(source.getVideo(tmdbId))

Backend().getVideo(0)