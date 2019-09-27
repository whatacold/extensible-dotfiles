# zsh customizations

source ~/.dotfilesrc

# colorscheme
eval `dircolors $V_DIRROOT/dircolors-solarized-light`

# alias
alias rsync='rsync -avz --exclude=".svn*" -e "ssh -p 36000"'
alias j='jobs'
alias flushtags='rm -f tags cscope.*; ctags -R; cscope -Rb'