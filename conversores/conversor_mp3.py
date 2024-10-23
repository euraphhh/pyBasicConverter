from moviepy.editor import AudioFileClip

def converterMP3 (caminhoAudio, caminhoMP3):
    try:
        audio = AudioFileClip(caminhoAudio)
        audio.write_audiofile(caminhoMP3, codec = 'libmp3lame')
        print('Conversão para MP3 realizada com sucesso!')
    except Exception as e:
        print('Erro ao converter para MP3: ',   e)