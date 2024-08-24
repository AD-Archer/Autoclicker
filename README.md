
# AutoClicker

Welcome to the **AutoClicker** project! This is a free and customizable autoclicker application designed to make repetitive clicking tasks easier and more efficient. Unlike many commercial autoclickers, this tool is open-source and available at no cost. I believe that everyone should have access to effective automation tools without financial barriers.

## Features

- **Customizable Click Intervals:** Set intervals for minutes, seconds, and milliseconds.
- **Mouse Button Options:** Choose between left and right mouse buttons.
- **Click Type:** Select between single and double clicks.
- **Repeat Options:** Click a specific number of times or until stopped.
- **Position Recording:** Click at predefined positions or use the current cursor position.
- **Hotkey Support:** Start/stop autoclicking with customizable hotkeys.

## Getting Started

To get started with the AutoClicker, you'll need to install the required Python packages. Follow these steps to set up the application on your local machine:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AD-Archer/Autoclicker.git
   cd Autoclicker
   ```

2. **Install Required Packages:**

   The AutoClicker requires the following Python packages:

   - `tkinter` (for the GUI)
   - `pyautogui` (for simulating mouse clicks)
   - `keyboard` (for hotkey functionality)
   - `threading` (for running the autoclicker in the background)
   
   Install them using pip:

   ```bash
   pip install pyautogui keyboard
   ```

   Note: `tkinter` is included with Python by default, so you don't need to install it separately.

3. **Run the Application:**

   Execute the script to launch the AutoClicker:

   ```bash
   python autoclicker.py
   ```

## How It Works

The AutoClicker allows you to set up and customize clicking intervals, mouse buttons, and click types. It also supports recording mouse positions for repeated clicks. You can start and stop the autoclicker using configurable hotkeys, which are set through the application’s interface.

## Why Free?

Many autoclickers on the market are paid, which can be a barrier for users who need such tools but cannot afford them. By providing this tool for free, I aim to make automation accessible to everyone. Feel free to use, modify, and contribute to the project.

## Contributing

Contributions to the AutoClicker project are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

