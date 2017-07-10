# We are going to use OF bindings to load/play videos
from openframeworks import *

# This is the ProtoPixel API for Content creation
from protopixel import Content

# Standard python stuff we need to list directories
import os
import os.path


# Constants
DEFAULT_VIDEO_PATH = "/home/protopixel/Desktop/videos"
VIDEO_EXTENSIONS = ['.mp4','.avi','.mpg']


# Create content and its parameters
content = Content('Video Folder')
content.add_parameter('video folder', type='filepath')


# Video player from OF
vid = ofVideoPlayer()

current_video_file = None


def update():
    "Update function, called once per frame"
    if video_ended(vid) or not current_video_file:
        load_next_video()

    if vid.isLoaded():
        vid.update()


def load_next_video():
    "Checks what's the next video to be loaded and loads it"
    global current_video_file

    video_folder = content['video folder']

    if not os.path.isdir(video_folder):
        video_folder = os.path.dirname(video_folder)

    # get the default video folder in case the specified one does not exist
    if not os.path.exists(video_folder):
        video_folder = DEFAULT_VIDEO_PATH
        if not os.path.exists(video_folder):
            # no valid folder
            return

    video_list = [fn for fn in os.listdir(video_folder) if os.path.splitext(fn)[1].lower() in VIDEO_EXTENSIONS]

    # we sort it alphabetically
    video_list = sorted(video_list)

    # empty dir
    if not video_list:
        return

    print video_list

    #try to get next playable item
    try:
        index_current = video_list.index(current_video_file)
        next_to_play = video_list[index_current+1]
    except (ValueError, IndexError):
        # no next item, go to first
        next_to_play = video_list[0]

    print "Next video is", next_to_play

    current_video_file = next_to_play

    if load_video(os.path.join(video_folder,next_to_play)):
        print "PLAYING"
        vid.setLoopState(OF_LOOP_NONE)
        vid.play()
        print vid.isLoaded()
        print vid.isPlaying()
        print vid.isInitialized()
        print vid.isPaused()
        print vid.getPosition()

def load_video(path):
    if not os.path.isfile(path):
        return
    result = vid.load(path)
    if result:
        content.FBO_SIZE = (int(vid.getWidth()), int(vid.getHeight()))
    return result

def draw():
    ofClear(0, 0, 0)
    ofSetColor(255, 255, 255)
    if vid.isLoaded():
        vid.draw(0, 0)

# Tools


def video_ended(v):
    "Portable way to know if an OF video player has ended"
    
    # We need to remember latest checks, as some of these methods return ambiguous values
    if not hasattr(v,'video_was_playing'):
        v.video_was_playing = False
    
    # Now we deduce the state of video player
    if v.getPosition() == 1.0:
        v.video_was_playing = False
        return True
    elif v.getPosition() < 0: #-inf tipically
        if v.video_was_playing:
            v.video_was_playing = False
            return True
        else:
            return False
    else:
        v.video_was_playing = True
        return False



def exit():
    vid.stop()