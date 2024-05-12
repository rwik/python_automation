# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pytube import YouTube


def download_audio(url):
    try:
        video = YouTube(url)
        print("Title: ", video.title)
        audio = video.streams.get_audio_only()
        audio.download()
        print("Download complete")
    except Exception as e:
        print("Error : ", str(e))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = input("Enter youtube URL : ")
    download_audio(url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
