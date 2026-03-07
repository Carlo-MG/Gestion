import flet as ft
import styles.variables as var


class form(ft.Container):

    def __init__(self, contenido):
        super().__init__()

        self.bgcolor = var.color1
        self.width = 400
        self.height = 600
        self.padding = 30
        self.border_radius = 10

        self.content = ft.Column(
            controls=contenido,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50
        )