# video_compressor
Simple video comporessor wirtten in python using ffmpeg

Requirements:
```
ffmpeg, ffprobe added to PATH
python libs: os, tkinter, json, subprocess, shlex, time
```

To use it, first open vidcomp gui.py, then select video files you want to compress (only mp4 and mov).

Choose if you want to use bitrate compression or auto compression mode. When using bitrate compression you can choose the bitrate of compressed videos. 
It will be equal to the current bitrate * slider number(%). 

Auto compression uses ffmpeg crf compression, its better and faster. The slider will affect compression factor. 
Higher number = bigger compresion. 

Then click compress and wait untill "Done" window pops up. Don't worry if the windows will be unresponding, just wait. In cmd window, you can see the progress program  has already made.

After completion of compression, you can see how much time it took.

I've also made command line tool, you can use it similarly to the gui one. 

To add this script to right click menu, you have to insert 'YOUR_PATH_TO_THIS_FILE' in reg_key.py and run it as administrator.
You also need to install winregistry lib.
