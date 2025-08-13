import flet as ft
from threading import Timer
from toast_animation import ModernToast

def main(page: ft.Page):
    page.title = "Modern Toast Demo"
    page.theme_mode = ft.ThemeMode.DARK

    def show_basic_toast(e):
        ModernToast.info(
            page,
            message="This is a basic info toast!",
            duration=4,
            show_progress=True
        )

    def show_success_toast(e):
        ModernToast(
            page,
            message="Operation completed successfully!",
            duration=3,
            show_dismiss_button=True,
            pausable=False,
            show_progress=True,
            content_spacing=8
        )

    def show_error_toast(e):
        ModernToast.error(
            page,
            message="An error occurred while processing!",
            duration=5
        )

    def show_warning_toast(e):
        ModernToast.warning(
            page,
            message="This is a warning message!",
            duration=4
        )

    def show_cascade_toasts(e):
        ModernToast.success(page, "First toast in cascade!")
        Timer(0.5, lambda: ModernToast.info(page, "Second toast!")).start()
        Timer(1.0, lambda: ModernToast.warning(page, "Third toast!")).start()
        Timer(1.5, lambda: ModernToast.error(page, "Last toast!")).start()

    def show_custom_content_simple(e):
        custom_content = ft.Row([
            ft.Icon(ft.Icons.DOWNLOAD, color="white", size=20),
            ft.Text("Download completed!", color="white", size=14, weight=ft.FontWeight.W_500),
            ft.Icon(ft.Icons.CHECK_CIRCLE, color="white", size=16)
        ], alignment=ft.MainAxisAlignment.START, spacing=8)

        ModernToast(
            page,
            custom_content=custom_content,
            toast_type="success",
            duration=5,
            show_progress=True
        )

    def show_custom_content_advanced(e):
        custom_content = ft.Column([
            ft.Row([
                ft.Icon(ft.Icons.UPLOAD_FILE, color="white", size=24),
                ft.Column([
                    ft.Text("Uploading file...", color="white", size=14, weight=ft.FontWeight.W_600),
                    ft.Text("document.pdf (2.3 MB)", color="white", size=12, opacity=0.8)
                ], spacing=2, expand=True),
                ft.IconButton(
                    icon=ft.Icons.CLOSE,
                    icon_color="white",
                    icon_size=18,
                    tooltip="Cancel upload"
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.ProgressBar(
                value=0.7,
                color="white",
                bgcolor="rgba(255,255,255,0.3)",
                height=4
            )
        ], spacing=8, tight=True)

        ModernToast(
            page,
            custom_content=custom_content,
            toast_type="info",
            duration=6,
            show_progress=False,
            custom_style={"width": 350, "padding": 16}
        )

    def show_custom_content_interactive(e):
        def handle_action(action_type):
            def handler(e):
                print(f"Action clicked: {action_type}")
            return handler

        custom_content = ft.Column([
            ft.Row([
                ft.Icon(ft.Icons.NOTIFICATIONS, color="white", size=24),
                ft.Column([
                    ft.Text("New message received", color="white", size=14, weight=ft.FontWeight.W_600),
                    ft.Text("John Doe sent you a message", color="white", size=12, opacity=0.9)
                ], spacing=2, expand=True)
            ], spacing=12),
            ft.Row([
                ft.TextButton(
                    "Reply",
                    style=ft.ButtonStyle(
                        color="white",
                        bgcolor="rgba(255,255,255,0.2)"
                    ),
                    on_click=handle_action("reply")
                ),
                ft.TextButton(
                    "Mark as Read",
                    style=ft.ButtonStyle(
                        color="white",
                        bgcolor="rgba(255,255,255,0.1)"
                    ),
                    on_click=handle_action("mark_read")
                )
            ], alignment=ft.MainAxisAlignment.END, spacing=8)
        ], spacing=10, tight=True)

        ModernToast(
            page,
            custom_content=custom_content,
            toast_type="info",
            duration=8,
            show_progress=True,
            custom_style={"width": 380, "padding": 16}
        )

    def show_custom_style_toast(e):
        custom_style = {
            "bg_color": "#6366F1",
            "text_color": "white",
            "icon_color": "#FDE047",
            "progress_color": "#FDE047",
            "progress_height": 4,
            "width": 400,
            "padding": 20,
            "border_radius": 12,
            "border_width": 2,
            "border_color": "#8B5CF6",
            "icon_size": 28,
            "text_size": 16,
            "text_weight": ft.FontWeight.BOLD,
            "shadow_blur": 20,
            "shadow_spread": 2,
            "shadow_opacity": 0.4
        }

        ModernToast(
            page,
            message="This is a custom styled toast with enhanced colors and styling!",
            toast_type="info",
            duration=6,
            custom_style=custom_style
        )

    def show_gradient_style_toast(e):
        custom_style = {
            "bg_color": "#EC4899",
            "text_color": "#FFFFFF",
            "icon_color": "#FEF3C7",
            "progress_color": "#FEF3C7",
            "progress_height": 5,
            "width": 380,
            "padding": 18,
            "border_radius": 15,
            "border_width": 1,
            "border_color": "#F472B6",
            "shadow_blur": 25,
            "shadow_x": 0,
            "shadow_y": 8,
            "shadow_opacity": 0.35
        }

        ModernToast.success(
            page,
            message="Beautiful gradient-style toast with custom progress bar!",
            duration=5,
            custom_style=custom_style
        )

    def show_dark_theme_toast(e):
        custom_style = {
            "bg_color": "#1F2937",
            "text_color": "#F9FAFB",
            "icon_color": "#10B981",
            "progress_color": "#10B981",
            "progress_height": 3,
            "border_width": 1,
            "border_color": "#374151",
            "close_color": "#9CA3AF",
            "shadow_opacity": 0.5
        }

        ModernToast.info(
            page,
            message="Dark theme toast with visible progress bar",
            duration=7,
            custom_style=custom_style
        )

    def show_minimal_toast(e):
        custom_style = {
            "bg_color": "#FFFFFF",
            "text_color": "#1F2937",
            "icon_color": "#6366F1",
            "progress_color": "#6366F1",
            "progress_height": 2,
            "border_width": 1,
            "border_color": "#E5E7EB",
            "border_radius": 6,
            "shadow_blur": 10,
            "shadow_opacity": 0.1
        }

        ModernToast.warning(
            page,
            message="Clean minimal toast design",
            duration=4,
            custom_style=custom_style
        )

    # UI Layout
    page.add(
        ft.Column([
            ft.Text("Modern Toast Demo", size=28, weight=ft.FontWeight.BOLD),
            ft.Divider(height=20),

            ft.Text("Basic Toast Types", size=20, weight=ft.FontWeight.W_600),
            ft.Row([
                ft.ElevatedButton("Info Toast", on_click=show_basic_toast),
                ft.ElevatedButton("Success Toast", on_click=show_success_toast),
                ft.ElevatedButton("Error Toast", on_click=show_error_toast),
                ft.ElevatedButton("Warning Toast", on_click=show_warning_toast),
            ], wrap=True, spacing=10),

            ft.Divider(height=20),
            ft.Text("Cascade Effect", size=20, weight=ft.FontWeight.W_600),
            ft.ElevatedButton("Show Cascade Toasts", on_click=show_cascade_toasts),

            ft.Divider(height=20),
            ft.Text("Custom Content Examples", size=20, weight=ft.FontWeight.W_600),
            ft.Row([
                ft.ElevatedButton("Simple Custom", on_click=show_custom_content_simple),
                ft.ElevatedButton("Advanced Custom", on_click=show_custom_content_advanced),
                ft.ElevatedButton("Interactive Toast", on_click=show_custom_content_interactive),
            ], wrap=True, spacing=10),

            ft.Divider(height=20),
            ft.Text("Enhanced Custom Styling (v0.2)", size=20, weight=ft.FontWeight.W_600),
            ft.Row([
                ft.ElevatedButton("Custom Colors", on_click=show_custom_style_toast),
                ft.ElevatedButton("Gradient Style", on_click=show_gradient_style_toast),
                ft.ElevatedButton("Dark Theme", on_click=show_dark_theme_toast),
                ft.ElevatedButton("Minimal Style", on_click=show_minimal_toast),
            ], wrap=True, spacing=10),
        ], spacing=15, scroll=ft.ScrollMode.AUTO)
    )

if __name__ == "__main__":
    ft.app(target=main)
