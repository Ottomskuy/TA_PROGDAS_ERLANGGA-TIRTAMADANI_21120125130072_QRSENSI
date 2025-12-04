import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from qrcode_generator import generate_qr
from qrcode_scanner import scan_qr
from absensi import Absensi
from users import UserSystem

absensi = Absensi()
user_system = UserSystem()

root = tk.Tk()
root.title("QR Sensi - Absensi QR Code")
root.geometry("500x700")

# Create gradient background
canvas = tk.Canvas(root, width=500, height=700, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Gradient colors (blue to purple)
def create_gradient(canvas, width, height):
    r1, g1, b1 = 79, 108, 217  # Blue
    r2, g2, b2 = 145, 88, 188  # Purple
    
    for i in range(height):
        ratio = i / height
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)

create_gradient(canvas, 500, 700)

# Modern styling
FONT_TITLE = ("Segoe UI", 28, "bold")
FONT_LABEL = ("Segoe UI", 11)
FONT_ENTRY = ("Segoe UI", 12)
FONT_BTN = ("Segoe UI", 12, "bold")

# ------------------- HELPER FUNCTIONS -------------------
def create_card(parent, width=400, height=500):
    """Create a white card with shadow effect"""
    card = tk.Frame(parent, bg="white", width=width, height=height)
    card.place(relx=0.5, rely=0.5, anchor="center")
    return card

def create_underline_entry(parent, show=None):
    """Create modern underline-style entry"""
    frame = tk.Frame(parent, bg="white")
    entry = tk.Entry(frame, font=FONT_ENTRY, border=0, bg="white", 
                     show=show if show else "", fg="#333333")
    entry.pack(fill="x", padx=5)
    
    # Underline
    line = tk.Frame(frame, height=1, bg="#d0d0d0")
    line.pack(fill="x", pady=(5, 0))
    
    # Change color on focus
    def on_focus_in(e):
        line.config(bg="#4F6CD9")
    def on_focus_out(e):
        line.config(bg="#d0d0d0")
    
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
    
    return frame, entry

def create_pill_button(parent, text, command, bg="#4F6CD9", fg="white"):
    """Create rounded pill-style button"""
    btn = tk.Button(parent, text=text, font=FONT_BTN, bg=bg, fg=fg,
                   border=0, cursor="hand2", command=command,
                   padx=30, pady=12, activebackground="#3d5ab8",
                   activeforeground="white")
    
    # Hover effect
    def on_enter(e):
        btn.config(bg="#3d5ab8")
    def on_leave(e):
        btn.config(bg=bg)
    
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    
    return btn

# ------------------- LOGIN PAGE -------------------
def show_login_page():
    canvas.delete("card")
    
    card = create_card(canvas, 380, 480)
    canvas.create_window(250, 350, window=card, tags="card")
    
    # Title
    tk.Label(card, text="Login", font=FONT_TITLE, bg="white", fg="#333333").pack(pady=(40, 50))
    
    # Username
    tk.Label(card, text="Username", font=FONT_LABEL, bg="white", fg="#999999", anchor="w").pack(fill="x", padx=40)
    username_frame, username_entry = create_underline_entry(card)
    username_frame.pack(fill="x", padx=40, pady=(5, 20))
    
    # Password
    tk.Label(card, text="Password", font=FONT_LABEL, bg="white", fg="#999999", anchor="w").pack(fill="x", padx=40)
    password_frame, password_entry = create_underline_entry(card, show="*")
    password_frame.pack(fill="x", padx=40, pady=(5, 10))
    
    # Show password checkbox
    show_var = tk.IntVar()
    def toggle_password():
        password_entry.config(show="" if show_var.get() else "*")
    
    check_frame = tk.Frame(card, bg="white")
    check_frame.pack(fill="x", padx=40, pady=(0, 30))
    tk.Checkbutton(check_frame, text="Tampilkan Password", variable=show_var, 
                   bg="white", font=("Segoe UI", 9), command=toggle_password,
                   cursor="hand2").pack(anchor="w")
    
    def login_action():
        user = username_entry.get()
        pw = password_entry.get()
        success, msg = user_system.login(user, pw)
        if success:
            messagebox.showinfo("Sukses", msg)
            show_main_menu()
        else:
            messagebox.showerror("Error", msg)
    
    # Login button
    create_pill_button(card, "Login", login_action).pack(pady=(10, 15))
    
    # Register button
    create_pill_button(card, "Register", show_register_page, 
                      bg="#9158BC", fg="white").pack(pady=5)

