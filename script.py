import pyautogui
import pyperclip
import tkinter as tk
import keyboard

is_playing = False

def press_tab():
    
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('v')
    
    text = pyperclip.paste()
    values = text.split('#sep#')
    for i in range(0, len(values)):
        
        pyautogui.write(values[i])  # interval prevents skipping
        if i < len(values) - 1:
            pyautogui.press('tab')


def toggle_play_pause():
    global is_playing
    is_playing = not is_playing
    if is_playing:
        btn.config(text="Pause")
        keyboard.add_hotkey('ctrl+shift+p', press_tab)
    else:
        btn.config(text="Play")
        keyboard.remove_hotkey('ctrl+shift+p')

window = tk.Tk()
window.title("GP Paster")

btn = tk.Button(window, text="Play", command=toggle_play_pause)
btn.pack(pady=10, padx=140)

window.mainloop()