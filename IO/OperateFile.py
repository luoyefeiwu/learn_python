class OperateFile(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def openFile(self):
        try:
            f = open(self.filePath, 'r', encoding='utf-8')
        finally:
            if f:
                f.close()

    def withFile(self):
        with open(self.filePath, 'r', encoding='utf-8') as f:
            print(f.read())
