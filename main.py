from diaries.KasugaDiary import KasugaDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    KasugaDiary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
