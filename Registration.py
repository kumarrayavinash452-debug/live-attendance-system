import cv2
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ================= PATH FIX =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

# ================= TKINTER GUI =================
root = tk.Tk()
root.title("Student Registration")
root.geometry("700x550")
root.configure(bg="#2C3E50")

# ================= OPTIONAL BACKGROUND =================
try:
    bg_image = Image.open("background.jpg")
    bg_image = bg_image.resize((700, 550))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    pass

# ================= LABELS =================
tk.Label(root, text="Student Name:", font=("Arial", 16),
         bg="#2C3E50", fg="white").place(x=50, y=20)
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.place(x=220, y=22, width=400)

tk.Label(root, text="Phone Number:", font=("Arial", 16),
         bg="#2C3E50", fg="white").place(x=50, y=70)
phone_entry = tk.Entry(root, font=("Arial", 14))
phone_entry.place(x=220, y=72, width=400)

# ================= CAMERA FRAME =================
camera_label = tk.Label(root, bg="black")
camera_label.place(x=50, y=120, width=600, height=350)

# ================= OPENCV CAMERA =================
cam = cv2.VideoCapture(0)

def show_frame():
    ret, frame = cam.read()
    if ret:
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)
    camera_label.after(10, show_frame)

# ================= SAVE IMAGE =================
def save_image():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Name aur Phone dono bharo")
        return

    filename = os.path.join(DATASET_DIR, f"{name}_{phone}.jpg")

    # 🔒 Duplicate registration check
    if os.path.exists(filename):
        messagebox.showwarning("Already Registered",
                               "❌ Ye student pehle hi register ho chuka hai")
        return

    ret, frame = cam.read()
    if not ret:
        messagebox.showerror("Error", "Camera se image nahi mil rahi")
        return

    saved = cv2.imwrite(filename, frame)
    if saved:
        messagebox.showinfo("Success", f"✅ Registration Successful\n{filename}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Image save nahi ho rahi")

# ================= BUTTON =================
tk.Button(
    root,
    text="Capture & Save",
    font=("Arial", 14),
    bg="#27AE60",
    fg="white",
    command=save_image
).place(x=280, y=490, width=150, height=40)

# ================= START =================
show_frame()
root.mainloop()

cam.release()
cv2.destroyAllWindows()
