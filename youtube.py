"""
Este script permite o download de vídeos do YouTube utilizando a biblioteca `yt_dlp`.

Funções:
---------
1. download_youtube_video(url):
    - Descrição: Faz o download de um vídeo do YouTube com qualidade máxima de 1080p.
    - Parâmetros:
        - url (str): O link do vídeo do YouTube que será baixado.
    - Comportamento:
        - Configura as opções do `yt_dlp` para baixar apenas o melhor vídeo com altura máxima de 1080p.
        - Garante que apenas um vídeo seja baixado (sem playlists).
        - Define o caminho de saída do arquivo como `C:\Users\HP\Videos\` com o título do vídeo como nome do arquivo.
        - Utiliza o `yt_dlp.YoutubeDL` para realizar o download.

Execução:
---------
- Quando o script é executado diretamente, solicita ao usuário o link do vídeo do YouTube.
- Chama a função `download_youtube_video` para baixar o vídeo.
- Exibe uma mensagem de confirmação após o download ser concluído.

Dependências:
-------------
- yt_dlp: Certifique-se de que a biblioteca `yt_dlp` está instalada. Você pode instalá-la usando:
  `pip install yt-dlp`

Exemplo de uso:
---------------
1. Execute o script.
2. Insira o link do vídeo do YouTube quando solicitado.
    Por exemplo: `https://youtu.be/QGv2v2Ps_fk`
3. O script irá baixar o vídeo na melhor qualidade disponível (até 1080p) e salvá-lo na pasta especificada.
4. O nome do arquivo será o título do vídeo, com a extensão apropriada.
3. O vídeo será baixado na pasta `C:\Users\HP\Videos\` com o título do vídeo como nome do arquivo.

Nota:
-----
- Certifique-se de que você tem permissão para baixar o conteúdo do YouTube.
- O caminho de saída pode ser alterado modificando o valor da chave `outtmpl` em `ydl_opts`.
"""

import yt_dlp

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]',
        'noplaylist': True,
    }
    ydl_opts['outtmpl'] = r'C:\Users\HP\Videos\%(title)s.%(ext)s'
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Coloque o link do vídeo do YouTube aqui: ")
    download_youtube_video(video_url)
    print("Download feito!")