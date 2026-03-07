import flet as ft
import styles.variables as var

class ButtonBsc(ft.ElevatedButton):

    def __init__(self, text):
        super().__init__(content=ft.Text(text))

        self.bgcolor = var.color3
        self.color = var.color1
        self.width = 300
        self.height = 50

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=10,
            text_style=ft.TextStyle(
                size=14,
                weight=ft.FontWeight.BOLD
            )
        )