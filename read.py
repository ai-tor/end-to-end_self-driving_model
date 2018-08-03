import cv2
import gzip
from config import *
from deepgtav.messages import frame2numpy

if __name__ == '__main__':
    # open the dataset.pz file
    with open(GFILE_PATH, 'rb') as f:
        gzip_handler = gzip.GzipFile(mode='rb', fileobj=f)

        # decompress the file and show the video
        while gzip_handler.readable():
            item = gzip_handler.readline()
            image = frame2numpy(item, (FRAME[0], FRAME[1]))
            cv2.imshow('CapturedVideo', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
