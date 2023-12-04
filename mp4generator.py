import cv2
import os
import re

def extrair_numero_do_nome(nome_arquivo):
    # Use uma expressão regular para extrair números do nome do arquivo
    match = re.search(r'\d+\.\d+', nome_arquivo)
    if match:
        return float(match.group())
    else:
        return float('inf')  # Se não houver número, coloque-o no final da ordenação

def ordenar_arquivos_numericamente(diretorio):
    arquivos = os.listdir(diretorio)
    arquivos_ordenados = sorted(arquivos, key=extrair_numero_do_nome)
    return arquivos_ordenados

def criar_video(diretorio_imagens, nome_video_saida='output.mp4', fps=30):
    imgorneadas = ordenar_arquivos_numericamente(diretorio_imagens)
    imagens = [img for img in imgorneadas if img.endswith(".png")]

    # Obtém as dimensões da primeira imagem para configurar o vídeo
    img = cv2.imread(os.path.join(diretorio_imagens, imagens[0]))
    altura, largura, _ = img.shape

    # Configuração do objeto VideoWriter
    video_saida = cv2.VideoWriter(nome_video_saida, cv2.VideoWriter_fourcc(*'mp4v'), fps, (largura, altura))

    for imagem in imagens:
        imagem_path = os.path.join(diretorio_imagens, imagem)
        img = cv2.imread(imagem_path)

        # Adiciona o nome do arquivo no canto inferior direito
        fonte = cv2.FONT_HERSHEY_SIMPLEX
        texto = imagem
        posicao_texto = (10, altura - 10)  # Posição do texto no canto inferior esquerdo
        cor = (0, 0, 0)  # Cor do texto (branco)
        espessura = 1  # Espessura da fonte

        cv2.putText(img, texto, posicao_texto, fonte, 0.5, cor, espessura, cv2.LINE_AA)

        video_saida.write(img)

    # Libera o recurso VideoWriter e fecha o vídeo
    video_saida.release()

if __name__ == "__main__":
    diretorio_imagens = "./"
    nome_video_saida = "output2.mp4"
    fps = 30

    criar_video(diretorio_imagens, nome_video_saida, fps)
