import sublime
import sublime_plugin


class SendSelectionToHaskell(sublime_plugin.TextCommand):
    """
    Extract the contents of the first selection, wrap in :{ and :}, and send it to ghci in Terminus.
    """
    def run(self, edit, tag=None, visible_only=False):
        selection = self.view.substr(self.view.sel()[0])
        self.view.window().run_command("terminus_send_string", {
            "string": ":{\n" + selection + "\n:}\n",
            "tag": tag,
            "visible_only": visible_only
            })
