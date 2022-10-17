import pathlib
import random

# Note:
# Changing FRAMES and or RESOLUTION will heavily impact load on CPU.
# If you have a powerful enough computer you may set it to 1080p60

# other
PATH = str(pathlib.Path().absolute()).replace("\\", "/")
CLIP_PATH = PATH + "/clips/{}/{}"
CHECK_VERSION = True  # see if you're running the latest versions
DEBUG = True  # If additional/debug information should be printed (True/False)

DATA = ["c a2guapo", "c addison", "c asunaweeb",
        "c ethos", "c kyedae", "c nosyy", "c odablock",
        "c revenvalorant", "c s0mcs", "c scream", "c HasanAbi",
        "c shanks_ttv", "c subroza", "c ventusval", "c wardell",
        "c shroud", "c nAts", "c TenZ", "c AverageJonas",
        "c ShahZam", "c Cryocells", "c Horcus", "c lululuvely",
        "g Valorant"]

# For Japanese Content
DATA_JP = [
    "c fps_shaka", "c tennn", "c spygea",
    "c kamito_jp", "c im_mittiii", "c lazvell", "c neth3",
    "c takejfps", "c raderaderader", "c suzucharo",
    "c crowfps__", "c lazvell", "c reitathefps", "c sugarz3ro",
    "c barcefps", "c zepher", "c cr_rion", "c fps_fisker",
    "c derialy", "c blackwiz_cs", "c xnfri", "c mintyjp",
    "c popogachi7", "marin000", "c jpryota", "c Npoint",
    "c oitan_", "c 21sakurai", "c ow_pepper", "c flaxiey",
    "c kuukai1022"
]

# Randomising Order of Content Creators
random.shuffle(DATA_JP)
# Extending Game Name
DATA_JP.extend("g Valorant")


BLACKLIST = [
    "g Overwatch 2",
    "g Apex Legends",
    "g Counter-Strike: Global Offensive",
    "g Fortnite",
    "g Just Chatting"
]  # channels/games you don't want to be included in the video

BLACKLIST_JP = [

]
# twitch
PERIOD = 24  # how many hours since the clip's creation should've passed e.g. 24, 48 etc 0 for all time
LANGUAGE = "en"  # en, es, th etc.
LANGUAGE_JPN = "ja"
LIMIT = 100  # 1-100


# selenium
ROOT_PROFILE_PATH = r"/Users/macbook/Library/Application Support/Firefox/Profiles/bsd7ebhs.Selenium"  # Path to the Firefox profile where you are logged into YouTube
EXECUTABLE_PATH = r"geckodriver"
SLEEP = 3  # How many seconds Firefox should sleep for when uploading
HEADLESS = True  # If True Firefox will be hidden (True/False)


# video options
RENDER_VIDEO = True  # If clips should be rendered into one video (True/False). If set to False everything else under Video will be ignored
RESOLUTION = (
    1080,
    1920,
)  # Resolution of the rendered video (height, width) for 1080p: ((1080, 1920))
FRAMES = 30  # Frames per second (30/60)
VIDEO_LENGTH = 15.5  # Minimum video length in minutes (doesn't always work)
RESIZE_CLIPS = True  # Resize clips to fit RESOLUTION (True/False) If any RESIZE option is set to False the video might end up having a weird resolution
FILE_NAME = "rendered"  # Name of the rendered video
ENABLE_INTRO = True  # Enable (True/False)
RESIZE_INTRO = True  # Resize (True/False) read RESIZE_CLIPS
INTRO_FILE_PATH = PATH + "/twitchtube/files/intro.mp4"  # Path to video file (str)
ENABLE_TRANSITION = True
RESIZE_TRANSITION = True
TRANSITION_FILE_PATH = PATH + "/twitchtube/files/transition.mp4"
ENABLE_OUTRO = False
RESIZE_OUTRO = True
OUTRO_FILE_PATH = PATH + "/twitchtube/files/outro.mp4"


# other options
SAVE_TO_FILE = True  # If YouTube stuff should be saved to a separate file e.g. title, description & tags (True/False)
SAVE_FILE_NAME = "youtube"  # Name of the file YouTube stuff should be saved to
UPLOAD_TO_YOUTUBE = True  # If the rendered video should be uploaded to YouTube after rendering (True/False)
DELETE_CLIPS = True  # If the downloaded clips should be deleted after rendering the video (True/False)


# youtube
TITLE = "Most Watched Valorant Clips Today E1"  # YouTube title, leave empty for the first clip's title
DESCRIPTION = (
    "Our main goal is to bring the valorant gaming community closer by uploading the smart gameplays, key moments and sometimes funny clips from valorant.  We also try helping underrated Valorant pros/streamers to grow more by featuring them in our channel . You can send us the clips on our Discord Channel.\n\nAlso, we try our best to bring you the best and most unique videos, we hope you enjoy it! We spend about 6-8 hours daily working on these videos (searching / filtering / editing) and showing the best game clips combined with creative and high-quality editing.\n\nStreamers in This Video:\n"  # YouTube's description, streamers will be added
)
THUMBNAIL = ""  # path to the image file to be set as thumbnail
TAGS = ["twitch", "valorant", "valorant clips", "valorant highlights", "valorant daily"]  # your youtube tags