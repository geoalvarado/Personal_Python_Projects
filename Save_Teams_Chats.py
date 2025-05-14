import os
import re
from datetime import datetime
from collections import Counter
import tkinter as tk
from tkinter import messagebox, scrolledtext

# === CONFIGURATION ===
BASE_DIR = "Teams_Chat_Archive"
YOUR_NAME = "Me"  # Change if needed

# === CORE FUNCTIONS ===

def extract_names(text):
    matches = re.findall(r'^\[?([^\]]+?)\]?\s+\d{1,2}:\d{2}\s?[APMapm]{2}?:', text, re.MULTILINE)
    name_counts = Counter(matches)
    return name_counts

def format_chat(text):
    return text.strip()

def save_chat(text):
    chat_date = datetime.now().date()
    name_counts = extract_names(text)
    participants = [name for name in name_counts if name != YOUR_NAME]
    contact_name = participants[0].replace(" ", "") if participants else "Unknown"

    year = chat_date.year
    week_number = chat_date.isocalendar()[1]
    date_str = chat_date.strftime("%Y-%m-%d")
    file_name = f"{date_str}_Chat_with_{contact_name}.txt"
    folder_path = os.path.join(BASE_DIR, str(year), f"Week_{week_number}")
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Date: {date_str}\n")
        f.write(f"Participants: {', '.join(name_counts.keys())}\n\n")
        f.write(format_chat(text))

    return file_path

# === TKINTER UI ===

def submit_chat():
    chat_text = text_box.get("1.0", tk.END).strip()
    if not chat_text:
        messagebox.showwarning("Empty Chat", "Please paste a Teams chat before saving.")
        return
    try:
        path = save_chat(chat_text)
        messagebox.showinfo("Success", f"Chat saved to:\n{path}")
        text_box.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# === MAIN WINDOW ===

root = tk.Tk()
root.title("Teams Chat Archiver")

tk.Label(root, text="Paste Teams Chat Below:").pack(pady=(10, 0))

text_box = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
text_box.pack(padx=10, pady=10)

save_button = tk.Button(root, text="Save Chat", command=submit_chat)
save_button.pack(pady=(0, 10))

root.mainloop()