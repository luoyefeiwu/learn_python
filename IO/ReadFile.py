from IO.OperateFile import OperateFile


def main():
    file = OperateFile('test.txt')
    file.openFile()
    file.withFile()

main()
