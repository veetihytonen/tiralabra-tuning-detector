import wave as wa
import numpy as np

# Expected values of bit depth and sampling rate
BIT_DEPTH = 16
SAMPLING_RATE = 44100


class FileReader:
    """
    Wrapper for opening and reading WAV file content.

    Requirements for file encoding:
    - PCM
    - 16 bits
    - 44.1kHz

    Other encodings are not supported for now.
    """

    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path

    def __open_file(self) -> wa.Wave_read:
        """
        Currently only supports WAV files with PCM encoding, 
        which is by far the most common encoding for WAV files.
        """
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
                "File is not in WAV format, is not PCM encoded, "
                f"or is corrupted: {self.__file_path}"
            )
            raise

        return reader

    def __validate_file_format(self, reader: wa.Wave_read) -> None:
        """
        This funcion checks that the sample uses 16 bit encoding and 44.1kHz sampling rate,

        as that is a common standard for digital audio, sometimes referred to as CD quality.

        For now, other formats are not supported.
        """

        # Sample width corresponds to number of bytes per sample in raw data.
        # Eg. sample width of 2 means each sample is two bytes aka. 16 bits in raw data
        # We divide BIT_DEPTH by 8 to get target number of bytes the file should use per sample
        if reader.getsampwidth() != BIT_DEPTH / 8:
            print(
                "\n"
                f"File uses {8 * reader.getsampwidth()} bit encoding. "
                f"Please provide file with {BIT_DEPTH} bit encoding."
            )
            raise ValueError("Wrong encoding")

        if reader.getframerate() != SAMPLING_RATE:
            print(
                "\n"
                f"File uses sampling rate of {reader.getframerate()}kHz. "
                f"Please provide file with sampling rate of {SAMPLING_RATE}kHz."
            )
            raise ValueError("Wrong sampling rate")

    def read_file(self) -> np.ndarray:
        try:
            reader = self.__open_file()
        except (FileNotFoundError, EOFError, wa.Error):
            raise

        try:
            self.__validate_file_format(reader)
        except ValueError:
            raise

        raw = reader.readframes(64)
        reader.close()

        data = np.frombuffer(raw, dtype=np.int16)

        return data
