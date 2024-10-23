import os
from downloader import baixarAudio
from conversores import converterMP3, converterWAV


def main():
    print("Bem-vindo ao Conversor de Vídeo para Áudio!")
    urlVideo = input("Digite a URL do vídeo que deseja converter: ")
    caminhoAudio = baixarAudio(urlVideo)
    if caminhoAudio:
        formatoConvert = input("Digite o formato que deseja converter (MP3 ou WAV): ").upper()

        if formatoConvert == 'MP3':
            caminho_mp3 = os.path.splitext(caminhoAudio)[0] + '.mp3'
            converterMP3(caminhoAudio, caminho_mp3)
        elif formatoConvert == 'WAV':
            caminho_wav = os.path.splitext(caminhoAudio)[0] + '.wav'
            converterWAV(caminhoAudio, caminho_wav)
        else:
            print("Formato de conversão inválido. Tente novamente.")

if __name__ == '__main__':
    main()