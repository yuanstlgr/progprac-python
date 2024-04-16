from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
import sys
'''
the shorten_path function shortens the path to a specified maximum length (default is 50 characters) by keeping the 
first and last parts of the path and replacing the middle with '...'. The setToolTip method sets the tooltip of the 
label to the full path, so the full path will be displayed when the user hovers over the label.
'''


def shorten_path(path, max_length=50):
    if len(path) > max_length:
        return path[:max_length//2] + '...' + path[-max_length//2:]
    return path


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QVBoxLayout
        layout = QVBoxLayout()

        # Create a QLabel
        self.image_path_label = QLabel()

        # Add the QLabel to the QVBoxLayout
        layout.addWidget(self.image_path_label)

        # Set the QVBoxLayout as the layout for the MainWindow
        self.setLayout(layout)

        # Set a long image path
        image_path = ("/this/is/a/very/long/path/to/an/image/file/that/needs/to/be/shortened"
                      "/for/display/purposes/image.png")

        # Shorten the image path and set it as the text of the QLabel
        shortened_path = shorten_path(image_path)
        self.image_path_label.setText("> Image Path: " + shortened_path)

        # Set the full image path as the tooltip of the QLabel
        self.image_path_label.setToolTip(image_path)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
