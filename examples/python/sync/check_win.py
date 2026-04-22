from BinaryOptionsToolsV2.pocketoption import PocketOption


def main(ssid: str):
    api = PocketOption(ssid)

    # Method 1: buy with check_win=True
    # Rust handles the timeout internally — works for any trade duration
    print("--- Method 1: buy with check_win=True ---")
    trade_id, result = api.buy(asset="EURUSD_otc", amount=1.0, time=60, check_win=True)
    print(f"Trade ID: {trade_id}")
    print(f"Result: {result['result']} (profit: {result.get('profit')})")

    # Method 2: buy first, then call check_win separately
    print("\n--- Method 2: buy then check_win separately ---")
    (buy_id, _) = api.buy(asset="EURUSD_otc", amount=1.0, time=60, check_win=False)
    (sell_id, _) = api.sell(asset="EURUSD_otc", amount=1.0, time=60, check_win=False)
    print(f"Buy ID: {buy_id}")
    print(f"Sell ID: {sell_id}")

    buy_data = api.check_win(buy_id)
    sell_data = api.check_win(sell_id)
    print(f"Buy result: {buy_data['result']} | data: {buy_data}")
    print(f"Sell result: {sell_data['result']} | data: {sell_data}")


if __name__ == "__main__":
    ssid = input("Please enter your ssid: ")
    main(ssid)
