import os

class FileIO:
    @staticmethod
    def readAsString(fName):
        try:
            """read info from file, if file exists. return a string"""
            with open(fName) as f:
                data = f.read()
                return data
        except FileNotFoundError:
            # we want a string either way, but this way we can let the calling class decide business logic
            return ""

    @staticmethod
    def readAsPosInt(fName):
        try:
            """read info from file. If file exists, return a positive int, negative for errors"""
            with open(fName) as f:
                data = f.read()
                if data.isnumeric():
                    return int(data)
                else:
                    return 0
        except ValueError:
            # if there's no file, or the file has invalid data, return -1 for value
            return -1

    @staticmethod
    def mkdir(newDir):  # returns an int to indicate status, 1 created, 0 already exists, -1 error
        try:
            os.mkdir(newDir)
            return 1
        except FileExistsError:
            return 0
        except Exception:
            return -1

    @staticmethod
    def pathJoin(directory,file):
        # wrapper for path join to eliminate importing os elsewhere
        os.path.join(directory,file)
