import qrcode
import tkinter as tk
from PIL import Image, ImageTk

def generate_qr_code():
    text = entry.get() # get text from input field
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color = "white")
    img.save("generated_qr.png") # save the qr code

    # display the qr code image above the input field
    qr_image = Image.open("generated_qr.png")
    qr_image = ImageTk.PhotoImage(qr_image)
    qr_label.config(image = qr_image)
    qr_label.image = qr_image

# create the main window
window = tk.Tk()
window.title("QR Code Generator")

# create an input field for the user to enter text
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# create a button to generate the code
generate_button = tk.Button(window, text = "Generate QR Code")
generate_button.pack()

# create a label to display the QR code image
qr_label = tk.Label(window)
qr_label.pack()

# start the main loop
window.mainloop()


