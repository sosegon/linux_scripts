import sys
import os
import glob
import main_window
from PyQt4 import QtGui

class ImageScene(QtGui.QGraphicsScene):
    def __init__(self, parent):
        QtGui.QGraphicsScene.__init__(self, parent)
        self.reset()

    def reset(self):
        while len(self.items()) > 0:
            item = self.items()[-1]
            self.removeItem(item)

class ImageClassifier(QtGui.QMainWindow, main_window.Ui_Dialog):
    def __init__(self):
        
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.image_extensions = ["png", "jpg", "ppm"]
        self.src_folder_path, self.dst_folder_path = "", ""
        self.image_paths = []

        self.scene = ImageScene(self)

        # Listeners for buttons
        self.btn_src.clicked.connect(lambda: self.open_folder(self.lbl_src))
        self.btn_dst.clicked.connect(lambda: self.open_folder(self.lbl_dst))
        self.btn_start.clicked.connect(self.start_classification)

    def open_folder(self, qlabel):
        command = "Open Directory"
        path = os.path.dirname(os.path.abspath(__file__))
        folder_name = QtGui.QFileDialog.getExistingDirectory(
            self, 
            command, 
            path, 
            QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)

        qlabel.setText(folder_name)

    def start_classification(self):
        self.src_folder_path = str(self.lbl_src.text())
        self.dst_folder_path = str(self.lbl_dst.text())

        if(self.src_folder_path == "" or self.dst_folder_path == ""):
            return

        self.image_paths = self.get_files(self.src_folder_path, True)

        for im_path in image_paths:
            

    def get_files(self, dir_path, recursive):
        file_names = []
        for fname in glob.glob(dir_path + "/**/*", recursive=recursive):
            print(fname)
            if self.is_image_path(fname):
                file_names.append(fname)

        return file_names


    def is_image_path(self, file_name):
        reverse = file_name[::-1]
        try:
            dot_index = reverse.index(".")
            extension = reverse[:dot_index][::-1].lower().strip()
            return extension in self.image_extensions
        except:
            return False


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ImageClassifier()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    sys.exit(app.exec_())
    #app.exec_()                         # and execute the app

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()    