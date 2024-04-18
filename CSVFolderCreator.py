import os
import tkinter as tk
from tkinter import filedialog

def create_folders_for_csv_files(directory):
    # 指定されたディレクトリ内のCSVファイルを検索し、条件に応じて同名のフォルダを作成
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".csv"):
                    folder_name = os.path.splitext(file)[0]  # フォルダ名として使用するファイル名（拡張子なし）
                    new_folder_path = os.path.join(root, folder_name)  # 新しいフォルダのパス
                    if not os.path.exists(new_folder_path) and os.path.exists(os.path.join(root, file)):
                        try:
                            os.makedirs(new_folder_path)
                            print(f"Created folder: {new_folder_path}")
                        except Exception as e:
                            print(f"Failed to create folder {new_folder_path}: {e}")
                    else:
                        if os.path.exists(new_folder_path):
                            print(f"Folder already exists: {new_folder_path}")
                        else:
                            print(f"File does not exist for folder creation: {new_folder_path}")
    except Exception as e:
        print(f"Error processing directory {directory}: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Tkウィンドウを表示しない
    try:
        directory = filedialog.askdirectory()  # ユーザーにディレクトリを選択させる
        if directory:  # ディレクトリが選択された場合
            create_folders_for_csv_files(directory)
        else:
            print("No directory selected. Exiting.")
    except Exception as e:
        print(f"Error with the file dialog: {e}")
    finally:
        root.destroy()  # システムリソースを解放するために Tkinter root ウィンドウを閉じる
