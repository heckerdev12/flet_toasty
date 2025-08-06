import flet as ft
from toast_animation import ModernToast

def main(page: ft.Page):
    def show_toast(e):
        toast = ModernToast(
            page,
            message="This is a toast notification!",
            toast_type="info",
            duration=3,
            position="bottom_right"
        )
        toast.show()

    page.add(ft.ElevatedButton("Show Toast", on_click=show_toast))

ft.app(target=main)
