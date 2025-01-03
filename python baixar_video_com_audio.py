import yt_dlp  
def baixar_video_e_converter(url):  
    try:  
        # Opções para baixar o vídeo em MP4  
        video_ydl_opts = {  
            'format': 'bestvideo[ext=mp4]',  
            'outtmpl': '%(title)s.%(ext)s',  
        }  
        # Primeiro, baixa o vídeo em MP4  
        with yt_dlp.YoutubeDL(video_ydl_opts) as ydl:  
            ydl.download([url])  
        
        # Agora, baixa o áudio e converte para MP3  
        audio_ydl_opts = {  
            'format': 'bestaudio/best',  
            'postprocessors': [{  
                'key': 'FFmpegExtractAudio',  
                'preferredcodec': 'mp3',  
                'preferredquality': '192',  
            }],  
            'outtmpl': '%(title)s.%(ext)s',  
        }   
        with yt_dlp.YoutubeDL(audio_ydl_opts) as ydl:  
            ydl.download([url])  

        print("Vídeo em MP4 e áudio em MP3 baixados e convertidos com sucesso!")  

    except Exception as e:  
        print(f"Erro ao baixar vídeo: {e}")  
# Solicita a URL do usuário  
url = input("Digite a URL do vídeo do YouTube: ")  
baixar_video_e_converter(url)