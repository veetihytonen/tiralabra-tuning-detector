from argparse import ArgumentParser
from file_reader import FileReader

def main(file_path: str):
    reader = FileReader(file_path)
    try:
        print(reader.read_file())
    except:
        exit()

if __name__  == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--file")
    args = parser.parse_args()

    main(args.file)
