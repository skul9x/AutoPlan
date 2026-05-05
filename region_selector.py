import tkinter as tk

class RegionSelector:
    def __init__(self, parent=None):
        if parent:
            self.root = tk.Toplevel(parent)
        else:
            self.root = tk.Tk()
            
        self.root.attributes('-alpha', 0.3)
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.config(cursor="cross")
        
        self.canvas = tk.Canvas(self.root, cursor="cross", bg="grey")
        self.canvas.pack(fill="both", expand=True)
        
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.selection = None

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.root.bind("<Escape>", self.on_cancel)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1, outline='red', width=2, dash=(4, 4))

    def on_move_press(self, event):
        cur_x, cur_y = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x, end_y = (event.x, event.y)
        
        # Calculate x, y, width, height
        x = min(self.start_x, end_x)
        y = min(self.start_y, end_y)
        width = abs(end_x - self.start_x)
        height = abs(end_y - self.start_y)
        
        if width > 0 and height > 0:
            self.selection = (x, y, width, height)
            self.root.destroy()
        else:
            # If just a click, ignore
            self.canvas.delete(self.rect)

    def on_cancel(self, event):
        self.selection = None
        self.root.destroy()

    def get_selection(self):
        self.root.wait_window()
        return self.selection

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() # Hide the main root
    selector = RegionSelector(root)
    region = selector.get_selection()
    if region:
        print(f"Selected Region: {region}")
    else:
        print("Selection cancelled.")
    root.destroy()
