import os, tkinter.filedialog, json, subprocess, shlex, time
import tkinter as tk
from tkinter.constants import END, HORIZONTAL

class MainWindow():

    def __init__(self, root):
        self.root = root
        
        self.video_files = tk.Button(self.root, height=1, width=20, text="choose files", command=self.select_videos)
        self.video_files.place(x=20, y=20)

        self.videos_frame = tk.Frame(self.root)
        self.videos_frame.place(x=20, y=55)
        self.videos_names = tk.Listbox(self.videos_frame, height=10, width=50)
        self.videos_names.grid(column=0, row=1)
        self.videos_scrolly = tk.Scrollbar(self.videos_frame, orient='vertical')
        self.videos_scrolly.configure(command=self.videos_names.yview)
        self.videos_scrolly.grid(column=1, row=1, sticky='w'+'n'+'s')
        self.videos_scrollx = tk.Scrollbar(self.videos_frame, orient='horizontal')
        self.videos_scrollx.configure(command=self.videos_names.xview)
        self.videos_scrollx.grid(sticky='n'+'e'+'w')
        self.videos_names.configure(xscrollcommand=self.videos_scrollx.set, yscrollcommand=self.videos_scrolly.set)

        self.compression_type_frame = tk.Frame(self.root, height=100, width=200, background='#f0f0f0')
        self.compression_type_frame.place(x=20, y=245)
        self.compression_type_var = tk.IntVar()
        self.compression_type = tk.Radiobutton(self.compression_type_frame, variable=self.compression_type_var,
            value=0, text='Bitrate compression', command=self.compresion_factor)
        self.compression_type.pack(anchor="w")
        self.compression_type = tk.Radiobutton(self.compression_type_frame, variable=self.compression_type_var,
            value=1, text='Automatic compression', command=self.compresion_factor)
        self.compression_type.pack(anchor="w")

        self.bitrate_number = tk.Label(text='Choose compresion rate.\nHigher value is higher compression.', justify='left')
        self.bitrate_number.place(x=20, y=300)

        self.compression_number_slider = tk.Scale(self.root, from_=0, to=99, orient=HORIZONTAL, length=300)
        self.compression_number_slider.place(x=20, y=345)

        self.action_button = tk.Button(self.root, height=1, width=20, text='Compress', command=self.compress)
        self.action_button.place(x=20, y=395)

        self.work_status = tk.Label(width=17, height=1)
        self.work_status.place(x=20,y=430)

    
    def select_videos(self):
        video_paths = tkinter.filedialog.askopenfilenames()
        not_vid_notification = False
        video_paths_sanitized = []
        for path in video_paths:
            if path[-3:] not in ['mp4', 'mov']:
                not_vid_notification = True
                continue
            else:
                video_paths_sanitized.append(path)
        
        if not_vid_notification:
            tk.messagebox.showerror('Not a video', 'Some of the files were not mp4, mov or files. They were skipped.')

        self.videos_names.delete(0, END)
        for i, path in enumerate(video_paths_sanitized):
            self.videos_names.insert(i, path)

    def compresion_factor(self):
        if self.compression_type_var.get() == 0:
            try:
                self.crf_number_label.destroy()
            except Exception:
                pass

            self.bitrate_number = tk.Label(text='Choose compresion rate.\nHigher value is higher compression.')
            self.bitrate_number.place(x=20, y=300)

        elif self.compression_type_var.get() == 1:
            try:
                self.bitrate_number.destroy()
            except Exception:
                pass

            self.crf_number_label = tk.Label(text='Choose compresion rate.\nHigher value is higher compression.')
            self.crf_number_label.place(x=20, y=300)

    def compress(self):
        
        for path in self.videos_names.get(0, END):
            folder, filename = os.path.split(path)
            newpath = os.path.join(folder, 'compressed_' + filename)
            if os.path.isfile(newpath):
                tk.messagebox.showerror('File already exist', f'"{newpath}" already exist, remove it to continue.')
                return

        if self.compression_type_var.get() == 0:
            comporession_rate = self.compression_number_slider.get()

            start = time.time()

            for path in self.videos_names.get(0, END):
                accual_bitrate = int(json.loads(subprocess.run(shlex.split(f'ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -print_format json "{path}"'), stdout=subprocess.PIPE).stdout)['streams'][0]['bit_rate'])
                target_bitrate = accual_bitrate * ((100 - comporession_rate)/100)
                folder, filename = os.path.split(path)
                newpath = os.path.join(folder, 'compressed_' + filename)
                os.system(f'ffmpeg -i "{path}" -vcodec h264 -b {target_bitrate} "{newpath}"')

        elif self.compression_type_var.get() == 1:
            comporession_rate = int((self.compression_number_slider.get()+3)/2)

            start = time.time()

            for path in self.videos_names.get(0, END):
                folder, filename = os.path.split(path)
                newpath = os.path.join(folder, 'compressed_' + filename)
                os.system(f'ffmpeg -i "{path}" -vcodec h264 -crf {comporession_rate} "{newpath}"')
        
        self.work_status.config(text="%.2f seconds" % (time.time()-start))
        tk.messagebox.showinfo('Done', 'Done')


root = tk.Tk()
root.title('Video Compressor')
root.resizable(width=False, height=False)
root.geometry('360x470')
root.configure(background='#2e2e2e')

VideoCompressor = MainWindow(root)
root.mainloop()
