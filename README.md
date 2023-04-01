# Scripts
A collection of convenience scripts i use from time to time.

## Making the scripts executable from anywhere


### Step 1: Make the scripts executable
Make sure 
```
#! /usr/bin/env python3
```
Is at the top of the script. Then use the following command for the relevant script:
```
chmod +x <script_name>
```
Keep in mind that `<script_name>` is what you will use to envoke the script, make sure its unique and doesn't collide with anything else. This is also why the files are saved without extension, so you can write `zipper <args>` instead of `zipper.py <args>`.

---

### Step 2: Make it runnable from everywhere

To do this we just have to add the directory the script are saved in to `$PATH`, which will make all scripts in that directory executable from anywhere.

Customize the following line to match the location of the scripts:

```sh
export PATH="<path-to-script-dir>:$PATH"
```

> for me this is: 
> ```
> export PATH="~/Developer/GitHub/scripts/bin:$PATH"
> ```

and paste it into a new line in one of the following files (depending on which shell you use):

> You scan wap out TextEdit with any application, `nano` will be an in-terminal editor.

#### bash
```sh
open -a TextEdit ~/.bash_profile
```

#### zsh
```sh
open -a TextEdit ~/.zshrc
```


## Installs

Start by swithing to zsh:
```sh
# simply switch from bash to zsh as default
chsh -s /bin/zsh
```
then (after restarting the terminal) install Homebrew:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Install other stuff with:
```
brew install pandoc pandoc-crossref
```
Also make sure the correct path to pandoc-templates is set in `setup/config.py`:

> for me this is: 
> ```
> pandoc_templates_path = "~/Developer/GitHub/pandoc-templates/"
> ```



### Command Prompts

For convenience i also like to customize my command prompts, so i just save them here so i don't need to recreate them from scratch.

> might want to run the following to stop annoying prompt every time terminal is opened:
> 
> ```
> touch ~/.hushlogin
> ```

#### zsh 
Add to: `~/.zshrc`
```sh
export PROMPT="%F{227}%n%F{reset}: %F{081}%2~%F{reset} => "
``` 

#### bash
Add to: `~/.bashrc`
```sh
PS1="\e[1;49;93m\u\e[0m: \e[0;49;96m\W\e[0m => "
```