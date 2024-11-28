
from diaries.DiarySample import DiarySample
from diaries.PimanDiary import PimanDiary
from diaries.takaoka_diary import TakaokaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    PimanDiary(),
    TakaokaDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
