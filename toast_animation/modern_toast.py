import flet as ft
from threading import Timer

class ModernToast:
    TOAST_TYPES = {
        "success": {
            "icon": ft.Icons.CHECK_CIRCLE_ROUNDED,
            "colors": {
                "bg": "#10B981",
                "text": "#FFFFFF"
            }
        },
        "error": {
            "icon": ft.Icons.ERROR_ROUNDED,
            "colors": {
                "bg": "#EF4444",
                "text": "#FFFFFF"
            }
        },
        "warning": {
            "icon": ft.Icons.WARNING_ROUNDED,
            "colors": {
                "bg": "#F59E0B",
                "text": "#FFFFFF"
            }
        },
        "info": {
            "icon": ft.Icons.INFO_ROUNDED,
            "colors": {
                "bg": "#3B82F6",
                "text": "#FFFFFF"
            }
        }
    }

    def __init__(self, page: ft.Page, message: str, toast_type: str = "info", duration: int = 3, play_sound: bool = False, position: str = "bottom_right"):
        self.page = page
        self.message = message
        self.toast_type = toast_type if toast_type in self.TOAST_TYPES else "info"
        self.duration = duration
        self.play_sound = play_sound
        self.position = position
        self._init_toast()
        self._ensure_toast_stack()
        self.show()

    def _init_toast(self):
        toast_style = self.TOAST_TYPES[self.toast_type]
        self.toast_content = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=toast_style["icon"],
                        color=toast_style["colors"]["text"],
                        size=24
                    ),
                    ft.Text(
                        value=self.message,
                        color=toast_style["colors"]["text"],
                        size=14,
                        weight=ft.FontWeight.W_500,
                        expand=True,
                        no_wrap=False,
                        max_lines=3
                    ),
                    ft.IconButton(
                        icon=ft.Icons.CLOSE_ROUNDED,
                        icon_color=toast_style["colors"]["text"],
                        icon_size=20,
                        on_click=self.dismiss,
                        tooltip="Dismiss"
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=toast_style["colors"]["bg"],
            border_radius=8,
            padding=12
        )

        self.toast_container = ft.Container(
            content=self.toast_content,
            width=320,
            opacity=0,
            animate_opacity=300,
            animate_position=300,
        )

    def _ensure_toast_stack(self):
        if not hasattr(self.page, "toast_stack"):
            self.page.toast_stack = ft.Stack(controls=[])
            self.page.overlay.append(self.page.toast_stack)
            self.page.update()

    def show(self):
        if self.toast_container not in self.page.toast_stack.controls:
            self.page.toast_stack.controls.append(self.toast_container)
            self._update_toast_positions()
            self.toast_container.opacity = 1
            self._safe_update(self.page)
            Timer(self.duration, self.dismiss).start()

    def _update_toast_positions(self):
        for index, toast_container in enumerate(self.page.toast_stack.controls):
            offset = index * 80  # Adjust this value to change the spacing between toasts
            if self.position == "top_left":
                toast_container.left = 20
                toast_container.top = 20 + offset
            elif self.position == "top_right":
                toast_container.right = 20
                toast_container.top = 20 + offset
            elif self.position == "bottom_left":
                toast_container.left = 20
                toast_container.bottom = 20 + offset
            elif self.position == "bottom_right":
                toast_container.right = 20
                toast_container.bottom = 20 + offset
            elif self.position == "top_center":
                toast_container.top = 20 + offset
                toast_container.left = (self.page.width - toast_container.width) / 2
            elif self.position == "bottom_center":
                toast_container.bottom = 20 + offset
                toast_container.left = (self.page.width - toast_container.width) / 2

    def dismiss(self, e=None):
        if self.toast_container in self.page.toast_stack.controls:
            self.toast_container.opacity = 0
            self._safe_update(self.toast_container)
            Timer(0.3, self._remove_from_toast_stack).start()

    def _remove_from_toast_stack(self):
        if self.toast_container in self.page.toast_stack.controls:
            self.page.toast_stack.controls.remove(self.toast_container)
            self._update_toast_positions()
            self._safe_update(self.page)

    def _safe_update(self, control):
        try:
            if hasattr(self.page, '_session_id'):
                if isinstance(control, ft.Container):
                    control.update()
                elif isinstance(control, ft.Page):
                    control.update()
        except Exception as e:
            print(f"Error updating control: {e}")
