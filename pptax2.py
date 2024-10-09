from flet import *

def main(page: Page):
    BG = '#BEBEBE'

    # Definición de la imagen del logo usando una ruta relativa
    img = Image(
        src="https://w7.pngwing.com/pngs/816/682/png-transparent-taxi-icon-taxi-logo-text-rectangle-logo-thumbnail.png",  # Usa la ruta relativa correcta
        width=45,
        height=45,
        fit=ImageFit.CONTAIN,
    )

    # Definición de la fila de imágenes con desplazamiento horizontal
    images = Row(expand=1, wrap=False, scroll="always")

    # Agregando imágenes a la fila
    for i in range(30):
        images.controls.append(
            Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=400,
                height=400,
                fit=ImageFit.COVER,
                border_radius=border_radius.all(10)
            )
        )

    # Container con Column para alinear imagen y fila de imágenes
    primer_pag_content = Container(
        content=Column(
            [
                img,      # Imagen centrada
                #images    # Fila de imágenes desplazables
            ],
            alignment=MainAxisAlignment.CENTER,               # Centra la columna verticalmente
            horizontal_alignment=CrossAxisAlignment.CENTER    # Centra la columna horizontalmente
        ),

        
    
        width=400,
        height=400,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=50),  # Ajuste del padding
    )

    # Añade el contenedor a la página
    page.add(primer_pag_content)
    page.add(images)

app(target=main)
