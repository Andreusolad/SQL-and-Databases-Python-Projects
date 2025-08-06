# QR code when scanned will open the url to our project
import qrcode
# We also installed pillow

image = qrcode.make("https://127.0.0.1:8000")
# If we have a domain we only have to change the string url
image.save("qr.png")