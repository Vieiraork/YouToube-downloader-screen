import flet as ft
from controller import Controller

def main(page: ft.Page):
    page.title = "YouTube Downloader"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    label = ft.Text("Link do vídeo", text_align="center")
    text_url = ft.TextField(value="", text_align=ft.TextAlign.LEFT, width=500)
    controller = Controller()

    def download_video(e):
        res = controller.download_from_youtube(text_url.value)
        if res:
            text_url.value = ""
        page.update()

    row_texto = ft.Row(
                [
                    text_url,
                ],
                alignment=ft.MainAxisAlignment.CENTER
    )

    row_botao = ft.Row(
                [
                    ft.ElevatedButton('Baixar Vídeo', icon=ft.icons.DOWNLOAD, on_click=download_video)
                ],
                alignment=ft.MainAxisAlignment.CENTER
    )

    texto = ft.Row(
        [
            label,
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    page.add(
        ft.Column(
            [
                texto,
                row_texto,
                row_botao
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )