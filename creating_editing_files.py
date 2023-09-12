"""
Open or create a file then
1. write to the file.
2. Also read from the file.
"""

olympicsfile = open("reading.txt", "w")

olympicsfile.write("""I am new here \n
My name is Reindorf Tawiah Narh and I am a student.\n
I hope to do something very meaningful with my life.""")

olympicsfile.write("""
This is another one. \n
I want to see if it will add up or delete the first one.""")
olympicsfile.close()
