This repository contains my personal settings for some software, including:

- ack
- astyle
- i3wm
- qtile
- oh-my-zsh
- vim

# SSH

Typical SSH config snippet for `~/.ssh/config`:

    # Default settings for all hosts
    Host *
        ServerAliveInterval 10
        ServerAliveCountMax 100
        Port 1234

    # Settings for a specific host
    Host github.com
        Port 22
        User git
        IdentityFile ~/.ssh/foo_key

P.S. Generate a key pair by `ssh-keygen -t rsa -b 4096 -f /tmp/foo -C "your_email@example.com"`, where the email address is optional.
P.P.S. Copy key id to another host by `ssh-copy-id foo@1.2.3.4`, it will append a record to `~/.ssh/authorized_keys` on that host.
