import flet as ft
import View.InicioSesion as login_view

def main(page: ft.Page):

    def route_change(e):
        page.views.clear()

        if page.route == "/login":
            page.views.append(login_view.login_view(page))
        elif page.route == "/register":
            from View.Registrase import main as register_view
            page.views.append(register_view(page))
            
        page.update()

    page.on_route_change = route_change
    page.go("/login")

ft.run(main)