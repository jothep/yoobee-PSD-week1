class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def get_length(self):
        length = len(self.text)
        return length

    def set_String(self):
        return self.text.capitalize()

name = StringManipulator("example")

result = name.find_character("x")
length = name.get_length()
result_Cap = name.set_String()

print(length)
print(result_Cap)

