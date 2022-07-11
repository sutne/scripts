# Installs

Install everything with:
```
sudo innstall-all.sh
```

## Other stuff

For convenience i also like to customize my command prompts, so i just save them here so i don't need to recreate them from scratch.

##### zsh 
`~/.zshrc`
```sh
export PROMPT="%F{227}%n%F{reset}: %F{081}%2~%F{reset} => "
``` 

##### bash
`~/.bashrc`
```sh
PS1="\e[1;49;93m\u\e[0m: \e[0;49;96m\W\e[0m => "
``` 

> might want to run the following to stop annoygin prompt every time terminal is opened:
> 
> ```
> touch ~/.hushlogin
> ```