from pytube import YouTube

save_path = open(r'C:\Users\Enez\Downloads','w')
link = "https://www.youtube.com/watch?v=4KlRnvlxfHw&pp=ygURZ2VjZWxlciBrYXJhIHRyZW4%3D"

try:
    yt = YouTube(link)

except:
  print("Ag Hatasi")


mp4_streams = yt.streams.filter(file_extension='mp4').all()

d_video = mp4_streams[-1]

try:
    
    d_video.download(output_path=save_path)

    print("Basariyla İndirildi")
except:
    print("HATA!")