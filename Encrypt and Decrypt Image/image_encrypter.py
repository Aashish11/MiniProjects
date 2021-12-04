"""
Created on Fri Apr 2, 2021
@author: Ashish Singh

"""

# Imports LFSR and Image class object from their 
# respective modules.
from lfsr import LFSR
from PIL import Image

# A data type to encrypt and decrypt images.
class ImageEncrypter:

    # Initialize an ImageEncrypter object with LFSR and image file path.
    def __init__(self, lfsr: LFSR, org_file: str):
        """
        The constructor assigns the LFSR data type and 
        the file path of the image.
        """
        self.lfsr = lfsr
        self.file_name = org_file


    # Convert the image to a 2D array of tuples of the form (R,G,B)
    def pixel_array(self):
        """
        Opens the image and reads the Red(R), Green(G), and Blue(B)
        values from the x,y coordinates of the pixels in the image
        and stores it in a list.
        """
        self.rgb_list = []

        # Opens the image.
        self.px = Image.open(self.file_name)   
        # Extracts the width and height of the image.     
        self.width, self.height = self.px.size    
        # Allocates storage for image and loads pixel data.  
        self.img = self.px.load()                   

        # Reads every pixel in the x,y coordinate and stores it in 
        # a list.
        for i in range(self.width):
            for j in range(self.height):
                self.rgb_list.append(self.img[i,j])

        return self.rgb_list


    # Encrypts the 2D array returned from pixel_array(),
    # returns the encrypted 2D array.
    def transform(self):
        """
        Converts the Red(R), Green(G), and Blue(B) values from 
        the x,y coordinates of the pixels in the image and encrypts
        the RGB values using the LFSR data type.
        """
        # Calls the pixel_array method to read the RGB values from the
        # x,y coordinates in the image.
        self.rgb_list = self.pixel_array()
        # List to store the encrypted RGB values.
        self.encrypted_rgb_list = []
        # Temp list that will help in creation of a list of lists.
        self.temp_list = []
        # The Red(R), G(Green), and Blue(B) colors, so it's easier
        # to understand that we're iterating through only these colors.
        self.colors = ["RED", "GREEN", "BLUE"]

        # For every pixel, there is a RGB value stored in the list.
        # This loop will iterate through each RGB value of the pixel
        # and encrypt every Red, Green, and Blue value using the LFSR.
        for i in range(len(self.rgb_list)):
            for j in range(len(self.colors)):
                # Generates a new binary number using the LFSR encryption.
                decimal = self.lfsr.step()

                # Reads the individual R, G, B value and compares it to
                # the LFSR binary number and perform XOR function.
                old_rgb = self.rgb_list[i][j]
                new_rgb = old_rgb ^ decimal
                self.temp_list.append(new_rgb)

                # Once one iteration of encryption is complete, the 
                # seed is overridden with the calculated LFSR.
                new_seed = self.lfsr.calc_lfsr
                self.lfsr.seed = new_seed
            
            # Once one iteration of a pixel (RGB) is done, the encrypted
            # value is then stored in a list of lists.
            self.encrypted_rgb_list.append(self.temp_list)
            self.temp_list = []

        return self.encrypted_rgb_list

            
    # Converts the encrypted 2D array back into an image named file_name    
    def save_image(self, new_file: str):
        """
        Takes the encrypted pixel information and loads it to a new image,
        one pixel at a time.
        """
        # File path to store the encrypted pixel image.
        self.new_file = new_file
        # Extracts the encrypted RGB list.
        self.encrypted_rgb_list = self.transform()

        # Creates a new image with the same size as the original image.
        self.new_img = Image.new(mode = "RGB", size = (self.width, self.height))
        # self.new_img.show()
        # Allocates storage for image and loads pixel data.
        self.new_px = self.new_img.load()

        k = 0
        # Adds the encrypted RGB as x,y pixel coordinates of the image.
        for i in range(self.width):
            for j in range(self.height):
                self.new_px[i, j] = tuple(self.encrypted_rgb_list[k])
                k = k + 1

        # Saves the image.
        self.new_img.save(self.new_file, format="PNG")
        # Shows the saved image.
        self.new_img.show()


# The main method calls the image encryption method and the
# image decryption methods.
def main():
    print()
    encrypt_image()
    decrypt_image()


# Encrypts an image.
def encrypt_image():
    """
    Encrypts the original file and saves it to the
    folder provided by the user.
    """
    error = "Please correct the file path"

    try:
        original_file = input("Please enter absolute path of an image to encrypt: ")
    except FileNotFoundError:
        print(error)

    seed = "10011010"
    tap = 5
    # Creates a new object of ImageEncrypter data type.
    img = ImageEncrypter(LFSR(seed, tap), original_file)

    try:
        encrypted_file = input("Please enter absolute path to save the encrypted image: ")
    except FileNotFoundError:
        print(error)
    
    # Saves the image to the file.
    img.save_image(encrypted_file)

# Decrypts the encrypted image.
def decrypt_image():
    """
    Decrypts the encrypted image and saves it to the
    folder provided by the user.
    """

    try:
        original_file = input("Please enter absolute path of the encrypted image: ")
    except FileNotFoundError:
        print(error)

    seed = "10011010"
    tap = 5
    # Creates a new object of ImageEncrypter data type.
    img = ImageEncrypter(LFSR(seed, tap), original_file)

    try:
        decrypted_file = input("Please enter absolute path to save the decrypted image: ")
    except FileNotFoundError:
        print("Please correct the file path")

    # Saves the image to the file.
    img.save_image(decrypted_file)


# Excecutable code.
if __name__ == "__main__":
    main()