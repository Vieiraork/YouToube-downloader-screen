from pytube import YouTube

class Controller:
    def download_from_youtube(self, url: str) -> bool:
        video = YouTube(url=url)

        try:
            video.streams.\
                filter(progressive=True, file_extension='mp4').\
                    order_by('resolution').desc().first().download()
        except Exception as e:
            return False
        else:
            print('Sucesso, vídeo baixado com sucesso!')
            return True
