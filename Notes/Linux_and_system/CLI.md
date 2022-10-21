## check historical commands
```
history | grep 'xxx'
```

## generate SSH-key
```
# generate the ssh key
ssh-keygen -t rsa

# copy paste it to github in the clipboard
pbcopy < ~/.ssh/id_rsa.pub
```

## wildcard
```
\* : one or more  characters
?: one character
d[eo]ll match `e` or `o` 
d[e-o]ll match `e` to `o`
d[!e]ll exclude `e`
```

## last 20 commands
```
history -d 20
```

## remove
```
rm -r dictory
```

## check ip of dns
```
dig www.google.com
```
https://www.hostinger.com/tutorials/how-to-use-the-dig-command-in-linux/

## get env variables
```
env
```

## add path
The PATH is an important concept when working on the command line. It's a list of directories that tell your operating system where to look for programs, so that you can just write script instead of /home/me/bin/script or C:\Users\Me\bin\script.
https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7

## create password
```
sudo puttygen file.ppk -O private-openssh -o file.pem
openssl rsa -in file_encroption.pem -out file_decryption.pem
```

## get all variables
```bash
printenv
```
