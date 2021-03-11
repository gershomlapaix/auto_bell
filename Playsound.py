#
# Mongo.java This is a class for playing an audio
# @author Cedric & Souvede
#

from pygame import mixer
import time

mixer.init()


class Playsound:
    def __init__(self, path, duration):
        self.path = path
        self.duration = duration

    def playSound(self):
        sound_player = mixer.Sound(self.path)
        sound_player.play()
        time.sleep(self.duration)
        sound_player.stop()

# Main execution
# def main():
#     test_sound = Playsound("./audio/sample.mp3", 5)

#     test_sound.playSound()

# main()
