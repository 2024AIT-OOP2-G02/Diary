from diaries.AbstractDiary import AbstractDiary

class KasugaDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。
PullとかPushとか用語が多くて、どれがどれだかわからなかった。
"""

    def get_author(self):
        return "Nagatani"