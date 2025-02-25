import cv2
import os

def decode_message(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Error: File '{image_path}' not found.")

    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Error: Could not open image. Ensure it's a valid PNG/JPG file.")

    print(f"✅ Image loaded! Shape: {img.shape}, Data Type: {img.dtype}")

    binary_message = ""

    for row in img:
        for pixel in row:
            for channel in range(3):
                binary_message += str(pixel[channel] & 1)  # Extract LSB

    # Split into 8-bit chunks
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]

    # Convert binary to ASCII until we reach the correct end marker
    message = ""
    for i, char in enumerate(chars):
        if char == "11111110":  # Stop decoding at the correct end marker
            break
        try:
            message += chr(int(char, 2))  # Convert binary to ASCII
        except ValueError:
            break  # Stop if invalid binary is found

    if not message:
        print("❌ No hidden message found! Check encoding.")
    else:
        print("\n🔓 Decoded Message:", message)
    
    return message

if __name__ == "__main__":
    image_path = input("Enter the full path of the encoded image: ").strip()
    image_path = image_path.replace("\\", "/")
    decode_message(image_path)
