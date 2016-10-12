#!/bin/sh

ln -sf $PWD/astylerc ~/.astylerc
ln -sf $PWD/ackrc ~/.ackrc

# spf13-vim
ln -sf $PWD/vimrc.before.local ~/.vimrc.before.local
ln -sf $PWD/vimrc.bundles.local ~/.vimrc.bundles.local
ln -sf $PWD/vimrc.local ~/.vimrc.local

# git
ln -sf $PWD/gitconfig ~/.gitconfig
