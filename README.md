# steganography
 # steganography
This project is an image steganography tool built using Python and OpenCV. It allows users to hide a secret message inside an image and later extract it without altering the visual appearance of the image. The Least Significant Bit (LSB) encoding technique is used for embedding the message.
-------------------------------------------------------------------------------------

Folder Structure for this project is as following-
 steganography
│-- 📄 encode.py    # Script to encode a secret message into an image
│-- 📄 decode.py    # Script to extract the secret message from an image
│-- 📄 test_bits.py # Debugging script to verify the encoded bits
│-- 📄 README.md    # Project documentation
-------------------------------------------------------------------------------------

Technologies Used in this project are as follows-
Python 3.x
OpenCV (cv2)
NumPy
-------------------------------------------------------------------------------------
 
 Installation needed for the following project-

 Install dependencies
 pip install opencv-python numpy
-------------------------------------------------------------------------------------

 Usage-

 step 1.Encoding a Message
To hide a message inside an image:
python encode.py
.
The script will prompt you to enter:

Path to the image file

Secret message

Output image filename

A new image with the hidden message will be saved.

-------------------------------------------------------------------------------------
Step 2.Decoding the message

To extract the hidden message:
python decode.py

Enter the path of the encoded image.

The script will display the hidden message.

------------------------------------------------------------------------------------
Debugging

If decoding fails, use:
python test_bits.py

This extracts the first 200 bits of the image to verify if encoding was successful.
-------------------------------------------------------------------------------------
License

This project is open-source and available under the MIT License.
