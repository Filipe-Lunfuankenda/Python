import tkinter as tk
from tkinter import messagebox
import pyshorteners

def shorten_url():
    url = url_entry.get()
    if url:
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            result_label.config(text=short_url)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao encurtar o URL: {e}")
    else:
        messagebox.showwarning("Aviso", "Por favor insira um URL")

def copy_to_clipboard():
    short_url = result_label.cget("text")
    if short_url:
        app.clipboard_clear()
        app.clipboard_append(short_url)
        messagebox.showinfo("Copiado", "URL encurtado copiado para a área de transferência")
    else:
        messagebox.showwarning("Aviso", "Nenhum URL para copiar")

app = tk.Tk()
app.title("Encurtador de URL")

tk.Label(app, text="Insira o URL:").pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

shorten_button = tk.Button(app, text="Encurtar URL", command=shorten_url)
shorten_button.pack(pady=5)

copy_button = tk.Button(app, text="Copiar URL", command=copy_to_clipboard)
copy_button.pack(pady=5)

result_label = tk.Label(app, text="", fg="blue")
result_label.pack(pady=5)

app.mainloop()