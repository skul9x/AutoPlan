import os

def get_markdown_files(directory):
    """
    Quét toàn bộ file trong thư mục, chỉ lọc ra các file có đuôi .md và sắp xếp theo alphabet.
    """
    if not directory or not os.path.isdir(directory):
        return []
    
    files = [f for f in os.listdir(directory) if f.endswith('.md') and os.path.isfile(os.path.join(directory, f))]
    files.sort()
    
    return files
