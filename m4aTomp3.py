'''
このコードを使うためには、いくつかの準備が必要です。以下は環境構築の手順です:

1. Pythonのインストール:まず、Pythonをインストールしてください。公式サイト（https://www.python.org/downloads/）から最新バージョンをダウンロードし、インストールしてください。

2. Pydubのインストール:次に、Pydubパッケージをインストールする必要があります。以下のコマンドを使用して、Pydubをインストールしてください。

   ```
   pip install pydub
   ```

3. ffmpegのインストール:Pydubはffmpegという外部プログラムを使用して音声ファイルの変換を行いますので、ffmpegもインストールする必要があります。

   - Windowsの場合:ffmpegのバイナリをダウンロードして、適切な場所に配置します。ダウンロードリンクはこちらです:https://ffmpeg.org/download.html#windows
   - macOSの場合:Homebrewを使用してffmpegをインストールします。ターミナルで以下のコマンドを実行します。

     ```
     brew install ffmpeg
     ```

   - Linuxの場合:ディストリビューションのパッケージマネージャーを使用してffmpegをインストールします。例えば、Ubuntuの場合は以下のコマンドを実行します。

     ```
     sudo apt-get install ffmpeg
     ```

4. 実行環境の設定:コード中の`input_path`変数には変換したいm4aファイルのパスを指定してください。`output_path`変数には変換後のmp3ファイルの出力先を指定します。

以上で環境構築が完了し、コードを実行する準備が整いました。
'''


from pydub import AudioSegment

def convert_m4a_to_mp3(input_path, output_path):
    audio = AudioSegment.from_file(input_path, format="m4a")
    audio = audio.set_frame_rate(44100).set_channels(2) 
    audio.export(output_path, format="mp3", bitrate="192k")

input_path = "" # 対象のmp4の名前を指定（このコードと同じディレクトリの方がいい）
output_path = "output.mp3" # mp3変換時の名前の決定
convert_m4a_to_mp3(input_path, output_path)
print("変換が完了しました！")



