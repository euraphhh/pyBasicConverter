from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError, VideoUnavailable, LiveStreamError
import os

def baixarAudio(url, caminhoAudio = 'audioDownload'):
    try:
        youtube = YouTube(url)
        audio = youtube.streams.filter(only_audio=True).first()
        if not os.path.exists(caminhoAudio):
            os.makedirs(caminhoAudio)
        print(f"Baixando: {audio.title}...")
        caminhoAudioCompleto = audio.download(output_path = caminhoAudio)
        print("Vídeo baixado com sucesso!")
        return caminhoAudioCompleto
    except RegexMatchError:
        print("Erro: URL do vídeo inválida.")
    except VideoUnavailable:
        print("Erro: Vídeo indisponível.")
    except LiveStreamError:
        print("Erro: Não é possível baixar transmissões ao vivo.")
    except Exception as e:
        print(f"Erro ao baixar vídeo: {e}")
        return None