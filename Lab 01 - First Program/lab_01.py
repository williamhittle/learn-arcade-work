print("Some notes for myself:")
print("__________")
print("I like to use print statements with triple \" marks.")
print("""
When I do that, I like to write my code with the \"\"\" before and after my block of text,
but note that doing so adds extra spaces to the output,
because Python is counting those \"returns\" as keystrokes that need to get printed.
""")
print("Also note, I have to use an escape code to make this \" appear.")
print("""There are escape codes for single quotes like \',
double quotes like \" (seen above),
and also for things like a tab that can be used to indent a line
\tlike this.
""")
print("""Be careful when using \\r, because if you type it in the middle of a line of code and keep writing,
it'll print everything after the \\r from the starting position,
which can overwrite stuff.
Watch as this line is erased \\r by this chunk
when I leave the \\r in as a carriage return:
Watch as this line is erased \r by this chunk.
""")
print("""Maybe you meant to use \\n,
which puts a new line in\nwhile all the code\ncan stay on the same line.
Or just type things in as a new line with the triple-double-quotes, \"\"\".
""")