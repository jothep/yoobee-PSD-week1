class StringManipulator:

#Using __init__ can easily initialize, define internal variables, and quickly call internal variables when using methods

    def find_character(self, text, char):
        return text.find(char)
    
    def get_length(self, text):
        return len(text)

    def set_String(self, text):
        return text.upper()

name = StringManipulator()
string1 = "example"
result = name.find_character(string1, "x")
length = name.get_length(string1)
result_Upper = name.set_String(string1)

print(result)
print(length)
print(result_Upper)