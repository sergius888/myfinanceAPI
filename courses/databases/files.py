# mode r -> for read, raises error if the file does not exist, by default
 # mode w -> for write, will create the file if it does not exist
 # mode a -> for append, for adding to the file

 # we need to open the file and get an object for IO (input & output)
 # file = open("file.txt", mode="w")
 # # to write just call the method 'write'
 # file.write("aaaaa\nbbbbbb\ncccccc")
 # file.close()

try:
    file = open("file2.txt")
except Exception as e:
    print('am avut o eroare', str(e))
    raise e


 # data = file.read()
 # file.close()
 # print(data)