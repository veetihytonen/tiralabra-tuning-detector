import wave as wa

class FileReader:
    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path

    def __open_file(self) -> wa.Wave_read:
        try:
            reader = wa.open(self.__file_path, "rb")
        except FileNotFoundError:
            print(
                "\n"
                f"File couldn't be found: {self.__file_path}"
                "\n\n"
                "Make sure your file path relative to the directory you are running the command in."
            )
            raise
        except (EOFError, wa.Error):
            print(
                "\n"
                f"File is not in WAV format or is corrupted: {self.__file_path}"
            )
            raise

        return reader