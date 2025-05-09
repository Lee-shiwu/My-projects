import os
import pandas as pd
from PIL import Image

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.extension = os.path.splitext(file_path)[1].lower()
        self.data = None

    def process(self):
        if self.extension == '.csv':
            self._process_csv()
        elif self.extension == '.parquet':
            self._process_parquet()
        elif self.extension == '.txt':
            self._process_text()
        elif self.extension in ['.jpg', '.jpeg', '.png']:
            self._process_image()
        else:
            print(f"Unsupported file type: {self.extension}")

    def _process_csv(self):
        self.data = pd.read_csv(self.file_path)
        print(f"CSV file loaded: {self.file_path}")
        self._summarize_tabular()

    def _process_parquet(self):
        self.data = pd.read_parquet(self.file_path)
        print(f"Parquet file loaded: {self.file_path}")
        self._summarize_tabular()

    def _process_text(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        print(f"Text file loaded: {self.file_path}")
        print(f"Total lines: {len(lines)}")
        print(f"First 5 lines:\n{''.join(lines[:5])}")

    def _process_image(self):
        img = Image.open(self.file_path)
        print(f"Image file loaded: {self.file_path}")
        print(f"Format: {img.format}, Size: {img.size}, Mode: {img.mode}")

    def _summarize_tabular(self):
        print("\nData Info:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nSummary Statistics:")
        print(self.data.describe())


def main():
    file_path = "F:\master\Sample-1m.parquet"  # or .txt / .jpg / .parquet
    processor = DataProcessor(file_path)
    processor.process()

if __name__ == "__main__":
    main()
