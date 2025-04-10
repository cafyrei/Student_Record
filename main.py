import customtkinter
from assets.pages.window_conf import Window
import tracemalloc

# Start memory tracking
tracemalloc.start()

window = Window()

# Track memory after window is closed
def on_closing():
    current, peak = tracemalloc.get_traced_memory()
    print(f"📈 Current memory usage: {current / 10**6:.6f} MB")
    print(f"🚀 Peak memory usage: {peak / 10**6:.6f} MB")
    tracemalloc.stop()
    window.destroy()

# window = Window()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()      