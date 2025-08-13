import flet as ft
from threading import Timer
import time

class ModernToast:
    TOAST_TYPES = {
        "success": {
            "icon": ft.Icons.CHECK_CIRCLE_ROUNDED,
            "colors": {
                "bg": "#10B981",
                "text": "#FFFFFF",
                "progress": "#FFFFFF"
            }
        },
        "error": {
            "icon": ft.Icons.ERROR_ROUNDED,
            "colors": {
                "bg": "#EF4444",
                "text": "#FFFFFF",
                "progress": "#FFFFFF"
            }
        },
        "warning": {
            "icon": ft.Icons.WARNING_ROUNDED,
            "colors": {
                "bg": "#F59E0B",
                "text": "#FFFFFF",
                "progress": "#FFFFFF"
            }
        },
        "info": {
            "icon": ft.Icons.INFO_ROUNDED,
            "colors": {
                "bg": "#3B82F6",
                "text": "#FFFFFF",
                "progress": "#FFFFFF"
            }
        }
    }

    def __init__(
        self,
        page: ft.Page,
        message: str = "",
        toast_type: str = "info",
        duration: int = 3,
        position: str = "bottom_right",
        show_progress: bool = True,
        pausable: bool = True,
        custom_content: ft.Control = None,
        custom_style: dict = None,
        content_spacing: int = 8,
        show_dismiss_button: bool = True,
    ):
        self.page = page
        self.message = message
        self.toast_type = toast_type if toast_type in self.TOAST_TYPES else "info"
        self.duration = duration
        self.original_duration = duration
        self.position = position
        self.show_progress = show_progress
        self.pausable = pausable
        self.custom_content = custom_content
        self.custom_style = custom_style or {}
        self.content_spacing = content_spacing
        self.show_dismiss_button = show_dismiss_button

        # Initialize timing variables
        self.timer = None
        self.start_time = None
        self.remaining_time = duration
        self.is_paused = False
        self.progress_timer = None
        self.progress_start_time = None
        self.progress_update_timer = None
        self.total_progress_elapsed = 0  # Track total elapsed time for progress

        self._init_toast()
        self._ensure_toast_stack()
        self.show()

    def _get_style_value(self, key: str, default_value):
        """Get style value from custom_style or fall back to default value"""
        if key in self.custom_style:
            return self.custom_style[key]
        if isinstance(default_value, str) and '.' in default_value:
            value = self.TOAST_TYPES[self.toast_type]
            for part in default_value.split('.'):
                value = value[part]
            return value
        return default_value

    def _init_toast(self):
        toast_style = self.TOAST_TYPES[self.toast_type]

        # Main content (either custom or default)
        if self.custom_content:
            main_content = self.custom_content
        else:
            content_controls = []

            # Icon
            if self._get_style_value("show_icon", True):
                content_controls.append(
                    ft.Icon(
                        name=self._get_style_value("icon", toast_style["icon"]),
                        color=self._get_style_value("icon_color", toast_style["colors"]["text"]),
                        size=self._get_style_value("icon_size", 24)
                    )
                )

            # Message text
            if self.message:
                content_controls.append(
                    ft.Text(
                        value=self.message,
                        color=self._get_style_value("text_color", toast_style["colors"]["text"]),
                        size=self._get_style_value("text_size", 14),
                        weight=self._get_style_value("text_weight", ft.FontWeight.W_500),
                        expand=True,
                        no_wrap=False,
                        max_lines=self._get_style_value("max_lines", 3)
                    )
                )

            # Close button
            if self.show_dismiss_button and self._get_style_value("show_close", True):
                content_controls.append(
                    ft.IconButton(
                        icon=self._get_style_value("close_icon", ft.Icons.CLOSE_ROUNDED),
                        icon_color=self._get_style_value("close_color", toast_style["colors"]["text"]),
                        icon_size=self._get_style_value("close_size", 20),
                        on_click=self.dismiss,
                        tooltip="Dismiss"
                    )
                )

            main_content = ft.Row(
                controls=content_controls,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                spacing=self.content_spacing
            )

        # Improved Progress bar implementation
        container_width = self._get_style_value("width", 320) - (self._get_style_value("padding", 12) * 2)
        if self.show_progress:
            # Create progress background
            progress_bg = ft.Container(
                height=self._get_style_value("progress_height", 3),
                width=container_width,
                bgcolor=ft.Colors.with_opacity(0.3, self._get_style_value("progress_color", toast_style["colors"]["progress"])),
                border_radius=ft.border_radius.only(bottom_left=2, bottom_right=2),
            )
            
            # Create actual progress bar - starts at full width, will animate to 0
            self.progress_bar = ft.Container(
                height=self._get_style_value("progress_height", 3),
                width=container_width,  # Start with full width
                bgcolor=self._get_style_value("progress_color", toast_style["colors"]["progress"]),
                border_radius=ft.border_radius.only(bottom_left=2, bottom_right=2),
                # Set up animation properties
                animate_size=ft.Animation(
                    duration=100,  # Short duration for smooth updates
                    curve=ft.AnimationCurve.LINEAR
                )
            )
            
            # Stack progress bar on top of background
            progress_stack = ft.Stack(
                controls=[progress_bg, self.progress_bar],
                height=self._get_style_value("progress_height", 3),
                width=container_width
            )
        else:
            progress_stack = ft.Container(height=0)

        # Main container content
        container_content = ft.Column(
            controls=[main_content, progress_stack],
            spacing=0,
            tight=True
        )

        # Toast content container
        bg_color = self._get_style_value("bg_color", toast_style["colors"]["bg"])
        
        self.toast_content = ft.Container(
            content=container_content,
            bgcolor=bg_color,
            border_radius=self._get_style_value("border_radius", 8),
            padding=self._get_style_value("padding", 12),
            border=ft.border.all(
                width=self._get_style_value("border_width", 0),
                color=self._get_style_value("border_color", "transparent")
            ),
            shadow=ft.BoxShadow(
                spread_radius=self._get_style_value("shadow_spread", 1),
                blur_radius=self._get_style_value("shadow_blur", 15),
                color=ft.Colors.with_opacity(
                    self._get_style_value("shadow_opacity", 0.3), 
                    ft.Colors.BLACK
                ),
                offset=ft.Offset(
                    self._get_style_value("shadow_x", 0), 
                    self._get_style_value("shadow_y", 4)
                ),
                blur_style=ft.ShadowBlurStyle.OUTER,
            )
        )
        
        self.toast_container = ft.Container(
            content=self.toast_content,
            width=self._get_style_value("width", 320),
            opacity=0,
            animate_opacity=300,
            animate_position=300,
            on_hover=self._handle_hover if self.pausable else None
        )

    def _handle_hover(self, e):
        """Handle hover events for pause/resume functionality"""
        if e.data == "true":
            self.pause()
        else:
            self.resume()

    def pause(self):
        """Pause the toast timer and progress bar"""
        if not self.is_paused and self.timer:
            self.is_paused = True
            self.timer.cancel()
            if self.progress_update_timer:
                self.progress_update_timer.cancel()
                
            if self.start_time:
                elapsed = time.time() - self.start_time
                self.remaining_time = max(0, self.remaining_time - elapsed)
                
            # Also pause the progress calculation by updating the progress start time
            if hasattr(self, 'progress_start_time') and self.progress_start_time:
                progress_elapsed = time.time() - self.progress_start_time
                # Store the total elapsed time when pausing
                self.total_progress_elapsed = (self.original_duration - self.remaining_time)

    def resume(self):
        """Resume the toast timer and progress bar"""
        if self.is_paused and self.remaining_time > 0:
            self.is_paused = False
            self.start_time = time.time()
            self.timer = Timer(self.remaining_time, self.dismiss)
            self.timer.start()
            
            # Reset progress start time to current time when resuming
            self.progress_start_time = time.time()
            
            if self.show_progress:
                self._start_progress_updates()

    def _start_progress_updates(self):
        """Start smooth progress bar updates with better timing"""
        if not self.show_progress or not hasattr(self, 'progress_bar') or self.is_paused:
            return

        # Initialize progress start time only if not set or if resuming from pause
        if not hasattr(self, 'progress_start_time') or self.progress_start_time is None:
            self.progress_start_time = time.time()
            
        container_width = self._get_style_value("width", 320) - (self._get_style_value("padding", 12) * 2)
        
        def update_progress():
            if self.is_paused:
                return
                
            try:
                # Calculate elapsed time since current progress session started
                current_time = time.time()
                current_session_elapsed = current_time - self.progress_start_time
                
                # Add current session elapsed to total progress elapsed
                total_elapsed = self.total_progress_elapsed + current_session_elapsed
                
                # Calculate progress percentage (0 to 1)
                progress_percentage = min(1.0, total_elapsed / self.original_duration)
                
                # Calculate remaining width (countdown effect - starts full, goes to 0)
                remaining_width = max(0, container_width * (1 - progress_percentage))
                
                # Update the progress bar width
                self.progress_bar.width = remaining_width
                self._safe_update(self.progress_bar)
                
                # Continue updating if not complete and not paused
                if progress_percentage < 1.0 and not self.is_paused:
                    # Use shorter intervals for smoother animation
                    self.progress_update_timer = Timer(0.05, update_progress)  # 50ms intervals
                    self.progress_update_timer.start()
                    
            except Exception as e:
                print(f"Error updating progress: {e}")
        
        # Start the progress updates
        update_progress()

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

            # Initialize timing
            self.start_time = time.time()
            self.progress_start_time = time.time()  # Initialize progress timing
            
            # Start the dismiss timer
            self.timer = Timer(self.duration, self.dismiss)
            self.timer.start()

            # Start progress bar animation after a short delay to ensure UI is ready
            if self.show_progress:
                Timer(0.1, self._start_progress_updates).start()

    def _update_toast_positions(self):
        """Update toast positions with cascade effect"""
        toast_count = len(self.page.toast_stack.controls)
        gap_y = 12
        gap_x = 10

        for index, toast_container in enumerate(reversed(self.page.toast_stack.controls)):
            container_height = toast_container.height or self._get_style_value("height", 60)
            offset_x = index * gap_x
            offset_y = index * gap_y
            scale = 1 - (index * 0.05)
            toast_container.animate_position = ft.Animation(250, ft.AnimationCurve.EASE_OUT)
            toast_container.animate_scale = ft.Animation(250, ft.AnimationCurve.EASE_OUT)
            toast_container.scale = scale

            if self.position == "top_left":
                toast_container.left = 20 + offset_x
                toast_container.top = 20 + offset_y
            elif self.position == "top_right":
                toast_container.right = 20 - offset_x
                toast_container.top = 20 + offset_y
            elif self.position == "bottom_left":
                toast_container.left = 20 + offset_x
                toast_container.bottom = 20 + offset_y
            elif self.position == "bottom_right":
                toast_container.right = 20 - offset_x
                toast_container.bottom = 20 + offset_y
            elif self.position == "top_center":
                toast_container.top = 20 + offset_y
                toast_container.left = (self.page.width - toast_container.width) / 2 + offset_x
            elif self.position == "bottom_center":
                toast_container.bottom = 20 + offset_y
                toast_container.left = (self.page.width - toast_container.width) / 2 + offset_x

    def dismiss(self, e=None):
        """Dismiss the toast"""
        if self.timer:
            self.timer.cancel()
        if self.progress_timer:
            self.progress_timer.cancel()
        if self.progress_update_timer:
            self.progress_update_timer.cancel()

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
        """Safely update controls with better error handling"""
        try:
            if hasattr(self.page, '_session_id') or hasattr(self.page, 'session_id'):
                if isinstance(control, (ft.Container, ft.Control)):
                    control.update()
                elif isinstance(control, ft.Page):
                    control.update()
        except Exception as e:
            # Silently handle update errors to prevent crashes
            pass

    @classmethod
    def success(cls, page, message, **kwargs):
        return cls(page, message, toast_type="success", **kwargs)

    @classmethod
    def error(cls, page, message, **kwargs):
        return cls(page, message, toast_type="error", **kwargs)

    @classmethod
    def warning(cls, page, message, **kwargs):
        return cls(page, message, toast_type="warning", **kwargs)

    @classmethod
    def info(cls, page, message, **kwargs):
        return cls(page, message, toast_type="info", **kwargs)