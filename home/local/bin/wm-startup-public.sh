# THE COMMENT CHAR
#!/bin/sh

# Also extend /etc/profile by cat > /etc/profile.d/ibus-chs.sh
# export QT_IM_MODULE=ibus
# export XMODIFIERS="@im=ibus"
# Or ibus doesn't work with terminal and Emacs!
ibus-daemon -drx

# The notification daemon
systemctl restart --user dunst
