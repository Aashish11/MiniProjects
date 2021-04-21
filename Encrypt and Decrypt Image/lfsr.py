"""
Created on Fri Apr 2, 2021
@author: Ashish Singh

"""

# A class object of LFSR data type.
class LFSR:

    # Creates an LFSR with initial state "seed", tap, 
    # and LFSR by calling the step method.
    def __init__(self, seed: str, tap: int):
        """
        The constructor not only assigns the values for seed 
        and tap, but it also calls the step method to calculate
        one iteration of LFSR.
        """
        self.seed = seed
        self.tap = tap


    # Executes one LFSR iteration and returns new binary number.
    def step(self):
        """
        The seed value is passed as string. The character of the seed 
        at index "tap", and the character at index 0 is evaluated 
        using XOR and added to the end of the string, which then
        forms a Linear Feedback Shift Register (LFSR).

        The binary LFSR is then converted to a decimal number (whole number).
        """
        # Length of the seed.
        length = len(self.seed)
        # Extracts the first character of the seed.
        first_char = int(self.seed[0])
        # Calculates the index that needs to be XOR'ed.
        lfsr_index = length - self.tap
        # Extracts the character that needs to be XOR'ed.
        compare_char = int(self.seed[lfsr_index])
        # XOR comparison.
        xor = first_char^compare_char
        # XOR'ed character added to the end of the string.
        self.calc_lfsr = self.seed[1:length] + str(xor)
        # Binary number converted to decimal number.
        self.num = self.return_num()

        return self.num


    # Calculates the length of the lfsr.
    def __len__(self):
        text = str(self.calc_lfsr)
        return len(text)


    # Returns the string representation of the LFSR.
    def __str__(self):
        """
        Once an LFSR is created the __str__ method
        is overloaded to print in a desired format.
        """
        self.step()
        text = self.calc_lfsr[0]
        for i in range(1, len(self.calc_lfsr)):
            text = text + self.calc_lfsr[i]

        text = text + " " + self.calc_lfsr[-1]

        return text


    # Converts binary to decimal.
    def return_num(self):
        """
        Converts the LFSR binary to decimal (whole number).
        """
        text = str(self.calc_lfsr)
        decimal = int(text, 2)
        return decimal



# Excecutable code.
if __name__ == "__main__":
    lfsr1 = LFSR("0110100111", 2)
    lfsr2 = LFSR("0100110010", 8)
    lfsr3 = LFSR("1001011101", 5)
    lfsr4 = LFSR("0001001100", 1)
    lfsr5 = LFSR("1010011101", 7)

    print(lfsr1)
    print(lfsr2)
    print(lfsr3)
    print(lfsr4)
    print(lfsr5)