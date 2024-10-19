from PIL import Image

# Função para redimensionar uma imagem
def resize_image(image_path, output_path, size):
    """
    Redimensiona uma imagem para as dimensões especificadas.

    :param image_path: Caminho para a imagem original
    :param output_path: Caminho onde a imagem redimensionada será salva
    :param size: Tupla (largura, altura) para redimensionar a imagem
    """
    try:
        # Abre a imagem
        img = Image.open(image_path)
        # Redimensiona a imagem
        resized_img = img.resize(size)
        # Salva a imagem redimensionada
        resized_img.save(output_path)
        print(f"Imagem redimensionada para {size} e salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao redimensionar a imagem: {e}")

# Função para salvar uma imagem genérica
def save_image(image, output_path):
    """
    Salva uma imagem no caminho especificado.

    :param image: Objeto da imagem (Pillow Image)
    :param output_path: Caminho onde a imagem será salva
    """
    try:
        # Salva a imagem no caminho especificado
        image.save(output_path)
        print(f"Imagem salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao salvar a imagem: {e}")
