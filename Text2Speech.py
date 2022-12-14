from gtts import gTTS
import pyttsx3


# 方案1 : 只能识别英文
def transferSpeech(text: str, name: str):
    # tts = gTTS(text=text, lang='zh-tw')
    tts = gTTS(text=text, lang='zh-CN')
    tts.save(name + ".mp3")


#方案2
def pyttsx3Transfer():
    pp = pyttsx3.init()
    voices = pp.getProperty('voices')
    print(voices[0])
    # voices才支持中文版
    pp.setProperty('voice', voices[0].id)
    pp.say('Hello World')
    pp.save_to_file("我會繁體字", 'good.mp3')
    pp.runAndWait()
    pp.stop()


engine = pyttsx3.init()


def onWord(name, location, length):
    print('word', name, location, length)
    if location > 10:
      engine.stop()
    engine.connect('started-word', onWord)
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.save_to_file("The quick brown fox jumped over the lazy dog.", "intermmm.mp3")
    engine.runAndWait()


if __name__ == "__main__":
    # transferSpeech("哈哈哈", "hahaha")
    pyttsx3Transfer()
