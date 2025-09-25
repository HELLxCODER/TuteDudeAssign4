try:
    file1 = open('file1.txt', 'r')
    read_file = file1.read()
except FileNotFoundError:
    print("Error: the file was not found.")
finally:
    print(read_file)
    print("Execution completed.")
