import tkinter as tk
import math
from decimal import Decimal

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("별의 절대등급 계산기")

        # 프레임 생성
        self.frame1 = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)

        # 첫 번째 페이지 UI
        self.label1_1 = tk.Label(self.frame1, text="표면온도(K)를 입력하세요")
        self.label1_2 = tk.Label(self.frame1, text="별의 반지름을 입력하세요(M)")
        self.label1_3 = tk.Label(self.frame1, text="별과의 거리를 입력하세요(파섹)")
        self.entry1 = tk.Entry(self.frame1)
        self.entry2 = tk.Entry(self.frame1)
        self.entry3 = tk.Entry(self.frame1)
        self.label2_1 = tk.Label(self.frame1, text="단위 시간에 단위 면적당 방출하는 에너지 양(W/m²) :")
        self.label2_2 = tk.Label(self.frame1, text="별의 광도(W) :")
        self.label2_3 = tk.Label(self.frame1, text="별의 등급 :")
        self.label3_1 = tk.Label(self.frame1, text="")
        self.label3_2 = tk.Label(self.frame1, text="")
        self.label3_3 = tk.Label(self.frame1, text="")
        self.button1 = tk.Button(self.frame1, text="계산", command=self.calculate)
        self.button2 = tk.Button(self.frame1, text="다음 페이지", command=self.show_frame2)

        # 그리드 배치
        self.label1_1.grid(column=1, row=0)
        self.entry1.grid(column=3, row=0)
        self.label1_2.grid(column=1, row=1)
        self.entry2.grid(column=3, row=1)
        self.label1_3.grid(column=1, row=2)
        self.entry3.grid(column=3, row=2)
        self.button1.grid(column=2, row=3)
        self.button2.grid(column=2, row=4)

        # 결과 레이블 그리드 추가
        self.label2_1.grid(column=1, row=5)
        self.label3_1.grid(column=3, row=5)
        self.label2_2.grid(column=1, row=6)
        self.label3_2.grid(column=3, row=6)
        self.label2_3.grid(column=1, row=7)
        self.label3_3.grid(column=3, row=7)

        # 두 번째 페이지 UI
        self.label2 = tk.Label(self.frame2, text="두 번째 페이지입니다.")
        self.button_back = tk.Button(self.frame2, text="첫 번째 페이지로 돌아가기", command=self.show_frame1)

        self.label2.grid(column=1, row=0)
        self.button_back.grid(column=1, row=1)

        # 프레임을 초기화
        self.frame1.pack()

    def show_frame1(self):
        self.frame2.pack_forget()
        self.frame1.pack()

    def show_frame2(self):
        self.frame1.pack_forget()
        self.frame2.pack()

    def calculate(self):
        data1 = float(self.entry1.get())  # 표면온도
        data2 = float(self.entry2.get())  # 별의 반지름
        data3 = float(self.entry3.get())  # 거리 (파섹)

        # 단위 면적당 방출하는 에너지 양 계산
        result1 = (data1 ** 4) * 5.67 / 100000000  # W/m²
        # 별의 광도 계산
        result2 = result1 * 9.87 * 4 * (data2 ** 2)  # W

        # 겉보기 등급 계산
        L_sun = 3.828 * 10**26  # 태양의 광도 W
        m = -2.5 * math.log10(result2 / L_sun) + 4.83  # 겉보기 등급

        # 절대등급 계산
        M = m - 5 * math.log10(data3 / 10)  # 절대등급

        result1 = Decimal(result1)
        result2 = Decimal(result2)
        M = Decimal(M)

        # 레이블에 결과 출력
        self.label3_1.config(text=f"{result1:.0f} W/m²")  # 단위 추가
        self.label3_2.config(text=f"{result2:.0f} W")      # 단위 추가
        self.label3_3.config(text=f"{M:.2f}")              # 절대등급

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
