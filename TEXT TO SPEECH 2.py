from gtts import gTTS
import os
fh = open("test.txt", "r")
myText = fh.read().replace("\n", "")
output = gTTS(text=myText, lang='en', slow=False)
output.save("output.mp3")
fh.close()
os.system("start  output.mp3")
