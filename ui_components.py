import tkinter as tk
import os

from tkinter import ttk, filedialog, scrolledtext
import file_manager
import settings_manager
from engine import AutomationEngine
from hotkey import HotkeyHandler
from region_selector import RegionSelector


class AppUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoPlan Runner - Python Edition")
        self.root.geometry("650x650")
        self.root.configure(bg="#f0f0f0")
        
        # Engine setup
        self.engine = AutomationEngine(self.safe_log, self.on_engine_finished)
        
        # Hotkey setup
        self.hotkey = HotkeyHandler(self.on_stop)
        self.hotkey.start()

        # Region state
        self.scan_region = None
        
        # Alarm state
        self.alarm_enabled = tk.BooleanVar(value=False)
        
        # Main Container
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Folder selection
        self.create_path_selector(
            "MD Files Folder:", 
            "folder_path", 
            self.browse_folder, 
            0
        )
        
        # Icon selection
        self.create_path_selector(
            "Icon Image (➡️):", 
            "icon_path", 
            self.browse_file, 
            1
        )
        
        # File Selection Listbox
        ttk.Label(self.main_frame, text="Select Files to Execute:").grid(row=2, column=0, sticky=tk.W, pady=(10, 0))
        
        list_frame = ttk.Frame(self.main_frame)
        list_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.file_listbox = tk.Listbox(
            list_frame, 
            selectmode=tk.EXTENDED, 
            height=6,
            exportselection=False
        )
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.file_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=scrollbar.set)
        
        # List Buttons Frame
        list_btn_frame = ttk.Frame(self.main_frame)
        list_btn_frame.grid(row=3, column=2, sticky=tk.N, padx=5, pady=5)
        
        ttk.Button(list_btn_frame, text="Select All", command=self.select_all).pack(fill=tk.X, pady=2)
        ttk.Button(list_btn_frame, text="Deselect All", command=self.deselect_all).pack(fill=tk.X, pady=2)
        
        # Region Selection
        region_frame = ttk.LabelFrame(self.main_frame, text="Scan Region Management", padding=10)
        region_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        self.region_label = ttk.Label(region_frame, text="Current Region: Full Screen (Default)")
        self.region_label.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(region_frame, text="Select Scan Area", command=self.on_select_region).pack(side=tk.LEFT, padx=5)
        ttk.Button(region_frame, text="Reset", command=self.on_reset_region).pack(side=tk.LEFT, padx=5)
        
        # Alarm Settings
        alarm_frame = ttk.LabelFrame(self.main_frame, text="Alarm Settings (Completion)", padding=10)
        alarm_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Checkbutton(
            alarm_frame, 
            text="Enable Alarm on Finish", 
            variable=self.alarm_enabled,
            command=self.save_current_settings
        ).grid(row=0, column=0, sticky=tk.W, padx=5)
        
        ttk.Label(alarm_frame, text="MP3 File:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        
        self.alarm_path_entry = ttk.Entry(alarm_frame, width=40)
        self.alarm_path_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5)
        
        ttk.Button(alarm_frame, text="Browse MP3", command=self.browse_mp3).grid(row=1, column=2, padx=5)

        # Control Buttons
        self.btn_frame = ttk.Frame(self.main_frame)
        self.btn_frame.grid(row=6, column=0, columnspan=3, pady=10)
        
        self.start_btn = ttk.Button(
            self.btn_frame, 
            text="▶️ START AUTO", 
            command=self.on_start
        )
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_btn = ttk.Button(
            self.btn_frame, 
            text="⏹️ STOP", 
            command=self.on_stop,
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=10)
        
        # Log Area
        ttk.Label(self.main_frame, text="Log Output:").grid(row=7, column=0, sticky=tk.W)
        self.log_area = scrolledtext.ScrolledText(
            self.main_frame, 
            height=8, 
            wrap=tk.WORD,
            bg="black",
            fg="#00ff00", # Matrix green
            font=("Consolas", 10)
        )
        self.log_area.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        self.log_area.tag_config("error", foreground="red")
        self.main_frame.rowconfigure(8, weight=1)
        self.main_frame.columnconfigure(1, weight=1)

        # Load and Apply Settings
        self.load_and_apply_settings()

    def load_and_apply_settings(self):
        """Loads settings from manager and populates UI."""
        config_path = settings_manager.get_config_file_path()
        self.log(f"Loading configuration from: {config_path}")
        
        settings = settings_manager.load_settings()
        
        # 1. MD Folder
        md_folder = self.validate_path(settings.get("mru_md_folder", ""))
        if md_folder:
            self.folder_path.delete(0, tk.END)
            self.folder_path.insert(0, md_folder)
            self.update_file_list(md_folder)
            
        # 2. Icon Path
        icon_path = self.validate_path(settings.get("mru_icon_link", ""))
        if icon_path:
            self.icon_path.delete(0, tk.END)
            self.icon_path.insert(0, icon_path)
            
        # 3. Scan Region
        region = settings.get("scan_region")
        if region and isinstance(region, (list, tuple)) and len(region) == 4:
            self.scan_region = tuple(region)
            self.region_label.config(text=f"Current Region: {self.scan_region}")

        # 4. Alarm Settings
        self.alarm_enabled.set(settings.get("alarm_enabled", False))
        alarm_mp3 = self.validate_path(settings.get("alarm_mp3_path", ""))
        if alarm_mp3:
            self.alarm_path_entry.delete(0, tk.END)
            self.alarm_path_entry.insert(0, alarm_mp3)

    def validate_path(self, path):
        """Returns the path if valid on current OS, else empty string."""
        if not path:
            return ""
        
        # Convert path to current OS style for better check (though exists() handles it mostly)
        normalized_path = os.path.normpath(path)
        
        if os.path.exists(normalized_path):
            return normalized_path
        
        return ""

    def save_current_settings(self):
        """Gather current state and persist to storage."""
        data = {
            "mru_md_folder": self.folder_path.get(),
            "mru_icon_link": self.icon_path.get(),
            "scan_region": self.scan_region,
            "alarm_enabled": self.alarm_enabled.get(),
            "alarm_mp3_path": self.alarm_path_entry.get()
        }
        try:
            settings_manager.save_settings(data)
        except Exception as e:
            self.log(f"ERROR saving settings: {e}")

    def create_path_selector(self, label_text, attr_name, browse_cmd, row):
        ttk.Label(self.main_frame, text=label_text).grid(row=row, column=0, sticky=tk.W, pady=5)
        
        entry = ttk.Entry(self.main_frame, width=50)
        entry.grid(row=row, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        setattr(self, attr_name, entry)
        
        browse_btn = ttk.Button(self.main_frame, text="Browse", command=browse_cmd)
        browse_btn.grid(row=row, column=2, padx=5, pady=5)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.delete(0, tk.END)
            self.folder_path.insert(0, folder)
            self.log(f"Selected folder: {folder}")
            self.update_file_list(folder)
            self.save_current_settings()

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp"), ("All files", "*.*")]
        )
        if file_path:
            self.icon_path.delete(0, tk.END)
            self.icon_path.insert(0, file_path)
            self.log(f"Selected icon: {file_path}")
            self.save_current_settings()

    def browse_mp3(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")]
        )
        if file_path:
            self.alarm_path_entry.delete(0, tk.END)
            self.alarm_path_entry.insert(0, file_path)
            self.log(f"Selected alarm MP3: {file_path}")
            self.save_current_settings()

    def update_file_list(self, folder):
        """Cập nhật danh sách file trong Listbox."""
        self.file_listbox.delete(0, tk.END)
        md_files = file_manager.get_markdown_files(folder)
        for f in md_files:
            self.file_listbox.insert(tk.END, f)
        
        # Mặc định chọn tất cả
        self.select_all()

    def select_all(self):
        """Chọn tất cả item trong listbox."""
        self.file_listbox.select_set(0, tk.END)

    def deselect_all(self):
        """Bỏ chọn tất cả item trong listbox."""
        self.file_listbox.selection_clear(0, tk.END)

    def on_select_region(self):
        """Mở công cụ chọn vùng quét."""
        self.log("Opening Region Selector... Press ESC to cancel.")
        selector = RegionSelector(self.root)
        region = selector.get_selection()
        if region:
            self.scan_region = region
            self.region_label.config(text=f"Current Region: {region}")
            self.log(f"Region set to: {region}")
            self.save_current_settings()
        else:
            self.log("Region selection cancelled.")

    def on_reset_region(self):
        """Reset về chế độ toàn màn hình."""
        self.scan_region = None
        self.region_label.config(text="Current Region: Full Screen (Default)")
        self.log("Region reset to Full Screen.")
        self.save_current_settings()

    def log(self, message):
        tag = None
        if "ERROR:" in message:
            tag = "error"
        
        self.log_area.insert(tk.END, f"> {message}\n", tag)
        self.log_area.see(tk.END)

    def safe_log(self, message):
        """Cập nhật log an toàn từ luồng phụ."""
        self.root.after(0, self.log, message)

    def on_engine_finished(self):
        """Callback khi engine kết thúc."""
        self.root.after(0, self._reset_ui_state)

    def _reset_ui_state(self):
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

    def on_start(self):
        folder = self.folder_path.get()
        icon = self.icon_path.get()

        if not folder:
            self.log("Lỗi: Vui lòng chọn thư mục chứa file .md")
            return
        
        if not icon or not os.path.exists(icon):
            self.log("Lỗi: Vui lòng chọn file ảnh icon hợp lệ.")
            return

        # 1. Lấy danh sách các file được chọn từ Listbox
        selected_indices = self.file_listbox.curselection()
        
        # 2. Kiểm tra nếu chưa chọn file nào thì báo lỗi
        if not selected_indices:
            self.log("Lỗi: Vui lòng chọn ít nhất một file từ danh sách để bắt đầu.")
            return

        # 3. Map index về tên file thực tế
        selected_files = [self.file_listbox.get(i) for i in selected_indices]

        self.log("Starting Auto Bot...")
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
            
        self.log(f"Đã chọn {len(selected_files)} file kế hoạch. Bắt đầu chạy...")
        
        # 4. Truyền danh sách file đã chọn và vùng quét vào engine.start
        self.engine.start(folder, selected_files, icon, region=self.scan_region)

    def on_stop(self):
        self.engine.stop()
        self.root.after(0, self._reset_ui_state)

