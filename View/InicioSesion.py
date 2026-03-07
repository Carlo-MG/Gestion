import flet as ft
import styles.variables as var
import Component.forms.form as form
import Component.Button.buttonbsc as ButtonBsc

def main(page: ft.Page):
    page.title = "Dulceria"
    
    page.fonts = {
        'Montserrat': 'fonts/Montserrat-Regular.ttf',
        'Montserrat-Bold': 'fonts/Montserrat-Bold.ttf',
        'Montserrat-Medium': 'fonts/Montserrat-Medium.ttf'
    }
    
    page.theme = ft.Theme(
        font_family="Montserrat",
    )

    page.add(
        ft.ResponsiveRow(
            controls=[
                ft.Container(
                    col=9,
                    bgcolor=var.color2,
                    alignment=ft.Alignment.CENTER,
                    content=form.form([
                        ft.Text("DULCERIA", size=30, color=var.color5, weight=ft.FontWeight.BOLD),
                        ft.TextField(label="Usuario", label_style=ft.TextStyle(color=var.color5), bgcolor=var.color2),
                        ft.TextField(label="Contraseña", password=True, label_style=ft.TextStyle(color=var.color5), bgcolor=var.color2),
                        ButtonBsc.ButtonBsc("Iniciar Sesion")
                    ])
                ),
                ft.Container(
                    col=3,
                    bgcolor=var.color4
                )
            ],
            expand=True,
            spacing=0
        )
    )