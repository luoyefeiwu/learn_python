class OperateFile(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def openFile(self):
        try:
            f = open(self.filePath, 'w+', encoding='utf-8')
            f.write('大侠')
        finally:
            if f:
                f.close()

    def withFile(self):
        with open(self.filePath, 'r', encoding='utf-8') as f:
            print(f.read())
