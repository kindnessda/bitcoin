import pyupbit

access = "7zr0IGmHWeIgtRSBaulEAagP03OrBPGJ5fVp6Ux3"          # 본인 값으로 변경
secret = "jcQhVZPu0FImFGmyVWpZyagHqR7Ye8LdxwYqYlL0"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회