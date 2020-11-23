import json
import os.path as Path
import os
import binascii
import cv2.cv2 as cv
from constants import STORAGE_PATH, STORAGE_FILENAME, ALL_FRAMES_ADDED_FOLDER, LIST_MAXI_FILENAME
from helpers.pat import getNameWithExt


def saveProcessedVideos(_id, dataToSave):
    """
    @param: videoPath: path of video file that has been croped
    @param: a, b, c, d : 4 parameters resulting from croping
    """
    storagePath = Path.join(STORAGE_PATH, STORAGE_FILENAME)

    data = appendJson(storagePath, 'processedVideos', _id, dataToSave)

    # On écrit le tout dans le Json
    with open(storagePath, 'w') as outfile:
        json.dump(data, outfile)


def saveCroping(fileName, a, b, c, d):

    data = {
        'croping': {
            'a': a,
            'b': b,
            'c': c,
            'd': d,
        }
    }

    saveProcessedVideos(fileName, data)


def saveCalibration(fileName, h, s, v, step):

    data = {
        'calibration': {
            'h': h,
            's': s,
            'v': v,
            'step': step,
        }
    }

    saveProcessedVideos(fileName, data)


def openJson(path):
    """
    @param: path of Json file

    @retutrn:   - False if Json empty or does not exist
                - Content of Json else
    """

    # Si le fichier n'exsite pas, on le crée, et on renvoit {}
    if (not os.path.exists(path)):
        open(path, 'x')
        return {}

    # On ouvre le JSON
    with open(path) as json_file:
        # On essaie de lire le JSON
        try:
            data = json.load(json_file)
            if(not data):
                # Fichier vide
                return {}
            return data

        # On arrive pas à lire le JSON, il est probablement vide
        except json.decoder.JSONDecodeError:
            return {}


def appendJson(path, collection, _id, data):
    """
    @param: path of Json file
    @param: collection: name of the collection where data will be added
    @param: _id: id of the element in wich we will add/upate data
    @param: data: data to append

    @return: json updated as python dictionnary
    """

    # On ouvre le fichier
    fileData = openJson(path)
    tempBool = False

    # On fait des trucs qui marchent
    if (collection in [*fileData]):
        for p in fileData[collection]:
            if (p['_id'] == _id):
                tempBool = True
                update_panel_json(p, data)
        if (not tempBool):
            data["_id"] = _id
            fileData[collection].append(data)
    else:
        data["_id"] = _id
        fileData[collection] = [data]
    return fileData


def update_panel_json(input_json, newValues):
    if type(input_json) is dict and input_json:
        keysToAdd = [*newValues]
        for key in input_json:
            if key in newValues.keys():
                del keysToAdd[keysToAdd.index(key)]
                input_json[key] = newValues[key]
                update_panel_json(input_json[key], newValues[key])
        for key in keysToAdd:
            input_json[key] = newValues[key]

    elif type(input_json) is list and input_json:
        for entity in input_json:
            update_panel_json(entity, newValues)


def getCroping(videoPath):
    return getData(videoPath, 'croping', ['a', 'b', 'c', 'd'])


def getCalibration(videoPath):
    return getData(videoPath, 'calibration', ['h', 's', 'v', 'step'])


def getData(_id, subCollection, listOfValuesToReturn):
    storagePath = Path.join(STORAGE_PATH, STORAGE_FILENAME)

    # On ouvre le Json (fichier de sauvegarde)
    data = openJson(storagePath)

    if (len([*data]) > 0):

        # Si le json n'est pas vide, on cherche si la vidéo a déjà été traitée
        # On revoit les données du crop, ou False
        for p in data['processedVideos']:
            if (p['_id'] == _id):
                if (subCollection in [*p]):
                    d = p[subCollection]
                    return tuple([d[k] for k in listOfValuesToReturn])
    return False


def saveStream(values, _id):
    storagePath = Path.join(STORAGE_PATH, _id + LIST_MAXI_FILENAME)
    with open(storagePath, 'a') as outfile:
        outfile.write(values)


def saveList(listMaxi):
    storagePath = Path.join(STORAGE_PATH, LIST_MAXI_FILENAME)
    r = ''
    for x, y, z in listMaxi:
        r += '{},{},{};'.format(x, y, z)
    with open(storagePath, 'w') as outfile:
        outfile.write(r)


if __name__ == '__main__':
    saveCalibration('3', 1, 1, 1, 1)
    saveCroping('3', 1, 1, 1, 1)
