from pygame import mixer 

path = "C:\\Users\\ipasha\\Downloads\\believer_song.mp3"
mixer.init()
mixer.music.load(path)
mixer.music.play()
