import os, json, subprocess, shlex
from time import time

path_to_videos = input('Insert path to the folder with videos or video you want to compress: ')
if not os.path.isabs(path_to_videos):
    os.path.abspath(path_to_videos)

print(path_to_videos)

compression_factor = input('Input compression rate 0-99: ')
try: 
    compression_factor = int(compression_factor)
except:
    print('Invalid compression factor')
    
if compression_factor not in range(0,99):
    print('compression factor not in range!')
    input('press enter to exit')
    exit()

compression_type = input('Input compression type b/a (bitrate/auto): ')
if compression_type not in ['a','b']:
    print('Wrong compression type!')
    input('press enter to exit')
    exit()

if compression_type == 'a':
    compression_factor = int((compression_factor+3)/2)

start = time()

if os.path.isfile(path_to_videos):
    if path_to_videos[-3:] not in ['mp4', 'mov'] or os.path.isdir(path_to_videos):
        print(f'{path_to_videos} is not a valid file')
        exit()

    if compression_type == 'a':
        folder, filename = os.path.split(path_to_videos)
        newpath = os.path.join(folder, 'compressed_' + filename)
        os.system(f'ffmpeg -i "{path_to_videos}" -vcodec h264 -crf {compression_factor} "{newpath}"')

    elif compression_type == 'b':
        accual_bitrate = int(json.loads(subprocess.run(shlex.split(f'ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -print_format json "{path_to_videos}"'), stdout=subprocess.PIPE).stdout)['streams'][0]['bit_rate'])
        target_bitrate = accual_bitrate * ((100 - compression_factor)/100)
        folder, filename = os.path.split(path_to_videos)
        newpath = os.path.join(folder, 'compressed_' + filename)
        os.system(f'ffmpeg -i "{path_to_videos}" -vcodec h264 -b {target_bitrate} "{newpath}"')

elif os.path.isdir(path_to_videos):
    for path in os.listdir(path_to_videos):

        path = os.path.join(path_to_videos, path)
        
        if path[-3:] not in ['mp4', 'mov'] or os.path.isdir(path):
            print(f'skipped {path}')
            continue
        
        if compression_type == 'a':
            folder, filename = os.path.split(path)
            newpath = os.path.join(folder, 'compressed_' + filename)
            os.system(f'ffmpeg -i "{path}" -vcodec h264 -crf {compression_factor} "{newpath}"')

        elif compression_type == 'b':
            accual_bitrate = int(json.loads(subprocess.run(shlex.split(f'ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -print_format json "{path}"'), stdout=subprocess.PIPE).stdout)['streams'][0]['bit_rate'])
            target_bitrate = accual_bitrate * ((100 - compression_factor)/100)
            folder, filename = os.path.split(path)
            newpath = os.path.join(folder, 'compressed_' + filename)
            os.system(f'ffmpeg -i "{path}" -vcodec h264 -b {target_bitrate} "{newpath}"')

else: 
    print('Invalid path')
    input('press enter to exit')
    exit()

print("Finnished in %.2f seconds" % (time()-start))
input('press enter to exit')
