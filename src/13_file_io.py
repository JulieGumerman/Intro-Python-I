"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open("foo.txt", "r") as finish_this:
    read_data = finish_this.read()
    print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
some_lines = "The Raven himself is hoarse \n"
more_lines = "Tomorrow, and tomorrow, and tomorrow \n"
# YOUR CODE HERE
with open("bar.txt", "w") as write_this:
    write_this.write("Haiii \n")
    write_this.writelines(some_lines)
    write_this.writelines(more_lines)
    