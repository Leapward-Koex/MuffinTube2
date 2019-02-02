from __future__ import unicode_literals
import sys
import shutil
import urllib.request
from mutagen.mp3 import MP3 as MP3 #tagging AND writing MP3
from mutagen.id3 import ID3, APIC, TIT2, error
import os
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot)
import youtube_dl


class thumbnailGetter:
    def __init__(self, url):
        self.url = url
        self.stripURL()

    def stripURL(self):
        start_index = self.url.find("v")
        end_index = self.url.find("&")
        if "&" in self.url:                                     #For playlists
            self.videoID = self.url[start_index + 2:end_index]
        elif "youtu.be/" in self.url:                           #For shortened URLs
            start_index = self.url.find(".be/")
            self.videoID = self.url[start_index + 4:]
        else:                                                   #For single videos
            self.videoID = self.url[start_index + 2:] 

    def saveThumbnail(self):
        thumbnail_url = 'http://img.youtube.com/vi/' + self.videoID + '/maxresdefault.jpg'
        thumbnail_url2 = 'http://img.youtube.com/vi/' + self.videoID + '/0.jpg'
        file_name = self.videoID + '.jpg'
        try:
            urllib.request.urlretrieve(thumbnail_url, file_name)
            print("Thumbnail acquired")
        except:
            urllib.request.urlretrieve(thumbnail_url2, file_name)


class ConvertingClass(QThread):
    log = pyqtSignal(str)
    
    def __init__(self, url, path):
        super(QThread, self).__init__()
        self.url = url
        self.dest_path = path
        try:
            if self.dest_path[-1] != "\\": #Just making sure our paths are done correctly
                self.dest_path += "\\"
        except:
            self.log.emit("[WARNING] Invalid destination path, set valid path in settings")
        print("class made")

    class MyLogger(object): #This is a nested class that references the coverting thread
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance
            
        def debug(self, msg):
            #print(msg)
            self.outer_instance.log.emit(msg)

        def warning(self, msg):
            #print(msg)
            pass

        def error(self, msg):
            #print(msg)
            pass

    def run(self):
        self.tg = thumbnailGetter(self.url)
        self.tg.saveThumbnail()
        self.logger = self.MyLogger(self)
        self.ydl_opts = {
                    'format': "bestaudio/best",
                    'audioquality': 0,
                    'forcetitle' : True,
                    'noplaylist' : True, #Modify this with variable
                    'age_limit' : 30,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'logger': self.logger,
                    'progress_hooks': [self.my_hook],
                        }
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([self.url])
            
        self.filename_path = os.getcwd() + "\\" + \
                             self.title + "-" + \
                             self.tg.videoID + ".mp3" #these two variables are the full path to them files
        self.filename_path_pic = os.getcwd() + "\\" + self.tg.videoID + ".jpg"

        try:
            self.embedTags()
        except Exception as e: #Make specific errors
            self.log.emit("[WARNING] Failed to embed tags")
            self.log.emit(e)
            
        self.cleanMove()
        self.log.emit("Finished")
        self.log.emit("=" * 30)

    def my_hook(self, d):
        if d['status'] == 'finished':
            self.log.emit('Done downloading, now converting ...')
            print("FILENAME" + d['filename'])
            self.title = d['filename'][:d['filename'].rfind(self.tg.videoID) - 1] #no idea when we get this, pretty sure its after the with clause

    def embedTags(self): #Embeds the ablum thumbnail and title
        audio = MP3(self.filename_path, ID3=ID3) #opening the converted file for tagging
        try:
           audio.add_tags()
        except Exception as e:
           print(e)
        audio.tags.add(
           APIC(                                    #writes cover art
              encoding=1,
              mime='image/jpg',
              type=3,
              desc=u'Cover',
              data=open(self.filename_path_pic, 'rb').read()
               )
            )
        audio["TIT2"] = TIT2(encoding=3, text=self.title) #writes track title
        audio.save()

    def cleanMove(self):
        os.remove(self.filename_path_pic)
        shutil.move(self.filename_path, self.dest_path + self.title + ".mp3")
