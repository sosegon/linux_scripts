import sys
import os
import glob
import main_window
from PyQt4 import QtGui, QtCore

from skimage import io
import shutil

# from http://stackoverflow.com/a/7376838/1065981
try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str

class ImageScene(QtGui.QGraphicsScene):
    def __init__(self, parent):
        QtGui.QGraphicsScene.__init__(self, parent)
        self.reset()

    def reset(self):
        while len(self.items()) > 0:
            item = self.items()[-1]
            self.removeItem(item)

class ImageClassifier(QtGui.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.image_extensions = ["png", "jpg", "ppm"]
        self.src_folder_path, self.dst_folder_path = "", ""
        self.valid_images_folder_path = "" # to store classified images
        self.discarded_images_folder_path = "" # to store classified images
        self.classes_file_name = "" # csv with paths to images and classes
        self.image_paths = []
        self.isClassifying = False
        self.classified_count = 0
        self.discarded_count = 0
        self.current_file_name = ""

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

        self.image_paths = self.get_file_paths(self.src_folder_path, True)

        if len(self.image_paths) == 0:
            self.statusbar.showMessage(QString("No images to classify"))

        # Create folder for images
        self.valid_images_folder_path = self.dst_folder_path + "/valid_images"
        self.discarded_images_folder_path = self.dst_folder_path + "/discarded_images"
        os.makedirs(self.valid_images_folder_path)
        os.makedirs(self.discarded_images_folder_path)

        # Create csv file with paths and classes
        self.classes_file_name = self.dst_folder_path + "/data.csv"
        with open(self.classes_file_name, "w+") as f:
            try:
                f.writelines("path, class")
            finally:
                f.close()

        self.txt_class_name.setEnabled(True)
        self.txt_class_name.setFocus()
        self.isClassifying = True

        self.current_file_name = self.image_paths[self.classified_count + self.discarded_count]
        self.open_image(self.current_file_name)
    
    def keyPressEvent(self, event):
        if self.isClassifying:
            file_name = self.get_file_name(self.current_file_name)
            if event.key() == QtCore.Qt.Key_Enter:
                full_new_name = self.valid_images_folder_path + "/" + file_name
                shutil.copyfile(self.current_file_name, full_new_name)

                relative_path = "./images/" + file_name
                clazz = str(self.txt_class_name.text()).lower().strip()
                with open(self.classes_file_name, "a") as f:
                    try:
                        f.writelines("\n" + relative_path + ", " + clazz)
                    finally:
                        f.close()
                self.classified_count += 1
                remaining = len(self.image_paths) - self.discarded_count - self.classified_count
                self.statusbar.showMessage(QString("Remaining images: " + str(remaining) + ", " + file_name + " classified as " + clazz))
            elif event.key() == QtCore.Qt.Key_Escape:
                full_new_name = self.discarded_images_folder_path + "/" + file_name
                shutil.copyfile(self.current_file_name, full_new_name)
                self.discarded_count += 1
                remaining = len(self.image_paths) - self.discarded_count - self.classified_count
                self.statusbar.showMessage(QString("Remaining images: " + str(remaining) + ", " + file_name + " discarded"))

            self.txt_class_name.setFocus()
            self.txt_class_name.clear()
            total_count = self.classified_count + self.discarded_count
            
            if total_count >= len(self.image_paths):
                self.txt_class_name.setEnabled(False)
                self.statusbar.showMessage(QString("Files classified: " + str(self.classified_count) + ", Files discarded: " + str(self.discarded_count)))
                self.isClassifying = False

            self.current_file_name = self.image_paths[total_count]
            self.open_image(self.current_file_name)

    def open_image(self, file_name):
        self.scene.reset()

        pxm_image = QtGui.QPixmap(file_name)
        self.scene.addPixmap(pxm_image)
        self.gv_image.setScene(self.scene)

        self.image_file_name = str(file_name)
        self.image_data_array = io.imread(self.image_file_name)

    def get_file_paths(self, dir_path, recursive):
        file_names = []
        for fname in glob.glob(dir_path + "/**/*", recursive=recursive):
            if self.is_image_path(fname):
                file_names.append(fname)

        return file_names

    def is_image_path(self, file_name):
        return self.get_file_extension(file_name) != -1

    def get_file_extension(self, file_name):
        reverse = file_name[::-1]
        try:
            dot_index = reverse.index(".")
            extension = reverse[:dot_index][::-1].lower().strip()
            return extension
        except:
            return -1

    def get_file_name(self, file_name):
        reverse = file_name[::-1]
        try:
            dot_index = reverse.index("/")
            extension = reverse[:dot_index][::-1].lower().strip()
            return extension
        except:
            return -1

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ImageClassifier()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    sys.exit(app.exec_())
    #app.exec_()                         # and execute the app

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()    