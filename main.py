from pynput import keyboard
import time
import pyperclip

shortcuts = {
	"b": "barcellona",
	"m": "lorem ipsum",
	"6": "3331122333"
}

for key in shortcuts:
	assert len(shortcuts[key]) == 1, "Shortcuts must be one character long"

current_keys = {keyboard.Key.ctrl: False, keyboard.Key.cmd: False}

def on_press(key):
	if key in current_keys:
		current_keys[key] = True
	elif hasattr(key, 'char') and key.char in shortcuts:
		if current_keys[keyboard.Key.cmd]:
			print(f"Copied '{shortcuts[key.char]}' into clipboard")
			pyperclip.copy(shortcuts[key.char])
			return False
		elif current_keys[keyboard.Key.ctrl]:
			print(f"Simulating keystrokes '{shortcuts[key.char]}'")
			for char in shortcuts[key.char]:
				keyboard.Controller().type(char)
				time.sleep(0.02)
			return False

def on_release(key):
	if key in current_keys:
		current_keys[key] = False

while True:
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		try:
			listener.join()
		except KeyboardInterrupt:
			print("Exiting...")
			exit(0)
