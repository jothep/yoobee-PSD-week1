class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def get_length(self):
        length = len(self.text)
        return length

    def set_String(self):
        return self.text.upper()
    
    def split_String(self):
        return self.text.split(' ')
    
    def count_sentence(self):
        list1 = self.split_String()
        length = len(list1)
        return length

inputString = input("Enter a Sentence: ").lower()
name = StringManipulator(inputString)

count = name.count_sentence()
print(count)
