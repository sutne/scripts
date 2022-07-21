# Installs

Install everything with:
```
use-zsh.sh
install-homebrew.sh
install-git.sh
install-pandoc.sh
```
> Should be in specified order, terminal might need to be closed and reopened after some of these, and some might require `sudo`.
## Customization

### Command Prompts

For convenience i also like to customize my command prompts, so i just save them here so i don't need to recreate them from scratch.

#### zsh 
`~/.zshrc`
```sh
export PROMPT="%F{227}%n%F{reset}: %F{081}%2~%F{reset} => "
``` 

#### bash
`~/.bashrc`
```sh
PS1="\e[1;49;93m\u\e[0m: \e[0;49;96m\W\e[0m => "
``` 

> might want to run the following to stop annoying prompt every time terminal is opened:
> 
> ```
> touch ~/.hushlogin
> ```