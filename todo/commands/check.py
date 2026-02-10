from __future__ import absolute_import

from todo.commands.toggle import ToggleCommand


class CheckCommand(ToggleCommand):
    def check_by_item(self, item):
        """Returns a checked copy of the item"""
        item_toggled = item.copy()
        item_toggled['done'] = True
        return item_toggled


Check = CheckCommand()
