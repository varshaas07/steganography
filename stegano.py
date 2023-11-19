import cv2
import os

def validate_image_path(img_path):
    if not os.path.exists(img_path):
        print(f"Error: Image file '{img_path}' not found.")
        exit()

def encrypt_message(img, message):
    encrypted_img = img.copy()
    n, m, z = 0, 0, 0

    for char in message:
        encrypted_img[n, m, z] = ord(char)
        n += 1
        m += 1
        z = (z + 1) % img.shape[2]

    return encrypted_img

def decrypt_message(encrypted_img):
    decrypted_message = ""
    n, m, z = 0, 0, 0

    for _ in range(len(msg)):
        decrypted_message += chr(encrypted_img[n, m, z])
        n += 1
        m += 1
        z = (z + 1) % encrypted_img.shape[2]

    return decrypted_message

img_path = "img.jpg"
validate_image_path(img_path)

img = cv2.imread(img_path)

msg = input("Enter secret message: ")

# Ensure the length of the message is not greater than the number of pixels
if len(msg) > img.size // 3:
    print("Error: Message is too long for the given image.")
    exit()

password = input("Enter password: ")

# Encryption
encrypted_img = encrypt_message(img, msg)
cv2.imwrite("Encryptedmsg.jpg", encrypted_img)

print("Encryption completed. Opening encrypted image.")
os.system("start Encryptedmsg.jpg")

# Decryption
decryption_password = input("Enter passcode for Decryption: ")

if password == decryption_password:
    decrypted_msg = decrypt_message(encrypted_img)
    print(f"Decryption message: {decrypted_msg}")
else:
    print("Not a valid key")
