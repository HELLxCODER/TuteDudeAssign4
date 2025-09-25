file1 = open("Output.txt", "w")
input_data = input("Enter your text: ")
file1.write(input_data)
file1.close()

file1 = open("Output.txt", "a")
input_data = input("Enter additional text: ")
file1.write("\n" + input_data)
file1.close()

file1 = open("Output.txt", "r")
read_file = file1.read()
print(read_file)