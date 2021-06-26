This extensible-dotfiles manages dotfiles in an extensible way:
- Keep the universal part of dotfiles in the `home/` directory, and keep the directory
hierarchy same as `$HOME`

  Since different dotfiles have different comment chars, the files under `home/` should
  indicate that at the first line, for example if the comment char is `#`.

      # THE COMMENT CHAR

  or `;`:

      ; THE COMMENT CHAR

- Type `make` to install them

  It will keep the original content if target files already exist.
  The `home/` file content goes inside a block of `EXTENSIBLE-DOTFILES ...`,
  and the final dotfiles will look like:

  ```
  # EXTENSIBLE-DOTFILES BEGINS, DO NOT EDIT DIRECTLY {
  export PATH="$HOME/local/bin/:$PATH"
  
  # colorscheme
  
  # alias
  
  
  # EXTENSIBLE-DOTFILES ENDS, DO NOT EDIT DIRECTLY }
  
  export PATH="$HOME/bin:$PATH"
  ```

- Want to have local-specific config? Just edit the final dotfiles outside the `EXTENSIBLE-DOTFILES` block.

Please note that, you may also want to *version-control the final dotfiles* in another git repo,
if you have many local-specific config.
