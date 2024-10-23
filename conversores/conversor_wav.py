from moviepy.editor import AudioFileClip

def converterWAV (caminhoVideo, caminhoWAV):
    try:
        audio = AudioFileClip(caminhoVideo)
        audio.write_audiofile(caminhoWAV, codec = 'pcm_s16le')
        print('Conversão para WAV realizada com sucesso!')
    except Exception as e:
        print('Erro ao converter para WAV: ',   e)