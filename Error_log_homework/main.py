def main():
    file_name = input("Enter the file name here: ")
    # file_name = 'ErrorLog.txt'
    try:
        with open(file_name, 'rt') as data:
            lines = data.readlines()
            line_count = 0
            error_count = 0
            for line in lines:
                error_words = ['error', 'Error', 'ERROR']
                for words in error_words:
                    if words in line:
                        error_count += 1
                        print(line, end='')
                if line.strip():
                    line_count += 1

            with open('reportError.txt', 'w') as report:
                report.write("LinesCounts=" + str(line_count))
                print("LinesCounts=" + str(line_count))
                report.write("\r")
                report.write("ErrorCounts=" + str(error_count))
                print("ErrorCounts=" + str(error_count))
    except:
        print("File read/write Error!")



if __name__ == '__main__':
    main()

