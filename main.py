from diaries.DiarySample import DiarySample
from diaries.k23051diary import k23051diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    k23051diary(),
]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
