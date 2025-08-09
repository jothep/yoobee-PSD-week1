class StringManipulator:
    def find_character(text, char):
        return text.find(char)
    
    def get_length(text):
        return len(text)

    def set_String(text):
        return text.upper()

string1 = "example"
result = StringManipulator.find_character(text=string1, char="x")
length = StringManipulator.get_length(text=string1)
result_Upper = StringManipulator.set_String(text=string1)

print(result)
print(length)
print(result_Upper)