# video_compressor
Simple video comporessor wirtten in python using ffmpeg

To use it, first open main.py, then select video files you want to compress (only mp4, mkv and mov).

Choose if you want to use bitrate compression or auto, using bitrate compression you can choose the bitrate of compressed videos. 
It will be current bitrate * slider number%. 
Auto compression uses ffmpeg crf compression, its more effective and faster. The slider will affect compression factor. 
Higher number = bigger compresion. 

Then click compress and wait untill "Done" window pops up.

below you can see how much time the operation took.
