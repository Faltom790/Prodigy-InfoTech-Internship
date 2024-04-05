from PIL import Image

def encrypt_image(input_image_path, output_image_path):
    # Open the input image
    img = Image.open(input_image_path)
    width, height = img.size
    
    # Encrypt the image by swapping pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            # Encryption operation: swapping red and blue channels
            img.putpixel((x, y), (b, g, r))

    # Save the encrypted image
    img.save(output_image_path)

def decrypt_image(input_image_path, output_image_path):
    # Open the encrypted image
    img = Image.open(input_image_path)
    width, height = img.size
    
    # Decrypt the image (perform the reverse operation)
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            # Decryption operation: swapping red and blue channels again
            img.putpixel((x, y), (b, g, r))

    # Save the decrypted image
    img.save(output_image_path)

# Paths to image files
input_image = r"C:\Users\tomiwa\Desktop\TEST\letter.jpg" #This is the image file we want to encrypt
encrypted_image = r"C:\Users\tomiwa\Desktop\TEST\encrypted_image.jpg"    
decrypted_image = r"C:\Users\tomiwa\Desktop\TEST\decrypted_image.jpg"   

encrypt_image(input_image, encrypted_image)
decrypt_image(encrypted_image, decrypted_image)

print("Image encryption and decryption completed.") #Prints this when successful
