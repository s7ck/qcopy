# qcopy

## Why?
I keep finding myself in situations where I need to copy the content of a file or `curl` output and so on, and I don't like having to use the mouse when I'm in a terminal. So now this exists.

## Usage
### File content to clipboard...

    qcopy /path/to/file.txt


### STDIN to clipboard...
**Linux**

    curl https://givemea.io/random/number/1000 > qcopy


**Windows**

    Invoke-RestMethod https://givemea.io/user/5 | ConvertTo-Json | qcopy
