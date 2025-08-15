class process_data:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = open(file_path, "r+")
        
    def print_data(self, startline, endline):
        lines = self.data.readlines()
        for line in lines:
            print(line[startline:endline])

    def write_data(self, info):
        self.data.write(info)

    def close_file(self):
        self.data.close()

if __name__ == "__main__":
    pd = process_data("demo_file.txt")
    pd.write_data("new line 1\n")
    pd.print_data(0,5)
    pd.close_file()