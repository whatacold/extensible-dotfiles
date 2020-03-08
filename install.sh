#!/bin/bash

function apply_config()
{
    local src=$1
    local dst=$2
    local comment_prefix=$3
    local marker_begin="MY DOTFILE BEGIN DON'T EDIT DIRECTLY"
    local marker_end="MY DOTFILE END DON'T EDIT DIRECTLY"

    if [ -f "$dst" ]; then
        sed -i "/$marker_begin/,/$marker_end/d" $dst
    fi

    if [ "`tail -c 1 $dst` 2>/dev/null" == "" ]; then
        echo "${comment_prefix} $marker_begin" >> $dst
    else # not ended with a blank line
        echo -e "\n${comment_prefix} $marker_begin" >> $dst
    fi
    cat $src >> $dst
    echo -e "\n${comment_prefix} $marker_end" >> $dst
}

while read line; do
    comment_prefix=`echo $line | awk '{print $1}'`
    src_file=`echo $line | awk '{print $2}'`
    dst_file=`echo $src_file | sed "s:^home:$HOME:"`

    mkdir -p `dirname $dst_file`
    apply_config $src_file $dst_file $comment_prefix
done<<EOF
! home/.Xdefaults
" home/.vimrc.before.local
" home/.vimrc.bundles.local
" home/.vimrc.local
# home/.ackrc
# home/.agignore
# home/.astylerc
# home/.config/i3/config
# home/.config/pip/pip.conf
# home/.config/qtile/config.py
# home/.gitconfig
# home/.oh-my-zsh/custom/local.zsh
# home/.vagrant.d/Vagrantfile
# home/.screenrc
# home/.ssh/config
EOF
