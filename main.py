import tkinter as tk
from ui_components import AppUI

def main():
    root = tk.Tk()
    app = AppUI(root)
    
    # In một dòng chữ test vào khung Log khi khởi động
    app.log("Ứng dụng AutoPlan (Python) đã sẵn sàng.")
    app.log("Phase 01: Setup GUI completed.")
    
    root.mainloop()

if __name__ == "__main__":
    main()
