#This code generates a QR code for a given website or data using the qrcode library in Python. It sets up the QR code parameters, adds the data to be encoded, and saves the generated QR code as a PNG file.

#pip install "qrcode[pil]" Pillow
 #python qrcode_generator.py
#run


import qrcode 

#code to generate a QR code for a given website or data
qr =qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L, #an error handling mechanism incase the code doesn't run as expected
  box_size=10, 
  border=4
)

#what data you want to encode in the QR code
data ="https://github.com/"
qr.add_data(data)
qr.make(fit=True) #shows the QR code in a fit manner

img = qr.make_image(fill_color='black', back_color='white')
img.save("Githubwebsite_QRcode.png") #saves the generated QR code as a PNG file

print("QR code has been generated")
