from diaries.PimanDiary import PimanDiary
from diaries.takaoka_diary import TakaokaDiary
from diaries.KasugaDiary import KasugaDiary
from diaries.MizunoDiary import MizunoDiary
from diaries.k23051diary import k23051diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    PimanDiary(),
    TakaokaDiary(),
    KasugaDiary(),
    MizunoDiary(),
    k23051diary(),
]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
