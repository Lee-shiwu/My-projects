import pandas as pd
import math

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or Parquet.")
        print(f"Data loaded successfully from {self.file_path}")

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")

        print("Initial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())

    def calculate_sin_cos(self, angle_deg):
        angle_rad = math.radians(angle_deg)
        sin_val = round(math.sin(angle_rad), 4)
        cos_val = round(math.cos(angle_rad), 4)
        print(f"Sin({angle_deg}°) = {sin_val}")
        print(f"Cos({angle_deg}°) = {cos_val}")

    def calculate_circle_area(self, diameter):
        radius = diameter / 2
        area = math.pi * radius ** 2
        print(f"Area of a circle with diameter {diameter} is {round(area, 4)}")

def main():
    file_path = "F:\master\sample_junk_mail.csv"
    processor = DataProcessor(file_path)

    processor.load_data()
    processor.initial_processing()

    try:
        angle = float(input("Enter an angle in degrees to calculate Sin and Cos: "))
        processor.calculate_sin_cos(angle)
    except ValueError:
        print("Invalid input for angle.")

    try:
        diameter = float(input("Enter the diameter of a circle to calculate its area: "))
        processor.calculate_circle_area(diameter)
    except ValueError:
        print("Invalid input for diameter.")

if __name__ == "__main__":
    main()
