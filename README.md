# CSVFolderCreator
 

CSVFolderCreatorは、指定されたディレクトリ内のすべてのCSVファイルに基づいてフォルダを自動的に作成するPythonプログラムです。これにより、ファイルの整理と管理が容易になります。

#### 機能
- ユーザーが選択したディレクトリ内の全てのCSVファイルを検索します。
- 各CSVファイルの名前に基づいて、同名の新しいフォルダをそのファイルのある場所に作成します。
- 既に同名のフォルダが存在する場合は、新たにフォルダを作成しません。
- 対象フォルダが存在しないがファイルも存在しない場合は、フォルダの作成をスキップします。

#### システム要件
- Python 3.x
- tkinterライブラリ（GUI要素用）

#### インストール方法
1. Pythonをインストールします（既にインストールされている場合はこのステップをスキップしてください）。
2. 必要なライブラリが未インストールの場合、次のコマンドを使用してインストールできます。
   ```
   pip install tk
   ```

#### 使用方法
1. プログラムを起動します。
2. GUIがポップアップし、「ディレクトリ選択」ダイアログが表示されます。
3. CSVファイルが含まれているディレクトリを選択します。
4. プログラムが自動的にディレクトリ内の全てのCSVファイルに対応するフォルダを作成します。

#### メンテナンスとサポート
プログラムに関する問題や改善提案がある場合は、GitHubのイシュートラッカーに報告してください。

#### ライセンス
このプログラムはMITライセンスの下で公開されています。使用、改変、再配布が自由に行えますが、すべての原著作者のクレジットとMITライセンスのコピーを表示する必要があります。

このREADMEは、ユーザーがCSVファイルの管理と整理を容易に行えるようにするための簡潔なガイドとして機能します。
