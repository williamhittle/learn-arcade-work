# this is my python file with comments and code
#
# the pound symbol is how to make comments
#
# let's print hello world, or a variation therof
print("hello there")
# cool!  note that Python lets you use single or double quotes, but you have to use the same to start/end.
print('hi back')
# when I start typing, it fills in the second bit
# this can help if I want to use a ' somewhere
print("Hey, it's a new world")
# which would break if I typed 'Hey, it's a new world'
# a multi-line statement can be done with 3 double quotes:
print("""Hello there.
How are you doing?
I'm fine, thank you very much.
""")

# let's add some print functions that fail, just to see how it goes
# I have to comment these out to keep PyCharm and Python happy.
#Print("No working...")
#print  "still not working..."
print   ("almost fine, but editing isn't the best")
print("got it!")
# all of that should work fine

print("Note the subsequent print statements show up in the \"Run\" window with a blank line between them.")
print("Also note, I have to use an escape code to make this \" appear")
print("""There are escape codes for single quotes like \',
double quotes like \" (seen above),
and also for things lik a tab that can be used to intent a line
\tlike this.""")
print("""Be careful when using\\r, because if you type it in the middle of a line of code and keep writing,
it'll print everything after the \\r from the starting position,
which can overwrite stuff.
Watch as this line is erased. \\r by this 
when I leave the \\r in as a carriage return
Watch as this line is erased. \r by this
""")
print("""You probably meant to use \\n,
which puts a new line in\nwhile all the code\nstays on the same line.
""")