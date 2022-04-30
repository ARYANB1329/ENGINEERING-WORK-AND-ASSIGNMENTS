from gtts import gTTS
import os
myText ="Text to Speech conversion using python"
language = 'en'
output = gTTS(text=myText,lang=language, slow=False)
output.save("output1.mp3")
os.system("start  output.mp3")

