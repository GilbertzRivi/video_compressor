import os
from time import time

path_to_videos = os.getcwd()
compression_factor = 27

for path in os.listdir(path_to_videos):

    path = os.path.join(path_to_videos, path)
    
    if path[-3:] not in ['mp4', 'mov'] or os.path.isdir(path):
        continue
    
    folder, filename = os.path.split(path)
    newpath = os.path.join(folder, 'compressed_' + filename)
    os.system(f'ffmpeg -i "{path}" -vcodec h264 -crf {compression_factor} "{newpath}"')