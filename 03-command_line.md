# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. Pushd - pushes the current directory to a list and then changes to another directory
    2. Popd - returns to the the last directory that was pushed
    3. Touch - creates an empty file with the specified name
    4. cp - copies a file to a new file with the given name, the -r flag allows directories to be copied
    5. less - views the given file and allows for forward and backward navigation through the file
    6. cat - streams the given file to the terminal for viewing
    7. find - finds all of the files with the given properties, for example we could look for all files with a '.txt' extention
    8. grep - searches for lines containing a given regular expression and prints them out
    9. man - gives help for using the various commands
    10. export - updates the given environment variable
---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > ls lists information about files including directories.  ls -a lists all of the files in the current directory.  ls -l gives other information besides the name of each file, including file type, size, and timestamp.  ls -lh lists the same information as ls -l but it lists the sizes in human readable format.  The -a flag can be used with both -l and -la to give information about files that start with a '.'

---


---

What does `xargs` do? Give an example of how to use it.

> > xargs takes input from standard in and executes the echo/bin/ command over it.  One example would be find . -name "*.c" | xargs grep 'stdlib.h', the find command gets a list of all the the '.c' files and then passes it to xargs to execute the grep command and find all the lines with 'stdlib.h' in them.

---

