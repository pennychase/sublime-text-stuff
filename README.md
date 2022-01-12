# sublime-text-stuff

Various Sublime Text utilities (language syntax files, build systems, plugins, settings) to make Sublime more useful for what I do. A lot of this revolves around Haskell:

- Cabal syntax file based on [GitHub Linguist](https://github.com/hronro/sublime-linguist-syntax/tree/master/syntaxes)
- Haskell build file that uses [Terminus](https://packagecontrol.io/packages/Terminus) to open an interactive "cabal repl". It uses [Origami](https://github.com/SublimeText/Origami) to open up a pane whcih starts the REPL and defines file/line 
regexes to go back to errors in the source files.
