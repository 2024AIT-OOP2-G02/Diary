from diaries.AbstractDiary import AbstractDiary

class TakaokaDiary(AbstractDiary):
  def get_date(self):
    return "2021-11-28"
  
  def get_summary(self):
    return "今日はオブジェクト指向プログラミングの講義でgithubについて学んだ。初めて触ったので知らないことが多く置いていかれる場面もあったがチームメンバーが助けてくれた。"
  
  def get_author(self):
    return "Takaoka"