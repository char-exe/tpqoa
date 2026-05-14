"""
Quick smoke-test for tpqoa.
Run after filling in oanda.cfg:
    python test_connection.py
"""
import tpqoa

CFG = 'oanda.cfg'

oanda = tpqoa.tpqoa(CFG)

# 1. Account summary
print("=== Account Summary ===")
summary = oanda.get_account_summary()
print(f"  ID      : {summary['id']}")
print(f"  Balance : {summary['balance']} {summary['currency']}")

# 2. Instruments (first 5)
print("\n=== First 5 Instruments ===")
instruments = oanda.get_instruments()
for disp, name in instruments[:5]:
    print(f"  {disp:25s}  {name}")

# 3. Recent transactions
print("\n=== Transactions ===")
try:
    transactions = oanda.get_transactions(tid=0)
    print(f"  Retrieved {len(transactions)} transaction(s).")
    if transactions:
        first = transactions[0]
        last = transactions[-1]
        print(f"  First : id={first.get('id')}  type={first.get('type')}  time={first.get('time','')[:19]}")
        print(f"  Latest: id={last.get('id')}   type={last.get('type')}  time={last.get('time','')[:19]}")
except Exception as e:
    print(f"  ERROR: {e}")

print("\nAll tests done.")


