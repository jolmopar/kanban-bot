from telegram import Bot
from telegram import Update
from kanban import KanbanBot

class TestKanbanBot(object):
    def test_start(self):
        kb = KanbanBot()
