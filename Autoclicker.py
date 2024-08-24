import tkinter as tk
from tkinter import ttk
import pyautogui
import keyboard
import threading
import time

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoClicker")
        self.root.attributes('-topmost', True)

        self.click_interval = (0, 0, 100)  # (minutes, seconds, milliseconds)
        self.mouse_button = 'left'
        self.click_type = 'single'
        self.repeat_option = 'until stopped'
        self.repeat_count = 0
        self.positions = []
        self.use_current_position = True  # Default to using current position
        self.running = False
        self.hotkey = 'F9'
        self.position_hotkey = 'esc'

        self.create_widgets()
        self.update_repeat_options()

        # Register global hotkeys
        self.register_hotkeys()

        # Bind focus events
        self.root.bind('<FocusIn>', self.on_focus_in)
        self.root.bind('<FocusOut>', self.on_focus_out)

    def create_widgets(self):
        # Apply custom style
        self.create_style()

        ttk.Label(self.root, text="AutoClicker", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="n")

        ttk.Label(self.root, text="Click Interval (mm:ss:ms):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        interval_frame = ttk.Frame(self.root)
        interval_frame.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        ttk.Label(interval_frame, text="Minutes:").grid(row=0, column=0, padx=5, pady=5)
        self.minutes_entry = ttk.Entry(interval_frame, width=5)
        self.minutes_entry.grid(row=0, column=1, padx=5, pady=5)
        self.minutes_entry.insert(0, str(self.click_interval[0]))

        ttk.Label(interval_frame, text="Seconds:").grid(row=0, column=2, padx=5, pady=5)
        self.seconds_entry = ttk.Entry(interval_frame, width=5)
        self.seconds_entry.grid(row=0, column=3, padx=5, pady=5)
        self.seconds_entry.insert(0, str(self.click_interval[1]))

        ttk.Label(interval_frame, text="Milliseconds:").grid(row=0, column=4, padx=5, pady=5)
        self.milliseconds_entry = ttk.Entry(interval_frame, width=5)
        self.milliseconds_entry.grid(row=0, column=5, padx=5, pady=5)
        self.milliseconds_entry.insert(0, str(self.click_interval[2]))

        ttk.Label(self.root, text="Mouse Button:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.mouse_button_var = tk.StringVar(value=self.mouse_button)
        self.mouse_button_menu = ttk.Combobox(self.root, textvariable=self.mouse_button_var, values=['left', 'right'])
        self.mouse_button_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.root, text="Click Type:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.click_type_var = tk.StringVar(value=self.click_type)
        self.click_type_menu = ttk.Combobox(self.root, textvariable=self.click_type_var, values=['single', 'double'])
        self.click_type_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.root, text="Repeat Option:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.repeat_option_var = tk.StringVar(value=self.repeat_option)
        self.repeat_option_menu = ttk.Combobox(self.root, textvariable=self.repeat_option_var, values=['number of times', 'until stopped'])
        self.repeat_option_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.repeat_option_menu.bind("<<ComboboxSelected>>", self.update_repeat_options)

        ttk.Label(self.root, text="Repeat Count:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.repeat_count_entry = ttk.Entry(self.root, width=10)
        self.repeat_count_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_autoclicker)
        self.start_button.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_autoclicker, state=tk.DISABLED)
        self.stop_button.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        self.hotkey_popup_button = ttk.Button(self.root, text=f"Set Hotkey: {self.hotkey}", command=self.capture_hotkey)
        self.hotkey_popup_button.grid(row=7, column=0, padx=10, pady=10, sticky="w")

        self.set_positions_button = ttk.Button(self.root, text="Set Positions", command=self.start_position_selection)
        self.set_positions_button.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        # "Use Current Position" button with updated style
        self.toggle_position_checkbox = ttk.Checkbutton(self.root, text="Use Current Position", command=self.toggle_current_position, style="Toggle.TCheckbutton")
        self.toggle_position_checkbox.grid(row=8, column=0, padx=10, pady=10, sticky="w")

        # Set initial state
        self.toggle_position_checkbox.state(["selected"])

    def create_style(self):
        style = ttk.Style()
        style.configure("Toggle.TCheckbutton", background="lightgreen", foreground="black")
        style.map("Toggle.TCheckbutton", background=[("selected", "lightgreen"), ("!selected", "lightgrey")])

    def register_hotkeys(self):
        # Register the hotkey to start/stop autoclicker
        keyboard.add_hotkey(self.hotkey, self.start_autoclicker)
        # Register the hotkey to exit position selection
        keyboard.add_hotkey(self.position_hotkey, self.stop_position_selection)

    def unregister_hotkeys(self):
        # Unregister the hotkeys
        try:
            keyboard.remove_hotkey(self.hotkey)
        except KeyError:
            pass
        try:
            keyboard.remove_hotkey(self.position_hotkey)
        except KeyError:
            pass

    def start_autoclicker(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.unregister_hotkeys()  # Remove hotkey before re-adding
            try:
                keyboard.add_hotkey(self.hotkey, self.stop_autoclicker)
            except Exception as e:
                print(f"Error adding hotkey: {e}")
            threading.Thread(target=self.run_autoclicker, daemon=True).start()

    def stop_autoclicker(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def run_autoclicker(self):
        try:
            interval = int(self.minutes_entry.get() or 0) * 60 + int(self.seconds_entry.get() or 0) + int(self.milliseconds_entry.get() or 0) / 1000.0
            repeat_count = int(self.repeat_count_entry.get() or 0)
            
            if self.repeat_option == 'number of times':
                print("Running autoclicker for a specific number of times...")
                for _ in range(repeat_count):
                    if not self.running:
                        break
                    self.perform_click()
                    time.sleep(interval)
            elif self.repeat_option == 'until stopped':
                print("Running autoclicker until stopped...")
                while self.running:
                    self.perform_click()
                    time.sleep(interval)
        except Exception as e:
            print(f"Error in autoclicker: {e}")

    def perform_click(self):
        if self.use_current_position:
            x, y = pyautogui.position()
            print(f"Clicking at current position: ({x}, {y})")
            if self.click_type == 'single':
                pyautogui.click(x, y, button=self.mouse_button)
            else:
                pyautogui.click(x, y, button=self.mouse_button, clicks=2)
        else:
            for pos in self.positions:
                if not self.running:
                    break
                print(f"Clicking at position: {pos}")
                if self.click_type == 'single':
                    pyautogui.click(pos[0], pos[1], button=self.mouse_button)
                else:
                    pyautogui.click(pos[0], pos[1], button=self.mouse_button, clicks=2)
                time.sleep(self.click_interval[0] * 60 + self.click_interval[1] + self.click_interval[2] / 1000.0)

    def toggle_current_position(self):
        self.use_current_position = not self.use_current_position
        # Update the state of the Set Positions button based on the use_current_position flag
        if self.use_current_position:
            self.set_positions_button.config(state=tk.NORMAL)
        else:
            self.set_positions_button.config(state=tk.DISABLED)
        # Update the text color of the Toggle Position button
        if self.use_current_position:
            self.toggle_position_checkbox.config(style="Toggle.TCheckbutton")
        else:
            self.toggle_position_checkbox.config(style="Toggle.TCheckbutton")

    def update_repeat_options(self, *args):
        if self.repeat_option_var.get() == 'number of times':
            self.repeat_count_entry.config(state=tk.NORMAL)
        else:
            self.repeat_count_entry.config(state=tk.DISABLED)

    def capture_hotkey(self):
        self.root.bind('<KeyPress>', self.set_hotkey)

    def set_hotkey(self, event):
        self.hotkey = event.keysym
        self.hotkey_popup_button.config(text=f"Set Hotkey: {self.hotkey}")
        self.unregister_hotkeys()
        self.register_hotkeys()
        self.root.unbind('<KeyPress>')

    def start_position_selection(self):
        self.set_positions_button.config(state=tk.DISABLED)
        self.toggle_position_checkbox.config(state=tk.DISABLED)
        self.root.wait_window(tk.Toplevel(self.root))  # Open a new window to select positions
        self.stop_position_selection()

    def stop_position_selection(self):
        self.set_positions_button.config(state=tk.NORMAL)
        self.toggle_position_checkbox.config(state=tk.NORMAL)

    def on_focus_in(self, event):
        self.root.attributes('-topmost', True)

    def on_focus_out(self, event):
        self.root.attributes('-topmost', False)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()
