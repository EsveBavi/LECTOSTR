import flet as ft
from collections import Counter
import re
import os
import sys

def main(page: ft.Page):
    # Configuración básica de la página
    page.title = "LECTOSTR"
    page.padding = 0
    page.window_icon = os.path.join(assets_dir, "icon.ico")  # Icono de la ventana
    
    # Función para análisis de texto
    def analyze_text(text):
        total_chars = len(text)
        symbols = len(re.findall(r'[^\w\s]', text))
        vowels = len(re.findall(r'[aeiouAEIOU]', text))
        consonants = len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text))
        
        char_count = Counter(text)
        if ' ' in char_count:
            del char_count[' ']
        most_common_char = char_count.most_common(1)[0][0] if char_count else ''
        
        return {
            "total": total_chars,
            "symbols": symbols,
            "vowels": vowels,
            "consonants": consonants,
            "most_common": most_common_char
        }

    # Función para procesar archivos
    def pick_files_result(e: ft.FilePickerResultEvent):
        if page.dialog and page.dialog.open:
            page.dialog.open = False
            page.update()
            
        if e.files:
            results_text.value = ""
            page.update()
            
            try:
                file_path = e.files[0].path
                
                if not file_path.lower().endswith('.txt'):
                    raise ValueError("Solo se permiten archivos de texto (.txt)")
                    
                with open(file_path, 'r', encoding='utf-8') as file:
                    text_content = file.read()
                
                results = analyze_text(text_content)
                
                results_text.value = f"-Cantidad de texto ingresado: {results['total']}\n" \
                                     f"-Cantidad de símbolos: {results['symbols']}\n" \
                                     f"-Cantidad de vocales: {results['vowels']}\n" \
                                     f"-Cantidad de consonantes: {results['consonants']}\n" \
                                     f"-Carácter que más se repite: '{results['most_common']}'\n\n" \
                                     f"¡ Gracias por usar LECTOSTR 😊!"
                
                show_success_dialog()
                page.update()
                
            except Exception as ex:
                print(f"Error processing file: {str(ex)}")
                show_error_dialog()
    
    # Configuración del selector de archivos
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)
    pick_files_dialog.allowed_extensions = ["txt"]

    # Diálogo de éxito
    success_dialog = ft.AlertDialog(
        content=ft.Container(
            content=ft.Column([
                ft.Image(src=f"{assets_dir}/sucess_msg.png", width=350, height=100),
                ft.ElevatedButton(
                    content=ft.Image(src=f"{assets_dir}/btn_okver.png", width=190, height=50),
                    bgcolor="#90EE90",
                    width=200,
                    height=50,
                    on_click=lambda _: close_success_dialog()
                )
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
            bgcolor="#90EE90",
            padding=15,
            border_radius=10,
            width=480,
            height=250,
        ),
        modal=True
    )
    
    # Diálogo de error
    error_dialog = ft.AlertDialog(
        content=ft.Container(
            content=ft.Column([
                ft.Image(src=f"{assets_dir}/error_msg.png", width=490, height=200),
                ft.Row([
                    ft.ElevatedButton(
                        content=ft.Image(src=f"{assets_dir}/btn_uploadotherfile.png", width=190, height=30),
                        bgcolor="#FFA07A", 
                        on_click=lambda _: load_another_file()
                    ),
                    ft.ElevatedButton(
                        content=ft.Image(src=f"{assets_dir}/btn_exit.png", width=80, height=30),
                        bgcolor="#FFA07A", 
                        on_click=lambda _: close_app()
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
            bgcolor="#FFA07A",
            padding=15,
            border_radius=10,
            width=500,
            height=300,
        ),
        modal=True
    )

    # Diálogo de información
    info_dialog = ft.AlertDialog(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Creado por:", size=16, weight=ft.FontWeight.BOLD),
                ft.Text("Esve_Bavi 💕", size=16, weight=ft.FontWeight.BOLD),
                ft.Text("Para la materia", size=14),
                ft.Text("PSPO", size=14),
                ft.ElevatedButton(
                    "OK", 
                    bgcolor="#9370DB",
                    color="white",
                    width=80,
                    height=30,
                    on_click=lambda _: close_info_dialog()
                )
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
            bgcolor="#E6E6FA",
            padding=10,
            border_radius=10,
            width=200,
            height=150,
        ),
        modal=True
    )
    
    # Agregar diálogos a la página
    page.overlay.append(success_dialog)
    page.overlay.append(error_dialog)
    page.overlay.append(info_dialog)

    # Funciones para manejar diálogos
    def show_success_dialog():
        success_dialog.open = True
        page.update()

    def close_success_dialog():
        success_dialog.open = False
        page.update()

    def show_error_dialog():
        error_dialog.open = True
        page.update()

    def load_another_file():
        error_dialog.open = False
        page.update()
        pick_files_dialog.pick_files()

    def close_app():
        page.window_close()

    def show_info():
        if success_dialog.open:
            success_dialog.open = False
        if error_dialog.open:
            error_dialog.open = False
        info_dialog.open = True
        page.update()
        
    def close_info_dialog():
        info_dialog.open = False
        page.update()

    # Encabezado con título e icono de información
    header = ft.Container(
        content=ft.Row(
            [
                ft.Text("LECTOSTR", size=30, weight=ft.FontWeight.BOLD),
                ft.Container(expand=True),
                ft.IconButton(
                    icon=ft.icons.INFO,
                    icon_color="orange",
                    icon_size=30,
                    tooltip="Información",
                    on_click=lambda e: show_info()
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=page.width,
        bgcolor="#B6F5ED",
        padding=ft.padding.all(30),
    )

    # Contenedor para subir archivos
    upload_container = ft.Container(
        content=ft.Row(
            [
                ft.Image(src=f"{assets_dir}/btn_uploadinfo.png", width=500, height=250)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        width=500,
        height=90,
        bgcolor="#B0E0E6",
        border_radius=10,
        on_click=lambda _: pick_files_dialog.pick_files()
    )

    # Contenedor para mostrar resultados
    results_container = ft.Stack([
        ft.Image(
            src=f"{assets_dir}/relsuthere.png",
            width=700,
            height=350,
            fit=ft.ImageFit.COVER,
            border_radius=10,
        ),
        ft.Container(
            content=ft.Column(
                [
                    results_text := ft.Text(
                        size=14,
                        color="white",
                        selectable=True,
                        no_wrap=False,
                        font_family="Consolas, monospace"
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10
            ),
            width=700,
            height=300,
            bgcolor=ft.colors.with_opacity(0.7, "#333333"),
            border_radius=10,
            padding=30,
            margin=ft.margin.only(top=50),
        )
    ])

    # Contenedor principal
    main_content = ft.Container(
        content=ft.Column(
            [
                ft.Container(height=20),
                upload_container,
                results_container
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=ft.padding.all(20),
    )

    # Agregar componentes a la página
    page.add(
        header,
        main_content
    )

# Determinar la ruta de assets para ejecutable o desarrollo
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # Ejecutando como archivo exe (PyInstaller)
    assets_dir = os.path.join(sys._MEIPASS, "assets")
else:
    # Ejecutando en desarrollo
    assets_dir = "assets"

# Iniciar la aplicación
ft.app(target=main, assets_dir=assets_dir)