# Keyboard Shortcuts with Pyperclip and Pynput

This script provides custom keyboard shortcuts for pre-defined text.

## How it works

The script defines a dictionary of shortcuts, where each key is a single-character string and the corresponding value is the text to be typed or copied when that key is pressed in conjunction with either the Ctrl or Cmd key.

If the Ctrl key is held down while pressing one of the defined shortcut keys, the corresponding text is "typed" one character at a time with a small delay between each keystroke.

If the Cmd key is held down while pressing a shortcut key, the corresponding text is copied to the clipboard.

## Installation

```
pip install -r requirements
```

## Usage

```
python main.py
```

## Disclaimer

Always be careful when using scripts that listen for and blocks keyboard input. Use it at your own risk.

## Contribution

Feel free to contribute to this project by submitting issues or pull requests.
