class process_data:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = open(file_path, "r+")
        
    def print_data(self):
        self.data.seek(0)
        lines = self.data.readlines()
        for line in lines:
            print(line[0:-1])

    def write_data(self, info):
        self.data.write(info)

    def close_file(self):
        self.data.close()

    def count_words(file_path) -> int:
        with open(file_path, "r") as f:
            data = f.read()
            words = data.split()
            f.close()
            print(len(words))
            return len(words)

if __name__ == "__main__":
    process_data.count_words("demo_file.txt")