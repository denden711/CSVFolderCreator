import os
import tkinter as tk
from tkinter import filedialog

def create_folders_for_csv_files(directory):
    # 指定されたディレクトリ内のCSVファイルを検索し、条件に応じて同名のフォルダを作成
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                # フォルダ名として使用するファイル名（拡張子なし）
                folder_name = os.path.splitext(file)[0]
                # 新しいフォルダのパス
                new_folder_path = os.path.join(root, folder_name)
                # 同名のファイルの存在をチェック
                file_exists = os.path.exists(os.path.join(root, folder_name + '.csv'))

                # 同名のフォルダが存在しない、かつ同名のファイルが存在する場合のみフォルダを作成
                if not os.path.exists(new_folder_path) and file_exists:
                    os.makedirs(new_folder_path)
                    print(f"Created folder: {new_folder_path}")
                else:
                    if os.path.exists(new_folder_path):
                        print(f"Folder already exists: {new_folder_path}")
                    if not file_exists:
                        print(f"File does not exist for folder creation: {new_folder_path}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Tkウィンドウを表示しない
    directory = filedialog.askdirectory()  # ユーザーにディレクトリを選択させる
    if directory:  # ディレクトリが選択された場合
        create_folders_for_csv_files(directory)
