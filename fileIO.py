import os

class FileIO:
    @staticmethod
    def readAsString(fName):
        try:
            """read info from file, if file exists. return a string"""
            with open(str(fName)) as f:
                data = f.read()
                f.close()
                return data
        except FileNotFoundError:
            # we want a string either way, but this way we can let the calling class decide business logic
            return ""

    @staticmethod
    def readAsPosInt(fName):
        try:
            """read info from file. If file exists, return a positive int, negative for errors"""
            with open(str(fName)) as f:
                data = f.read()
                f.close()
                if data.isnumeric():
                    return int(data)
                else:
                    return 0
        except Exception:
            # if there's no file, or the file has invalid data, return -1 for value
            return -1

    @staticmethod
    def mkdir(newDir):  # returns an int to indicate status, 1 created, 0 already exists, -1 error
        try:
            os.mkdir(str(newDir))
            return 1
        except FileExistsError:
            return 0
        except Exception:
            return -1

    @staticmethod
    def pathJoin(directory,file):
        # wrapper for path join to eliminate importing os elsewhere
        return os.path.join(str(directory),str(file))

    @staticmethod
    def overwrite(fName, data):
        with open(fName, 'w') as f:
            f.write(str(data))

    @staticmethod  # not needed in this project, but good to have if we use this class elsewhere
    def append(fName, data):
        with open (str(fName)) as current:
            data = current.read() + data
            current.close()
        with open(str(fName),'w') as f:
            f.write(data)
            f.close()
