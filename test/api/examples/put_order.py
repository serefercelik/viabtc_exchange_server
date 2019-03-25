from ViaBTCAPI.ViaBTCAPI import ViaBTCAPI

EXCHANGE_URL = "http://localhost:18080/"  # choose to your exchange url
api = ViaBTCAPI(EXCHANGE_URL)

# consts
user_id = 2
asset = "BTC"
market = "BTCBCH"
side = "SELL"

# print("\n", "see balance change history")
# print(api.balance_history(user_id=user_id, asset=asset))

# print("\n", "put order")
# print(api.order_put_limit(
#     user_id=user_id, market=market, side=side, amount=10, price=2.5,
#     taker_fee_rate=0.011, maker_fee_rate=0.011
# ))

print("\n", "market last price")
print(api.order_pending())



print("\n", "get orderbook")
print(api.order_depth(market=market, limit=10))

# print("\n", "put order")
# print(api.order_put_limit(
#     user_id=user_id, market=market, side=side, amount=1, price=2.5,
#     taker_fee_rate=0.011, maker_fee_rate=0.011
# ))
#
#
# print("\n", "first get balance")
# print(api.balance_query(user_id=user_id, asset=asset))
# #
# print("\n", "put stop loss")
# #[2, "BTCBCH", 1, "1", "5.5", "0.0001", "0.0001"]
# #[2, "BTCBCH", 1, "5.5", "1", "5.5", "0.0001", "0.0001"]
# print(api.order_put_stop_limit(
#     user_id=user_id, market=market, side=side, trigger=0.1, amount=0.1, price=2.5,
#     taker_fee_rate=0.0001, maker_fee_rate=0.0001
# ))
#
# print("\n", "last get balance")
# print(api.balance_query(user_id=user_id, asset=asset))
#
# print("\n", "see balance change history")
# print(api.balance_history(user_id=user_id, asset=asset))


# print("\n", "put stop market")
# # [2, "BTCBCH", 1, "1", "5.5", "0.0001", "0.0001"]
# print(api.order_put_stop_market(
#     user_id=user_id, market=market, side=side, trigger=0.5, amount=10,
#     taker_fee_rate=0.0001, maker_fee_rate=0.0001
# ))
