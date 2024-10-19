from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

# Função para converter uma imagem para escala de cinza
def apply_grayscale(image_path, output_path):
    """
    Converte uma imagem para escala de cinza.

    :param image_path: Caminho para a imagem original
    :param output_path: Caminho onde a imagem em escala de cinza será salva
    """
    try:
        # Abre a imagem
        img = Image.open(image_path)
        # Converte para escala de cinza
        grayscale_img = img.convert("L")
        # Salva a nova imagem
        grayscale_img.save(output_path)
        print(f"Imagem convertida para escala de cinza e salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao aplicar escala de cinza: {e}")

# Função para aplicar detecção de bordas
def apply_edge_detection(image_path, output_path):
    """
    Aplica um filtro de detecção de bordas em uma imagem.

    :param image_path: Caminho para a imagem original
    :param output_path: Caminho onde a imagem com as bordas detectadas será salva
    """
    try:
        # Abre a imagem
        img = Image.open(image_path)
        # Aplica o filtro de detecção de bordas
        edge_img = img.filter(ImageFilter.FIND_EDGES)
        # Salva a nova imagem
        edge_img.save(output_path)
        print(f"Detecção de bordas aplicada e imagem salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao aplicar detecção de bordas: {e}")

# Converte a imagem para escala de cinza e binariza
def binarize_image(image, threshold=128):
    """
    Converte a imagem para escala de cinza e aplica um limiar para binarização.
    """
    grayscale_img = image.convert("L")
    binary_img = grayscale_img.point(lambda p: 255 if p > threshold else 0)
    return binary_img

# Função para aplicar operação AND entre duas imagens
def apply_and(image1_path, image2_path, output_path):
    """
    Aplica a operação booleana AND pixel a pixel entre duas imagens.

    :param image1_path: Caminho para a primeira imagem
    :param image2_path: Caminho para a segunda imagem
    :param output_path: Caminho para salvar o resultado
    """
    try:
        img1 = Image.open(image1_path)
        img2 = Image.open(image2_path)

        img1 = binarize_image(img1)
        img2 = binarize_image(img2)

        and_img = Image.fromarray(np.bitwise_and(np.array(img1), np.array(img2)))
        and_img.save(output_path)
        print(f"Operação AND aplicada e imagem salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao aplicar operação AND: {e}")

# Função para aplicar operação OR entre duas imagens
def apply_or(image1_path, image2_path, output_path):
    """
    Aplica a operação booleana OR pixel a pixel entre duas imagens.

    :param image1_path: Caminho para a primeira imagem
    :param image2_path: Caminho para a segunda imagem
    :param output_path: Caminho para salvar o resultado
    """
    try:
        img1 = Image.open(image1_path)
        img2 = Image.open(image2_path)

        img1 = binarize_image(img1)
        img2 = binarize_image(img2)

        or_img = Image.fromarray(np.bitwise_or(np.array(img1), np.array(img2)))
        or_img.save(output_path)
        print(f"Operação OR aplicada e imagem salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao aplicar operação OR: {e}")

# Função para aplicar operação NOT em uma imagem
def apply_not(image_path, output_path):
    """
    Aplica a operação booleana NOT em uma imagem.

    :param image_path: Caminho para a imagem
    :param output_path: Caminho para salvar o resultado
    """
    try:
        img = Image.open(image_path)
        img = binarize_image(img)

        not_img = Image.fromarray(np.bitwise_not(np.array(img)))
        not_img.save(output_path)
        print(f"Operação NOT aplicada e imagem salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao aplicar operação NOT: {e}")

# Função para aplicar operação XOR entre duas imagens
def apply_xor(image1_path, image2_path, output_path):
    """
    Aplica a operação booleana XOR pixel a pixel entre duas imagens.

    :param image1_path: Caminho para a primeira imagem
    :param image2_path: Caminho para a segunda imagem
    :param output_path: Caminho para salvar o resultado
    """
    try:
        img1 = Image.open(image1_path)
        img2 = Image.open(image2_path)

        img1 = binarize_image(img1)
        img2 = binarize_image(img2)

        xor_img = Image.fromarray(np.bitwise_xor(np.array(img1), np.array(img2)))
        xor_img.save(output_path)
        print(f"Operação XOR aplicada e imagem salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao aplicar operação XOR: {e}")
        
# Função para normalizar os valores de pixel de uma imagem
def normalize_image(image_path, output_path):
    """
    Normaliza os valores de pixel da imagem para o intervalo [0, 255].

    :param image_path: Caminho para a imagem original
    :param output_path: Caminho para salvar a imagem normalizada
    """
    try:
        img = Image.open(image_path)
        img_array = np.array(img)

        # Normaliza os valores de pixel para o intervalo [0, 255]
        img_norm = (img_array - img_array.min()) * (255 / (img_array.max() - img_array.min()))
        img_norm = img_norm.astype(np.uint8)  # Converte para uint8

        # Cria uma nova imagem normalizada
        norm_img = Image.fromarray(img_norm)
        norm_img.save(output_path)
        print(f"Imagem normalizada e salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao normalizar a imagem: {e}")

# Função de normalização por saturação (limita os valores ao intervalo [0, 255])
def normalize_saturation(image_path, output_path):
    """
    Normaliza os valores de pixel da imagem aplicando saturação.
    Valores acima de 255 são limitados a 255 e valores abaixo de 0 são limitados a 0.

    :param image_path: Caminho para a imagem original
    :param output_path: Caminho para salvar a imagem normalizada
    """
    try:
        img = Image.open(image_path)
        img_array = np.array(img)

        # Aplica a normalização por saturação, limitando ao intervalo [0, 255]
        img_saturated = np.clip(img_array, 0, 255)

        # Cria uma nova imagem com os valores saturados
        norm_img = Image.fromarray(img_saturated.astype(np.uint8))
        norm_img.save(output_path)
        print(f"Imagem normalizada (saturação) e salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao normalizar a imagem (saturação): {e}")

# Função de normalização com wrapping (ajusta valores ciclicamente dentro do intervalo [0, 255])
def normalize_wrapping(image_path, output_path):
    """
    Normaliza os valores de pixel da imagem aplicando wrapping.
    Valores acima de 255 voltam para 0, e valores abaixo de 0 voltam para 255.

    :param image_path: Caminho para a imagem original
    :param output_path: Caminho para salvar a imagem normalizada
    """
    try:
        img = Image.open(image_path)
        img_array = np.array(img)

        # Aplica a normalização por wrapping, ajustando os valores dentro do intervalo [0, 255]
        img_wrapped = img_array % 256  # O valor 256 faz o wrapping (enrolamento) no intervalo [0, 255]

        # Cria uma nova imagem com os valores ajustados
        wrap_img = Image.fromarray(img_wrapped.astype(np.uint8))
        wrap_img.save(output_path)
        print(f"Imagem normalizada (wrapping) e salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao normalizar a imagem (wrapping): {e}")