import tkinter as tk
import customtkinter as ctk
from PIL import ImageGrab, Image

class SignaturePopup(tk.Toplevel):  # Use tk.Toplevel
    def __init__(self, master, student_sign):
        super().__init__(master)
        self.save_path = f'assets/img/signatures/{student_sign}.png'
        self.title("Draw your signature")
        self.geometry("500x300")
        self.grab_set()  # Modal behavior

        self.canvas = tk.Canvas(self, bg='white', width=480, height=220, cursor='pencil')
        self.canvas.pack(pady=10)
        self.canvas.bind('<B1-Motion>', self.draw)

        button_frame = ctk.CTkFrame(self, fg_color='transparent')
        button_frame.pack()

        ctk.CTkButton(button_frame, text="Clear", command=self.clear_canvas, width=100).pack(side='left', padx=5)
        ctk.CTkButton(button_frame, text="Save", command=self.save_and_close, width=100).pack(side='left', padx=5)

    def draw(self, event):
        x, y = event.x, event.y
        r = 2
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill='black', outline='black')

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_and_close(self):
        self.update()
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        # Save canvas content
        img = ImageGrab.grab((x, y, x1, y1)).convert("RGBA")

        # Remove white background
        data = img.getdata()
        new_data = []
        for item in data:
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))  # Transparent
            else:
                new_data.append(item)
        img.putdata(new_data)

        img.save(self.save_path)

        self.destroy()
