This extensible-dotfiles manages dotfiles in an extensible way:
- Keep the universal part of dotfiles in the `home/` directory, and keep the directory
hierarchy same as `$HOME`

  Since different dotfiles have different comment chars, the files under `home/` should
  indicate that at the first line, for example if the comment char is `#`.

      # THE COMMENT CHAR

- Type `make` to install them

  It will keep the original content if target files already exist.
  The `home/` file content goes inside a block of `EXTENSIBLE-DOTFILES ...`,
  and the final dotfiles will look like:

  ```markdown
  # EXTENSIBLE-DOTFILES BEGINS, DO NOT EDIT DIRECTLY {
  export PATH="$HOME/local/bin/:$PATH"
  
  # colorscheme
  
  # alias
  
  
  # EXTENSIBLE-DOTFILES ENDS, DO NOT EDIT DIRECTLY }
  
  export PATH="$HOME/bin:$PATH"
  ```

- Want to have local-specific config? Just edit the final dotfiles outside the `EXTENSIBLE-DOTFILES` block.

# SSH

Typical SSH config snippet for `~/.ssh/config`:

    # Settings for a specific host
    Host github.com
        Port 22
        User git
        IdentityFile ~/.ssh/foo_key

    # Default settings for all hosts (better be put at the end)
    Host *
        ServerAliveInterval 10
        ServerAliveCountMax 100
        IdentityFile ~/.ssh/id_rsa
        Port 1234

P.S. Generate a key pair by `ssh-keygen -t rsa -b 4096 -f /tmp/foo -C "your_email@example.com"`, where the email address is optional.

P.P.S. Copy key id to another host by `ssh-copy-id foo@1.2.3.4`, it will append a record to `~/.ssh/authorized_keys` on that host.
