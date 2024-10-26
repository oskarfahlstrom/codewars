# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key
    
    def encode(self, text):
        string = ""
        for i, c in enumerate(text):
            if (index := self.alphabet.find(c)) == -1:  # char not in alphabet
                string += c
                continue
            string += self.alphabet[
                (index + self.alphabet.find(
                    self.key[i % len(self.key)])) % len(self.alphabet)]
        return string         
    
    def decode(self, text):
        string = ""
        for i, c in enumerate(text):
            if (index := self.alphabet.find(c)) == -1:  # char not in alphabet
                string += c
                continue
            string += self.alphabet[
                (len(self.alphabet) + index - self.alphabet.find(
                    self.key[i % len(self.key)])) % len(self.alphabet)]
        return string
