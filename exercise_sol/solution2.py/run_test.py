from datetime import datetime, timedelta
from time_window import TimeWindow

start = datetime(2024, 1, 1, 0, 0)
final = datetime(2024, 1, 1, 6, 0)
delta = timedelta(hours=1)

tw = TimeWindow(start, final, delta)
print(tw)
for m, ws, we in zip(tw.model_times, tw.window_starts, tw.window_ends):
    print(f"model={m}  window=({ws} -> {we})")

print("\nNow trying the bug: a negative delta...")
try:
    bad = TimeWindow(start, final, timedelta(hours=-1))
except ValueError as e:
    print(f"Caught expected error: {e}")