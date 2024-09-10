import sys
from errorhandle import NoLinksError, NotaYTLinkOrPlayListError
import re
from downloader import downloader

RES = '1080p'
FILE_FORMAT = 'video'
ALL_RESOLUTIONS = ['4320p', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p']
ALL_FORMATS = ['video','audio', 'audioonly']

regex = r"^(?:https?:)?(?:\/\/)?(?:youtu\.be\/|(?:www\.|m\.)?youtube\.com\/(?:watch|v|embed|playlist)(?:\.php)?(?:\?.*v=|\?.*list=|\/))([a-zA-Z0-9\_-]{7,100})(?:[\?&][a-zA-Z0-9\_-]+=[a-zA-Z0-9\_-]+)*(?:[&\/\#].*)?$"

def format_args(args: list):
    """
    formats command line arguments to get resolutions, file formats desired, and to weed out any invalid/junk, arguments
    Args:
        args (list): [command line arguments]

    Raises:
        NotaYTLinkOrPlayListError: [points out an invalid YouTube link]

    Returns:
        [links]: [list of all valid links]
    """
    global RES
    global FILE_FORMAT
    pattern = re.compile(regex)
    links = []
    OPTIONAL_ARGS_COUNTER = 0
    for arg in args:
        if arg.startswith('-') and arg.endswith(tuple(ALL_RESOLUTIONS)) and OPTIONAL_ARGS_COUNTER<2:
            OPTIONAL_ARGS_COUNTER +=1
            RES = arg[1::]
        elif arg.startswith('-') and arg.endswith(tuple(ALL_FORMATS)) and OPTIONAL_ARGS_COUNTER<2:
            OPTIONAL_ARGS_COUNTER +=1
            FILE_FORMAT = arg[1::]
        else:
            if pattern.match(arg):
                links.append(arg)
            else:
                try:
                    raise NotaYTLinkOrPlayListError(-1)
                except NotaYTLinkOrPlayListError as e:
                    print(f'{e.message}: {arg}')

    return links

        



def main(args):
    if len(args) < 2:
        try:
            raise NoLinksError(-1)
        except NoLinksError as e:
            print(e.message)
            exit(-1)

    links = format_args(args[1::])

    if not links:
        try:
            raise NoLinksError(-1)
        except NoLinksError as e:
            print(e.message)
            exit(1)
    

    for link in links:
        downloader(RES, FILE_FORMAT, link)
    

if __name__ == '__main__':
    main(sys.argv)
