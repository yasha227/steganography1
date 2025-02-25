import cv2
import os

def extract_first_bits(image_path, num_bits=200):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Error: File '{image_path}' not found.")

    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Error: Could not open image. Ensure it's a valid PNG/JPG file.")

    print(f"✅ Image loaded! Shape: {img.shape}, Data Type: {img.dtype}")

    binary_message = ""

    for row in img:
        for pixel in row:
            for channel in range(3):  # Extract from BGR channels
                binary_message += str(pixel[channel] & 1)  # Get LSB
                if len(binary_message) >= num_bits:
                    break
            if len(binary_message) >= num_bits:
                break
        if len(binary_message) >= num_bits:
            break

    print(f"🛠 First {num_bits} bits extracted: {binary_message}")
    return binary_message

if __name__ == "__main__":
    image_path = input("Enter the full path of the encoded image: ").strip()
    image_path = image_path.replace("\\", "/")
    extract_first_bits(image_path)
