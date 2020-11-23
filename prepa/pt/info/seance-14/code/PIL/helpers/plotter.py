import matplotlib.pyplot as plt
import numpy as np
import PIL


class Plotter:

    def __init__(self, name=''):
        self.imageToPlot = []
        self.name = name
        plt.rcParams['toolbar'] = 'None'

    def addSubplot(self, image, name='', axis=False):
        if type(image) == PIL.JpegImagePlugin.JpegImageFile:
            image = np.array(image)
        cmap = 'gray' if image[0][0].size == 1 else 'viridis'

        self.imageToPlot.append(ImageToPlot(image, cmap, name, axis))

    def show(self):
        plt.suptitle(self.name, fontsize=22, fontweight=4, color='#2c3e50')
        l = len(self.imageToPlot)
        nbOfColumn = int(np.sqrt(l))
        nbOfLines = l // nbOfColumn
        nbOfLines = nbOfLines if l % nbOfColumn == 0 else nbOfLines + 1

        i = 0
        for img in self.imageToPlot:
            i += 1
            plt.subplot(nbOfColumn, nbOfLines, i)
            plt.imshow(img.image, cmap=img.colorMode)
            if not img.axis:
                plt.axis('off')
                plt.title(img.name, fontweight='bold', color='#27ae60')
                plt.margins(0, 0)
                plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                                    hspace=0, wspace=0)
            pass

        figManager = plt.get_current_fig_manager()
        # figManager.window.showMaximized()
        plt.show()


class ImageToPlot:
    def __init__(self, image, colorMode, name, axis):
        self.image = image
        self.colorMode = colorMode
        self.name = name
        self.axis = axis
