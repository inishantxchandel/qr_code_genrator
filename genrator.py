import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import ImageTk, Image

def generate_qr_code():
    url = entry.get()

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Display the QR code in the UI
    img = img.resize((300, 300), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
    img_tk = ImageTk.PhotoImage(img)
    qr_code_label.config(image=img_tk)
    qr_code_label.image = img_tk

    # Save the QR code as a PNG file
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img.save(file_path)

# Create the main application window
root = tk.Tk()
root.title("QR Code Generator")

# Entry field for the website link
entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack(pady=10)

# Button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", font=("Helvetica", 14), command=generate_qr_code)
generate_button.pack(pady=10)

# Label to display the QR code
qr_code_label = tk.Label(root)
qr_code_label.pack()

root.mainloop()
