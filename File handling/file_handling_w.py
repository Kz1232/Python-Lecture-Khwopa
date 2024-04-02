'''#Approach 1 
file_obj=open('file.txt',"w")
file_obj.write('This is some random stuff')
file_obj.close()
'''
#Approach 2
with open('file2.txt',"w") as file_obj:
    file_obj.write("The is some random stuff in file 2")


