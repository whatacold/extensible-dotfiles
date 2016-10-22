#!/bin/sh

cd `dirname $0`

ln -sf astylerc ~/.astylerc
ln -sf ackrc ~/.ackrc

# spf13-vim
ln -sf vimrc.before.local ~/.vimrc.before.local
ln -sf vimrc.bundles.local ~/.vimrc.bundles.local
ln -sf vimrc.local ~/.vimrc.local

# git
ln -sf gitconfig ~/.gitconfig

# oh-my-zsh
ln -sf local.zsh ~/.oh-my-zsh/custom/local.zsh

# leo editor
# not work yet.
# ln -sf myLeoSettings.leo ~/.leo/myLeoSettings.leo
