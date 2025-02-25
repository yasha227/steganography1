import cv2
import numpy as np

def encode_message(image_path, message, output_image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        raise ValueError("Image not found!")

    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # End marker
    

    data_index = 0
    message_length = len(binary_message)
    
    for row in img:
        for pixel in row:
            for channel in range(3):  # Iterate over BGR channels
                if data_index < message_length:
                    # Ensure pixel values stay in the valid range (0-255)
                    pixel[channel] = (pixel[channel] & 254) | int(binary_message[data_index])
                    data_index += 1
                else:
                    break
    
    cv2.imwrite(output_image_path, img)
    print(f"Message encoded and saved as {output_image_path}")

if __name__ == "__main__":
    image_path = input("Enter input image path: ")
    message = input("Enter the secret message: ")
    output_image_path = "encoded_image.png"

    encode_message(image_path, message, output_image_path)