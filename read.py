import cv2
import gzip
from config import *
import pickle
from deepgtav.messages import frame2numpy

def parserCommands(dct):
    """
    parse the Commands from every frame and return
    :param dct: dct read from the file
    :return: throttle, brake and steering
    """
    return dct['throttle'], dct['brake'], dct['steering']

def parserState(dct):
    """
    return the dict including the state of the vehicle
    :param dct: dct read from the file
    :return: location list, speed and yawRate
    """
    stateDict = {}
    stateDict['location'] = dct['location']
    stateDict['speed'] = dct['speed']
    stateDict['yawRate'] = dct['yawRate']
    return stateDict

if __name__ == '__main__':
    command_list = []
    state_list = []
    frame_list = []
    # open the dataset.pz file
    with gzip.open(
            filename=GFILE_PATH, mode='rb', compresslevel=0
    ) as f:

        while True:
            try:
                dct = pickle.load(f)
                # show frame
                frame = frame2numpy(dct['frame'], (FRAME[0], FRAME[1]))
                # frame_list.append(frame)
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                # get command and state of the vehicle
                throttle, brake, steering = parserCommands(dct)
                stateDict = parserState(dct)
                # command_list.append((throttle, brake, steering))
                # state_list.append(stateDict)
            except EOFError:
                break

        cv2.destroyAllWindows()
