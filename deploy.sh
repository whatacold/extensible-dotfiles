#!/bin/sh

cd `dirname $0`

ln -sf $PWD/astylerc ~/.astylerc
ln -sf $PWD/ackrc ~/.ackrc

# spf13-vim
ln -sf $PWD/vimrc.before.local ~/.vimrc.before.local
ln -sf $PWD/vimrc.bundles.local ~/.vimrc.bundles.local
ln -sf $PWD/vimrc.local ~/.vimrc.local

# git
ln -sf $PWD/gitconfig ~/.gitconfig

# oh-my-zsh
ln -sf $PWD/local.zsh ~/.oh-my-zsh/custom/local.zsh

# leo editor
# TODO: set body pane more wider.
ln -sf $PWD/myLeoSettings.leo ~/.leo/myLeoSettings.leo
