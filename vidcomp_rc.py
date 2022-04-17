import os, json, subprocess, shlex
from time import time

path_to_videos = os.getcwd()
compression_factor = 27

for path in os.listdir(path_to_videos):

    path = os.path.join(path_to_videos, path)
    
    if path[-3:].lower() not in ['mp4', 'mov'] or os.path.isdir(path):
        continue
    
    folder, filename = os.path.split(path)
    accual_bitrate = int(json.loads(subprocess.run(shlex.split(f'ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -print_format json "{path}"'), stdout=subprocess.PIPE).stdout)['streams'][0]['bit_rate'])
    target_bitrate = accual_bitrate * ((100 - compression_factor)/100)
    newpath = os.path.join(folder, 'compressed_' + filename)
    os.system(f'ffmpeg -i "{path}" -vcodec h264 -crf {compression_factor} -maxrate {target_bitrate} -bufsize 128M "{newpath}"')
