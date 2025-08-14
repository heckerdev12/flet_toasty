import flet as ft
from toast_animation import ModernToast


def main(page: ft.Page):
    page.title = "Price Drop Alert Demo"
    page.padding = 20
    
    def show_price_drop_alert(e):
        def view_product(e):
            print("Opening product page...")
            ModernToast.success(page, "Product page opened!", duration=2)
        
        def add_to_cart(e):
            print("Adding to cart...")
            ModernToast.success(page, "Added to cart!", duration=2)
        
        # Simple price drop content
        price_drop_content = ft.Column([
            ft.Row([
                ft.Icon(ft.Icons.TRENDING_DOWN, color="#10B981", size=24),
                ft.Column([
                    ft.Text("Price Drop Alert!", 
                           color="white", 
                           size=16, 
                           weight=ft.FontWeight.BOLD),
                    ft.Text("MacBook Pro M3", 
                           color="white", 
                           size=14),
                    ft.Row([
                        ft.Text("$2,199", 
                               color="white", 
                               size=12, 
                               opacity=0.6,
                               style=ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)),
                        ft.Text("$1,799", 
                               color="#10B981", 
                               size=14, 
                               weight=ft.FontWeight.BOLD),
                        ft.Container(
                            content=ft.Text("18% OFF", 
                                           color="white", 
                                           size=10,
                                           weight=ft.FontWeight.BOLD),
                            bgcolor="#EF4444",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=6, vertical=2)
                        )
                    ], spacing=8)
                ], spacing=4, expand=True)
            ], spacing=12),
            
            ft.Row([
                ft.OutlinedButton(
                    "View Product",
                    icon=ft.Icons.VISIBILITY,
                    style=ft.ButtonStyle(
                        color="white",
                        side=ft.BorderSide(width=1, color="white")
                    ),
                    on_click=view_product
                ),
                ft.ElevatedButton(
                    "Add to Cart",
                    icon=ft.Icons.SHOPPING_CART,
                    style=ft.ButtonStyle(
                        bgcolor="#10B981",
                        color="white"
                    ),
                    on_click=add_to_cart
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=5, color=ft.Colors.TRANSPARENT),
        ], spacing=16,)
        
        ModernToast(
            page,
            custom_content=price_drop_content,
            toast_type="success",
            duration=6,
            content_spacing=10,
            position="top_right",
            custom_style={
                "width": 350,
                "bg_color": "#1F2937",
                "border_radius": 12,
                "padding": 20,
                "shadow_blur": 20,
                "shadow_opacity": 0.3
            }
        )
    
    # Simple UI
    page.add(
        ft.Column([
            ft.Text("💰 Price Drop Alert Demo",
                     size=28, 
                     weight=ft.FontWeight.BOLD,
                     text_align=ft.TextAlign.CENTER),
            ft.Text("Get notified when your favorite products go on sale!",
                     size=16,
                     opacity=0.8,
                     text_align=ft.TextAlign.CENTER),
            
            ft.Container(height=40),
            
            ft.Container(
                content=ft.ElevatedButton(
                    "🔔 Show Price Drop Alert",
                    icon=ft.Icons.TRENDING_DOWN,
                    on_click=show_price_drop_alert,
                    style=ft.ButtonStyle(
                        bgcolor="#10B981",
                        color="white",
                        padding=ft.padding.symmetric(horizontal=30, vertical=15)
                    ),
                    height=50
                ),
                alignment=ft.alignment.center
            ),
            
            ft.Container(height=30),
            
            ft.Container(
                content=ft.Column([
                    ft.Text("✨ Features:",
                             size=16, 
                             weight=ft.FontWeight.BOLD),
                    ft.Text("• Interactive buttons in the toast notification"),
                    ft.Text("• Price comparison with discount percentage"),
                    ft.Text("• Modern design with smooth animations"),
                    ft.Text("• Click 'View Product' or 'Add to Cart' in the toast!")
                ], spacing=8),
                bgcolor="#2D3748",
                border_radius=12,
                padding=20
            )
        ], 
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )


if __name__ == "__main__":
    ft.app(target=main)