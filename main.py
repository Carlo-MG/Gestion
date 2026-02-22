import flet as ft

def main(page: ft.Page):
    page.title = "Mi primera app"
    page.add(ft.Text("Hola mundo"))

ft.app(target=main)