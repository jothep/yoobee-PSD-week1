class process_data:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def print_data(self, start_line: int = 0, end_line: int = -1):
        data = open(self.file_path, "r+")
        data.seek(0)
        lines = data.readlines()
        for line in lines[start_line:end_line]:
            print(line[0:-1])
        data.close()

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
    #process_data.count_words("demo_file.txt")
    pd = process_data("demo_file.txt")
    pd.print_data()