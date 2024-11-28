from diaries.AbstractDiary import AbstractDiary

class KasugaDiary(AbstractDiary):
    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。
PullやPushなどGitHubの用語が多くて、全てを理解するのが難しかった。
"""

    def get_author(self):
        return "Kasuga"
