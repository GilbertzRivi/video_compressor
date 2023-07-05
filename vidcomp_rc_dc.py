import os, json, subprocess, shlex
from time import time

path_to_videos = os.getcwd()

for path in os.listdir(path_to_videos):

    path = os.path.join(path_to_videos, path)
    
    if path[-3:].lower() not in ['mp4', 'mov'] or os.path.isdir(path):
        continue
    
    folder, filename = os.path.split(path)
    data = (json.loads(subprocess.run(shlex.split(f'ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate,duration -print_format json "{path}"'), stdout=subprocess.PIPE).stdout)['streams'][0])
    duration = data['duration']
    bitrate = data['bit_rate']
    targetbitrate = int(((8*1024*1024*8)/float(duration))*0.8)
    newpath = os.path.join(folder, 'compressed_' + filename)
    os.system(f'ffmpeg -i "{path}" -vcodec h264 -b {targetbitrate} "{newpath}"')
