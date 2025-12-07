import requests, time

def nova_game_whale():
    print("Arbitrum Nova — Game Whale Activated (> 500 ETH moved on gaming chain)")
    seen = set()
    while True:
        r = requests.get("https://nova.arbiscan.io/api?module=account&action=txlist"
                        "&address=0x0000000000000000000000000000000000000000&sort=desc")
        for tx in r.json().get("result", [])[:30]:
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            value = int(tx["value"]) / 1e18
            if value >= 500:  # > 500 ETH on Nova (ultra-cheap gaming chain)
                print(f"NOVA GAME WHALE JUST MOVED\n"
                      f"{value:,.1f} ETH transferred on Arbitrum Nova\n"
                      f"From: {tx['from'][:12]}...\n"
                      f"To:   {tx['to'][:12]}...\n"
                      f"Tx: https://nova.arbiscan.io/tx/{h}\n"
                      f"→ Someone is funding an entire game economy in one tx\n"
                      f"→ Nova fees ~$0.01 — this whale doesn't care about gas\n"
                      f"→ Usually studio treasury, guild vault, or exchange deposit\n"
                      f"{'-'*90}")
        time.sleep(2.5)

if __name__ == "__main__":
    nova_game_whale()
