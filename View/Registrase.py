import flet as ft
import styles.variables as var
import Component.forms.form as form
import Component.Button.buttonbsc as ButtonBsc


def main(page: ft.Page):
    page.title = "Dulceria"

    page.fonts = {
        "Montserrat": "fonts/Montserrat-Regular.ttf",
        "Montserrat-Bold": "fonts/Montserrat-Bold.ttf",
        "Montserrat-Medium": "fonts/Montserrat-Medium.ttf",
    }

    page.theme = ft.Theme(font_family="Montserrat")

    return ft.View(
        route="/register",
        controls=[
            ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        col=9,
                        bgcolor=var.color2,
                        alignment=ft.Alignment.CENTER,
                        content=ft.Container(
                            width=page.width * 0.35,  # 🔹 tamaño relativo
                            height=page.height * 0.8,  # 🔹 tamaño relativo
                            content=form.form([
                                ft.Text(
                                    "DULCERIA",
                                    size=30,
                                    color=var.color5,
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.TextField(
                                    label="Usuario",
                                    label_style=ft.TextStyle(color=var.color5),
                                    bgcolor=var.color2,
                                    width=float("inf")
                                ),
                                ft.TextField(
                                    label="Correo Electrónico",
                                    label_style=ft.TextStyle(color=var.color5),
                                    bgcolor=var.color2,
                                    width=float("inf")
                                ),
                                ft.TextField(
                                    label="Contraseña",
                                    password=True,
                                    label_style=ft.TextStyle(color=var.color5),
                                    bgcolor=var.color2,
                                    width=float("inf")
                                ),
                                ft.Container(
                                    col=12,
                                    bgcolor=var.color1,
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Column(
                                        controls=[
                                            ButtonBsc.ButtonBsc("Crear Cuenta", color=var.color3, fontcolor=var.color1),
                                            ButtonBsc.ButtonBsc("Iniciar Sesión", color=var.color1, fontcolor=var.color5, command=lambda _: page.go("/login"))
                                        ]
                                    )
                                )
                            ])
                        )
                    ),
                    ft.Container(
                        col=3,
                        bgcolor=var.color4
                    )
                ],
                expand=True,
                spacing=0
            )
        ]
        
    )