from PIL import Image, ImageDraw, ImageFont


def add_watermark(image_path, watermark_text, output_path):
    # Cargar la imagen original y Crear una copia de la imagen original para agregar la marca de agua
    image = Image.open(image_path)
    watermarked_image = image.copy()

    # Obtener el tamaño de la imagen
    width, height = image.size

    # Crear un objeto de dibujo
    draw = ImageDraw.Draw(watermarked_image)

    # Especificar el texto de la marca de agua y su fuente
    text = watermark_text
    font = ImageFont.truetype("arial.ttf", 20)

    # Obtener el cuadro delimitador del texto de la marca de agua utilizando textbbox()
    text_bbox = draw.textbbox((0, 0), text, font=font)

    # Obtener las dimensiones de ancho y alto del cuadro delimitador
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calcular las coordenadas para centrar el texto en la imagen
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Agregar el texto de la marca de agua a la imagen
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

    # Guardar la imagen con la marca de agua en el archivo de salida
    watermarked_image.save(output_path)


# Ejemplo de uso
image_path = "IMG_20220601_150914403.jpg"
watermark_text = "Mi marca de agua"
output_path = "imagen_con_marca_de_agua.jpg"

add_watermark(image_path, watermark_text, output_path)