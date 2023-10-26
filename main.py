import qrcode
import tkinter as tk
from PIL import Image, ImageTk
import os

def generate_qr_code():
    text = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Display the QR code image above the input field
    qr_image = qr_image.resize((200, 200)) 
    photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=photo)
    qr_label.image = photo

    # Save the QR code to a file in the "qrcodes" folder
    folder_name = "qrcodes"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    
    file_name = os.path.join(folder_name, f"{text}.png")
    qr_image.save(file_name)
    print(f"QR code saved to {file_name}")

# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create an input field for the user to enter text
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Create a button to generate the code
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create a label to display the QR code image
qr_label = tk.Label(window)
qr_label.pack()

# Start the main loop
window.mainloop()
