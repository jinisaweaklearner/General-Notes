# Bash

### shortcut in mac
```
Ctrl + A: Go to the beginning of the line you're currently typing on
Ctrl + E: Go to the end of the line you're currently typing on

Option + →: Move cursor one word forward
Option + ←: Move cursor one word backward

https://www.makeuseof.com/tag/mac-terminal-commands-cheat-sheet/
```
### shortcut in linux
```
Moving the cursor:
Ctrl + a   Go to the beginning of the line (Home)
Ctrl + e   Go to the End of the line (End)
  
Alt + b   Back (left) one word
Alt + f   Forward (right) one word
```

### debugging
```
# print the result of commands
#! /bin/bash -x

# -e = exit on error
#! /bin/bash -e
```

### sed
sed = stream editor
```
sed `s\search_partern\replace_value`

case insensitive
sed `s\search_partern\replace_value\i`

replace globally
sed `s\search_partern\replace_value\g`

replace the 2nd one
sed `s\search_partern\replace_value\2`

tutorial https://servian.udemy.com/course/bash-scripting/learn/lecture/15541904#overview
https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/
```


### exit code
- $? = exit status of a command
- 0 = success
- 1-255 = error

### Others
- $@ =  in list contexts expands to all the positional parameters as separate arguments
- exec "$@"
