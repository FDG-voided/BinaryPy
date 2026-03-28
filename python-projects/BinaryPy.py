class BinaryPy:
    def __init__(self):
     self.conv_digits = [128, 64, 32, 16, 8, 4, 2, 1]
        
    def convertDtoB(self, digit):
        self.binary_list = []
        for i in self.conv_digits:
            if digit >= i:
                digit = digit - i
                self.binary_list.append(1)
            else:
                self.binary_list.append(0)

        return self.binary_list

    def convertBtoD(self, binary):
        denary_digit = 0

        for bit, value in zip(binary, self.conv_digits):
            if bit == 1:
                denary_digit += value

        return denary_digit

    def bitwise_and(self, list1, list2):
        return [b1 & b2 for b1, b2 in zip(list1, list2)]


    def bitwise_or(self, list1, list2):
        return [b1 | b2 for b1, b2 in zip(list1, list2)]
    

    def bitwise_xor(self, list1, list2):
        return [b1 ^ b2 for b1, b2 in zip(list1, list2)]

    def bitwise_not(self, list1):
        return [1 - b for b in list1]

