import qrcode
import os

def generate_qr(nim, nama, folder="qrcodes", filename=None):
    if not os.path.exists(folder):
        os.makedirs(folder)
    if filename is None:
        filename = f"{nim}.png"
    full_path = os.path.join(folder, filename)
    data = f"{nim}|{nama}"
    img = qrcode.make(data)
    img.save(full_path)
    return full_path
