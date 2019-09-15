;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((nil
  (eval setq compile-command
        (format "make -C %s"
                (locate-dominating-file default-directory ".git")))))

