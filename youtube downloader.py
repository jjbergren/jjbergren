
#started 20210813
#JJ Bergren Ramirez
#youtube downloader


from pytube import YouTube
print("Let's save a video!")
link = input("Enter your forever favorite YouTube video: ")
yt = YouTube(link)

#video details
print("Title: ",yt.title)
print("Length: ",yt.length)

ys = yt.streams.get_highest_resolution()

ys.download()

print("ok it will be downloaded here",ys.exists_at_path)
print("Done!")


