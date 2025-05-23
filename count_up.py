import tkinter
import datetime
import threading

root = tkinter.Tk()
root.title('Countup Timer')
root.geometry('1922x1082')
root.attributes('-fullscreen', True)

# アプリ起動時点の時刻を保存する変数（初期値はNone）
start_time = None
stop_event = threading.Event()

def countup():
    global start_time

    # アプリ起動時点の時刻を取得
    start_time = datetime.datetime.now()

    while not stop_event.is_set():
        # 現在時刻を取得
        now = datetime.datetime.now()
        # 差分を計算（timedeltaオブジェクト）
        diff = now - start_time

        # timedeltaから「経過した秒」を取り出す
        total_seconds = int(diff.total_seconds())

        # 時、分、秒に分割
        hours = total_seconds // 3600
        remainder = total_seconds % 3600
        minutes = remainder // 60
        seconds = remainder % 60

        # フォーマット（時:分:秒）
        cd = f"{hours:02}:{minutes:02}:{seconds:02}"

        # テキスト要素を更新
        canvas.itemconfig(timer_text, text=cd)

        # 1秒待機
        stop_event.wait(1)

def start_timer():
    global start_time
    if start_time is None:  # カウントアップがまだ始まっていない場合のみ実行
        # スタートボタンを非表示にする
        start_button.place_forget()

        # スレッドを作成し、countup関数を実行
        thread = threading.Thread(target=countup, daemon=True)
        thread.start()

# キャンバスを作成し配置
canvas = tkinter.Canvas(root, width=1922, height=1082, background='black',highlightthickness=0)
canvas.pack()

# 初期テキストを配置
# テキスト要素を生成しIDを保持
# これを使ってテキストを更新する

timer_text = canvas.create_text(960, 520, text="00:00:00", font=('Arial Black', 300), fill='white')

# スタートボタンを作成し配置
start_button = tkinter.Button(root, text="Start", font=('Arial Black', 50), command=start_timer)
start_button.place(x=810, y=800)

# ESCキーでアプリを終了する機能を追加
def exit_app(event):
    root.destroy()

root.bind("<Escape>", exit_app)

# メインループ開始
root.mainloop()
