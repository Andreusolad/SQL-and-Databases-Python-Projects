from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtWidgets import QComboBox
import sys

class SpeedCalculator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time")
        self.time_line_edit = QLineEdit()

        # Create button
        calculate_button = QPushButton("Calculate Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Create select box
        self.combo = QComboBox()
        self.combo.addItems(["Metric (km)", "Imperial (miles)"])

        self.result_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):

        d = float(self.distance_line_edit.text())
        t = float(self.time_line_edit.text())
        speed = d/t
        if self.combo.currentText() == "Metric (km)":
            speed = round(speed, 2)
            unit = "km/h"
        if self.combo.currentText() == "Imperial (miles)":
            speed = round(speed * 0.621371, 2)
            unit = "mph"

        # Display the result
        self.output_label.setText(f"Speed is {speed} {unit}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
