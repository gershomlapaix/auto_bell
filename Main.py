#
# Mongo.java This is a class for playing an audio
# @author Cedric & Souvede
#

from Playsound import Playsound
import time

class Main:
    def __init__(self, given_time):
        self.time = given_time.split(":")
    
    def run(self):
        while True:
            now = time.localtime()
            if(now.tm_hour == int(self.time[0]) and now.tm_min == int(self.time[1])):
                print("Harahiye kbx!!!")
                test_sound = Playsound("./audio/sample.mp3",5)
                test_sound.playSound()
                # time.sleep(60)
            else:
                print(now.tm_hour,":",now.tm_min,":",now.tm_sec,"\n")
                time.sleep(1)

#Main execution 
def main():
    test = Main("19:58")

    test.run()
    
main()