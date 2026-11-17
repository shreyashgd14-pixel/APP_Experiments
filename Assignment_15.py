import gc

print("Thresholds:", gc.get_threshold())

def create_cycle():
    x = {}
    x[1] = x

for _ in range(10):
    create_cycle()

collected = gc.collect()
print(f"Collected {collected} objects.")

gc.disable()
obj = [1, 2, 3]
del obj
gc.enable()

gc.set_threshold(500, 5, 5)
print("New thresholds:", gc.get_threshold())
