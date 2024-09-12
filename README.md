

# AutoClicker

Welcome to the **AutoClicker** project, a fully customizable application designed to automate repetitive clicking tasks with ease and efficiency.

## Features

- **Customizable Click Intervals:** Define precise intervals in minutes, seconds, and milliseconds.
- **Mouse Button Options:** Choose between left and right mouse buttons.
- **Click Type:** Select between single and double clicks.
- **Repeat Options:** Specify the number of clicks or continue until manually stopped.
- **Position Recording:** Automate clicks at predefined positions or use the current cursor position.
- **Hotkey Support:** Start and stop the autoclicker with customizable hotkeys.

## Getting Started

To set up the AutoClicker on your local machine, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/AD-Archer/Autoclicker.git
cd Autoclicker
```

### 2. Install Required Packages

The AutoClicker requires several Python packages:

- `tkinter` (for the GUI)
- `pyautogui` (for simulating mouse clicks)
- `keyboard` (for hotkey functionality)
- `threading` (for running the autoclicker in the background)

Install the necessary packages using pip:

```bash
pip install pyautogui keyboard
```

Note: `tkinter` is included with most Python installations by default.

### 3. Run the Application

Once the required packages are installed, you can execute the script to launch the AutoClicker:

```bash
python autoclicker.py
```

## How It Works

The AutoClicker offers a variety of customization options, including setting click intervals, choosing between different mouse buttons, and selecting the type of click (single or double). Additionally, the application allows you to record specific mouse positions for repeated actions. Hotkeys can be configured to start and stop the clicking process, providing efficient control over the automation.

## Contributing

Contributions are encouraged and greatly appreciated. If you have suggestions for improvements, encounter any issues, or would like to contribute new features, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. For more information, refer to the [LICENSE](LICENSE) file.

