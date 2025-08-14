# 🍞 Toast Animation

A beautiful, lightweight Python package for creating animated toast notifications in Flet applications with smooth animations, progress bars, and hover-to-pause functionality.

![Toast screenshot](screenshots/intro.png)

![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![Flet](https://img.shields.io/badge/Flet-Compatible-green) ![License](https://img.shields.io/badge/License-MIT-blue)

## 📦 Installation

```bash
pip install toast_animation
```

## 🚀 Quick Start

```python
import flet as ft
from toast_animation import ModernToast

def main(page: ft.Page):
    def show_toast(e):
        ModernToast.success(page, "Hello World!")
    
    page.add(ft.ElevatedButton("Show Toast", on_click=show_toast))

ft.app(target=main)
```

![Toast screenshot](screenshots/basictoast.png)

## 🎨 Basic Usage

### Simple Toast Types
```python
# Success toast
ModernToast.success(page, "Operation completed!")

# Error toast  
ModernToast.error(page, "Something went wrong!")

# Warning toast
ModernToast.warning(page, "Please check your input!")

# Info toast
ModernToast.info(page, "Here's some information!")
```

### Positioning
```python
# Available positions: "top_left", "top_right", "top_center", 
#                     "bottom_left", "bottom_right", "bottom_center"
ModernToast.success(page, "Top center toast!", position="top_center")
```

### Duration Control
```python
# Custom duration (in seconds)
ModernToast.info(page, "This lasts 5 seconds", duration=5)
```

## ⚙️ Advanced Features

### Custom Content
Replace the default message with your own Flet controls:

```python
custom_content = ft.Row([
    ft.Icon(ft.Icons.DOWNLOAD, color="white", size=20),
    ft.Text("Download completed!", color="white", weight=ft.FontWeight.BOLD),
    ft.Icon(ft.Icons.CHECK_CIRCLE, color="white", size=16)
], spacing=8)

ModernToast(
    page,
    custom_content=custom_content,
    toast_type="success",
    duration=4
)
```
![Toast screenshot](screenshots/customtoast.png)

### Interactive Toasts
Create toasts with buttons and interactive elements:

```python
def handle_reply(e):
    print("Reply clicked!")

custom_content = ft.Column([
    ft.Row([
        ft.Icon(ft.Icons.MESSAGE, color="white", size=24),
        ft.Column([
            ft.Text("New Message", color="white", weight=ft.FontWeight.BOLD),
            ft.Text("John sent you a message", color="white", opacity=0.9)
        ], spacing=2, expand=True)
    ], spacing=12),
    ft.Row([
        ft.TextButton("Reply", 
            style=ft.ButtonStyle(color="white", bgcolor="rgba(255,255,255,0.2)"),
            on_click=handle_reply),
        ft.TextButton("Dismiss", 
            style=ft.ButtonStyle(color="white", bgcolor="rgba(255,255,255,0.1)"))
    ], alignment=ft.MainAxisAlignment.END, spacing=8)
], spacing=10)

ModernToast(page, custom_content=custom_content, duration=8)
```
![Toast screenshot](screenshots/message.png)

## 🎨 Custom Styling

### Dark Theme
```python
dark_style = {
    "bg_color": "#1F2937",
    "text_color": "#F9FAFB", 
    "icon_color": "#10B981",
    "progress_color": "#10B981",
    "border_color": "#374151",
    "close_color": "#9CA3AF"  # Proper contrast for dark theme
}

ModernToast.info(page, "Dark theme toast", custom_style=dark_style)
```

### Light/Minimal Theme
```python
light_style = {
    "bg_color": "#FFFFFF",
    "text_color": "#1F2937",
    "icon_color": "#6366F1", 
    "progress_color": "#6366F1",
    "border_color": "#E5E7EB",
    "close_color": "#6B7280",  # Dark close button for light background
    "shadow_opacity": 0.1
}

ModernToast.warning(page, "Clean minimal design", custom_style=light_style)
```

### Vibrant Style
```python
vibrant_style = {
    "bg_color": "#EC4899",
    "text_color": "#FFFFFF",
    "icon_color": "#FEF3C7",
    "progress_color": "#FEF3C7", 
    "border_color": "#F472B6",
    "width": 380,
    "border_radius": 15,
    "shadow_blur": 25
}

ModernToast.success(page, "Vibrant toast!", custom_style=vibrant_style)
```

## 🎛️ Configuration Options

### Basic Parameters
```python
ModernToast(
    page=page,                    # Required: Flet page instance
    message="Your message",       # Toast text
    toast_type="info",           # "success", "error", "warning", "info"
    duration=3,                  # Duration in seconds
    position="bottom_right",     # Toast position
    show_progress=True,          # Show progress bar
    pausable=True,              # Pause on hover
    show_dismiss_button=True    # Show close button
)
```

### Style Properties
| Property | Default | Description |
|----------|---------|-------------|
| `bg_color` | Type-specific | Background color |
| `text_color` | Type-specific | Text color |
| `icon_color` | Type-specific | Icon color |
| `progress_color` | Type-specific | Progress bar color |
| `close_color` | Type-specific | Close button color |
| `width` | `320` | Toast width |
| `border_radius` | `8` | Corner radius |
| `padding` | `12` | Internal padding |
| `shadow_blur` | `15` | Shadow blur radius |

## ✨ Features

- **🎯 Multiple Positions**: 6 positioning options
- **⏸️ Hover to Pause**: Automatically pauses timer on hover
- **📊 Progress Bar**: Visual countdown with smooth animation
- **🎨 Full Customization**: Override any visual aspect
- **🎪 Custom Content**: Use any Flet controls
- **⚡ Smooth Animations**: Fade and cascade effects
- **📱 Responsive**: Adapts to different screen sizes

## 🔄 Cascade Effect

Show multiple toasts with staggered timing:

```python
import flet as ft
from toast_animation import ModernToast
from threading import Timer

def main(page: ft.Page):
    page.title = "Toast Demo"
    page.theme_mode = ft.ThemeMode.DARK
    
    def show_cascade(e):
        ModernToast.success(page, "First toast!")
        Timer(0.5, lambda: ModernToast.info(page, "Second toast!")).start()
        Timer(1.0, lambda: ModernToast.warning(page, "Third toast!")).start()
    
    # Add the button to the page
    page.add(
        ft.ElevatedButton("Show Cascade Effect", on_click=show_cascade)
    )

ft.app(target=main)
```

![Toast screenshot](screenshots/cascade.png)

## 🎪 Bonus: Real-World App Examples

### 1. Social Media Notification
Perfect for social apps with message notifications:

```python
import flet as ft
from toast_animation import ModernToast
from threading import Timer

def main(page: ft.Page):
    page.title = "Toast Demo - Social Media Notification"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    
    def show_social_notification(e):
        def handle_reply(e):
            print("Opening reply interface...")
            # You could add another toast here showing "Reply window opened"
            ModernToast.info(page, "Reply window opened!", duration=2)

        def mark_as_read(e):
            print("Message marked as read")
            # You could add feedback toast
            ModernToast.success(page, "Message marked as read", duration=2)

        social_content = ft.Column([
            ft.Row([
                ft.CircleAvatar(
                    content=ft.Text("JD", color="white", weight=ft.FontWeight.BOLD),
                    bgcolor="#8B5CF6",
                    radius=20
                ),
                ft.Column([
                    ft.Text("John Doe", color="white", size=14, weight=ft.FontWeight.BOLD),
                    ft.Text("Hey! Are you free for coffee tomorrow?", 
                            color="white", size=12, opacity=0.9)
                ], spacing=2, expand=True),
                ft.Icon(ft.Icons.MESSAGE, color="#10B981", size=20)
            ], spacing=12),
            ft.Divider(color="rgba(255,255,255,0.2)", height=1),
            ft.Row([
                ft.TextButton("Reply", 
                    icon=ft.Icons.REPLY,
                    style=ft.ButtonStyle(
                        color="white",
                        bgcolor="rgba(16, 185, 129, 0.2)"
                    ),
                    on_click=handle_reply
                ),
                ft.TextButton("Mark Read",
                    icon=ft.Icons.DONE,
                    style=ft.ButtonStyle(
                        color="white", 
                        bgcolor="rgba(255,255,255,0.1)"
                    ),
                    on_click=mark_as_read
                )
            ], alignment=ft.MainAxisAlignment.END, spacing=8)
        ], spacing=12)

        ModernToast(
            page,
            custom_content=social_content,
            toast_type="info",
            duration=10,
            position="top_right",
            custom_style={
                "width": 400,
                "bg_color": "#1F2937",
                "border_radius": 12,
                "padding": 16,
                "border_color": "#374151"
            }
        )

    # Add UI elements to the page
    page.add(
        ft.Column([
            ft.Text("Social Media Toast Demo", 
                    size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Click the button to simulate receiving a message notification", 
                    opacity=0.8),
            ft.Divider(height=20),
            ft.ElevatedButton(
                "📱 Show Message Notification",
                icon=ft.Icons.NOTIFICATIONS,
                on_click=show_social_notification,
                style=ft.ButtonStyle(
                    bgcolor="#8B5CF6",
                    color="white"
                )
            ),
            ft.Text("💡 Try clicking 'Reply' or 'Mark Read' in the toast!", 
                    size=12, opacity=0.6, italic=True)
        ], spacing=10)
    )
ft.app(target=main)
```
![Social Media Toast](screenshots/socialmedia.png)

### 2. File Upload Progress
Great for file management apps:

```python
import flet as ft
from toast_animation import ModernToast

def main(page: ft.Page):
    page.title = "Toast Demo - File Upload Progress"
    page.theme_mode = ft.ThemeMode.LIGHT  # Light theme for this example
    page.padding = 20
    
    def show_upload_progress(e):
        def cancel_upload(e):
            print("Upload cancelled")
            ModernToast.warning(page, "Upload cancelled", duration=2)
        
        def view_file(e):
            print("Opening file viewer...")
            ModernToast.info(page, "Opening file viewer...", duration=2)
        
        def share_file(e):
            print("Opening share dialog...")
            ModernToast.info(page, "Share dialog opened", duration=2)
        
        upload_content = ft.Column([
            ft.Row([
                ft.Container(
                    content=ft.Icon(ft.Icons.UPLOAD_FILE, color="#3B82F6", size=24),
                    bgcolor="rgba(59, 130, 246, 0.1)",
                    border_radius=8,
                    padding=8
                ),
                ft.Column([
                    ft.Text("Upload Complete", color="#1F2937", 
                           weight=ft.FontWeight.BOLD, size=14),
                    ft.Text("project_files.zip (2.4 MB)", 
                           color="#6B7280", size=12)
                ], spacing=2, expand=True),
                ft.PopupMenuButton(
                    icon=ft.Icons.MORE_VERT,
                    icon_color="#6B7280",
                    items=[
                        ft.PopupMenuItem(text="View File", on_click=view_file),
                        ft.PopupMenuItem(text="Share", icon=ft.Icons.SHARE, on_click=share_file),
                    ]
                )
            ], spacing=12),
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.CLOUD_DONE, color="#10B981", size=16),
                    ft.Text("Synced to cloud", color="#10B981", size=12, weight=ft.FontWeight.W_500)
                ], spacing=6),
                bgcolor="rgba(16, 185, 129, 0.1)",
                border_radius=6,
                padding=ft.padding.symmetric(horizontal=8, vertical=4)
            )
        ], spacing=12)

        ModernToast(
            page,
            custom_content=upload_content,
            toast_type="success",
            duration=8,
            position="bottom_right",
            custom_style={
                "width": 380,
                "bg_color": "#FFFFFF",
                "border_color": "#E5E7EB",
                "border_radius": 12,
                "padding": 16,
                "shadow_blur": 20,
                "shadow_opacity": 0.1,
                "close_color": "#6B7280"
            }
        )

    # Add UI elements to the page
    page.add(
        ft.Column([
            ft.Text("File Upload Toast Demo", 
                    size=24, weight=ft.FontWeight.BOLD, color="#1F2937"),
            ft.Text("Click the button to simulate a completed file upload", 
                    opacity=0.8, color="#6B7280"),
            ft.Divider(height=20),
            ft.ElevatedButton(
                "📁 Show Upload Complete",
                icon=ft.Icons.CLOUD_UPLOAD,
                on_click=show_upload_progress,
                style=ft.ButtonStyle(
                    bgcolor="#3B82F6",
                    color="white"
                )
            ),
            ft.Text("💡 Try clicking the menu (⋮) in the toast to see options!", 
                    size=12, opacity=0.6, italic=True, color="#6B7280")
        ], spacing=10)
    )

ft.app(target=main)
```
![Upload Progress Toast](screenshots/file.png)

### 3. E-commerce Order Update
Perfect for shopping apps and order tracking:

```python
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
```
![E-commerce Toast](screenshots/e-commerce.png)

## 🎯 Best Practices

1. **Use appropriate colors**: Ensure good contrast between text and background
2. **Consider duration**: Longer messages need more time to read
3. **Don't overwhelm**: Limit concurrent toasts to avoid clutter
4. **Test on different themes**: Verify visibility in both light and dark modes
5. **Close button contrast**: Use `close_color` for proper visibility

## 📖 Complete Example

```python
import flet as ft
from toast_animation import ModernToast
from threading import Timer

def main(page: ft.Page):
    page.title = "Toast Demo"
    page.theme_mode = ft.ThemeMode.DARK
    
    def basic_toast(e):
        ModernToast.success(page, "Success! Operation completed.")
    
    def custom_toast(e):
        custom_style = {
            "bg_color": "#6366F1",
            "progress_color": "#FDE047",
            "width": 350,
            "border_radius": 12
        }
        ModernToast.info(page, "Custom styled toast!", custom_style=custom_style)
    
    def cascade_toasts(e):
        toasts = [
            ("success", "First toast!"),
            ("info", "Second toast!"), 
            ("warning", "Third toast!")
        ]
        for i, (toast_type, message) in enumerate(toasts):
            Timer(i * 0.5, lambda t=toast_type, m=message: 
                  getattr(ModernToast, t)(page, m)).start()
    
    page.add(
        ft.Text("Toast Animation Demo", size=24, weight=ft.FontWeight.BOLD),
        ft.Row([
            ft.ElevatedButton("Basic Toast", on_click=basic_toast),
            ft.ElevatedButton("Custom Style", on_click=custom_toast),
            ft.ElevatedButton("Cascade Effect", on_click=cascade_toasts)
        ], spacing=10)
    )

ft.app(target=main)
```
![Cascade Effect](screenshots/cascade.png)

## 📄 License

MIT License - feel free to use in your projects!

## 🤝 Contributing

Issues and pull requests are welcome on the [GitHub repository](https://github.com/heckerdev12/flet_toasty).

---

