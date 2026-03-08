import flet as ft
import styles.variables as var

class ButtonBsc(ft.ElevatedButton):

    def __init__(self, text, color, fontcolor, command=None):
        super().__init__(content=ft.Text(text),on_click=command)

        self.bgcolor = color
        self.color = fontcolor
        self.width = float("inf")
        self.elevation = 0

        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=10,
            text_style=ft.TextStyle(
                size=14,
                weight=ft.FontWeight.BOLD,
            )
        )