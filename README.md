# sublime-text-stuff

Various Sublime Text utilities (e.g., language syntax files, build systems, plugins, settings) to make Sublime more useful for what I do. A lot of this revolves around Haskell:

- Cabal syntax file based on [GitHub Linguist](https://github.com/hronro/sublime-linguist-syntax/tree/master/syntaxes)
- Haskell build files that uses [Terminus](https://packagecontrol.io/packages/Terminus) to open an interactive "cabal repl" or "stack repl". It uses [Origami](https://github.com/SublimeText/Origami) to open up a pane which starts the REPL and defines file/line 
regexes to go back to errors in the source files.
- Plugin to send Haskell code to a running ghci in Terminus. The code is wrapped in :{ and :} so multi-line definitions are handled properly by ghci. Invoked by `cmd-alt-enter` (see key bindings on how to set this up). This plugin is based on a [Sublime Text Forum post](https://forum.sublimetext.com/t/how-to-highlight-text-and-send-to-embedded-terminus-termial/50306) by @OdatNurd.

Keymap file:

- Haskell Language Server key bindings
    + `cmd-shift-a` - LSP extend selection, a replacement for the ST "Extend Selection"
- Terminus and Build key bindings
    + alt-` - toggle Terminus pane
    + `ctl-alt-t` - open Terminus in tab
    + `cmd-alt-enter` - send to build system in Terminus
- Hoogle Search key bindings
    + `cmd-alt-shift-h` - Hoogle Search
    + `alt-shift-h` - Hoogle Search selection