# ------------------- REGISTER PAGE -------------------
def show_register_page():
    canvas.delete("card")
    
    card = create_card(canvas, 380, 480)
    canvas.create_window(250, 350, window=card, tags="card")
    
    # Title
    tk.Label(card, text="Register", font=FONT_TITLE, bg="white", fg="#333333").pack(pady=(40, 50))
    
    # Username
    tk.Label(card, text="Username", font=FONT_LABEL, bg="white", fg="#999999", anchor="w").pack(fill="x", padx=40)
    username_frame, username_entry = create_underline_entry(card)
    username_frame.pack(fill="x", padx=40, pady=(5, 20))
    
    # Password
    tk.Label(card, text="Password", font=FONT_LABEL, bg="white", fg="#999999", anchor="w").pack(fill="x", padx=40)
    password_frame, password_entry = create_underline_entry(card, show="*")
    password_frame.pack(fill="x", padx=40, pady=(5, 10))
    
    # Show password checkbox
    show_var = tk.IntVar()
    def toggle_password():
        password_entry.config(show="" if show_var.get() else "*")
    
    check_frame = tk.Frame(card, bg="white")
    check_frame.pack(fill="x", padx=40, pady=(0, 30))
    tk.Checkbutton(check_frame, text="Tampilkan Password", variable=show_var, 
                   bg="white", font=("Segoe UI", 9), command=toggle_password,
                   cursor="hand2").pack(anchor="w")
    
    def register_action():
        user = username_entry.get()
        pw = password_entry.get()
        if not user.strip() or not pw.strip():
            messagebox.showerror("Error", "Username dan Password tidak boleh kosong!")
            return
        if len(pw) < 8:
            messagebox.showerror("Error", "Password harus minimal 8 karakter!")
            return
        success, msg = user_system.register(user, pw)
        if success:
            messagebox.showinfo("Sukses", msg)
            show_login_page()
        else:
            messagebox.showerror("Error", msg)
    
    # Register button
    create_pill_button(card, "Daftar", register_action).pack(pady=(10, 15))
    
    # Back button
    create_pill_button(card, "Kembali ke Login", show_login_page, 
                      bg="#9158BC", fg="white").pack(pady=5)

# ------------------- MAIN MENU -------------------
def show_main_menu():
    canvas.delete("card")
    
    card = create_card(canvas, 420, 600)
    canvas.create_window(250, 350, window=card, tags="card")
    
    # Title
    tk.Label(card, text="QR Sensi", font=FONT_TITLE, bg="white", fg="#333333").pack(pady=(30, 40))
    
    # NIM
    tk.Label(card, text="NIM", font=FONT_LABEL, bg="white", fg="#999999", anchor="w").pack(fill="x", padx=40)
    nim_frame, entry_nim = create_underline_entry(card)
    nim_frame.pack(fill="x", padx=40, pady=(5, 20))
    
    # Nama
    tk.Label(card, text="Nama", font=FONT_LABEL, bg="white", fg="#999999", anchor="w").pack(fill="x", padx=40)
    nama_frame, entry_nama = create_underline_entry(card)
    nama_frame.pack(fill="x", padx=40, pady=(5, 20))
    
    # QR Display
    qr_label = tk.Label(card, bg="white")
    qr_label.pack(pady=15)
    
    def buat_qr():
        nim = entry_nim.get()
        nama = entry_nama.get()
        if not nim.strip() or not nama.strip():
            messagebox.showerror("Error", "NIM dan Nama tidak boleh kosong!")
            return
        filename = generate_qr(nim, nama)
        img = Image.open(filename).resize((180, 180))
        img = ImageTk.PhotoImage(img)
        qr_label.config(image=img)
        qr_label.image = img
    
    def scan_qr_btn():
        data = scan_qr()
        if data:
            nim, nama = data.split("|")
            absensi.catat(nim, nama)
            messagebox.showinfo("Sukses", f"Absensi tercatat untuk {nama}")
    
    def riwayat_absensi():
        records = absensi.get_records()
        if not records:
            messagebox.showinfo("Riwayat Absensi", "Belum ada absensi.")
            return
        records_str = "\n".join([f"NIM: {nim} | Nama: {nama} | Waktu: {waktu}" for nim, nama, waktu in records])
        messagebox.showinfo("Riwayat Absensi", records_str)
    def logout_action():
        show_login_page()
    
    # Buttons
    btn_frame = tk.Frame(card, bg="white")
    btn_frame.pack(pady=10)
    
    create_pill_button(btn_frame, "Generate QR", buat_qr, bg="#4F6CD9").pack(pady=5)
    create_pill_button(btn_frame, "Scan QR", scan_qr_btn, bg="#4CAF50").pack(pady=5)
    create_pill_button(btn_frame, "Lihat Riwayat", riwayat_absensi, bg="#FF9800").pack(pady=5)
    create_pill_button(btn_frame, "Logout", logout_action, bg="#F44336").pack(pady=5)

# ------------------- RUN APP -------------------
show_login_page()
root.mainloop()