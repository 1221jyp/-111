import tkinter as tk
import math

# 초기 설정
canvas_width = 1200
canvas_height = 600
center_x = 600
center_y = 300
circle_radius = 200  # 원의 반지름
earth_radius = 10

# 별 목록 (색상, 크기, 이름, 절대등급)
star_options = [
    ('#FFFAF0', 8, '시리우스', -1.46),  # 시리우스 (푸른 흰색)
    ('#FFFFFF', 12, '베가', 0.03),       # 베가 (흰색)
    ('#FF4500', 25, '아르크투루스', -0.05), # 아르크투루스 (주황색)
    ('#B0C4DE', 50, '카노푸스', -5.53)     # 카노푸스 (푸른 흰색)
]

current_star_index = 0  # 현재 별 인덱스
sun_distance = 200  # 태양과 지구 간의 초기 거리

# Tkinter 초기화
root = tk.Tk()
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='black')
canvas.pack()

# 태양의 초기 속성
sun_color, sun_radius, sun_name, sun_absolute_magnitude = star_options[current_star_index]
sun_id = canvas.create_oval(0, 0, sun_radius * 2, sun_radius * 2, fill=sun_color)

# 거리 슬라이더와 라벨
distance_slider = tk.Scale(root, from_=70, to=500, orient='horizontal', showvalue=False)
distance_slider.set(sun_distance)
distance_slider.pack()

# 거리 라벨 추가
distance_label = tk.Label(root, text=f"거리: {sun_distance / 20:.1f} 파섹", bg='black', fg='white')
distance_label.pack()

# 별 이름과 절대등급 라벨 추가
star_info_label = tk.Label(root, text=f"{sun_name} (절대등급: {sun_absolute_magnitude})", bg='black', fg='white', font=('Arial', 14))
star_info_label.pack()

# 겉보기 등급 라벨 추가
apparent_magnitude_label = tk.Label(root, text="", bg='black', fg='white', font=('Arial', 14))
apparent_magnitude_label.pack()

# 설명 추가
discribe = tk.Label(root, text="가운데 파란 행성은 지구, 하얀색 테두리는 지구로부터 거리가 10파섹인 곳입니다.",font=('Arial', 14))
discribe.pack()

# 원 그리기 (테두리만)
def draw_circle():
    canvas.create_oval(center_x - circle_radius, center_y - circle_radius,
                       center_x + circle_radius, center_y + circle_radius,
                       outline='white', width=2)  # 테두리 색상과 두께

# 지구 그리기
def draw_earth():
    canvas.create_oval(center_x - earth_radius, center_y - earth_radius,
                       center_x + earth_radius, center_y + earth_radius,
                       fill='blue')

# 겉보기 등급 계산
def calculate_apparent_magnitude(absolute_magnitude, distance):
    d = distance / 20  # px를 파섹으로 변환
    apparent_magnitude = absolute_magnitude + 5 * (math.log10(d) - 1)
    return apparent_magnitude

# 태양 위치 업데이트
def update_sun_position(distance):
    global sun_distance
    sun_distance = float(distance)
    sun_x = center_x + sun_distance
    sun_y = center_y

    canvas.coords(sun_id, sun_x - sun_radius, sun_y - sun_radius,
                  sun_x + sun_radius, sun_y + sun_radius)

    apparent_magnitude = calculate_apparent_magnitude(sun_absolute_magnitude, sun_distance)

    distance_label.config(text=f"거리: {sun_distance / 20:.1f} 파섹")
    apparent_magnitude_label.config(text=f"겉보기 등급: {apparent_magnitude:.2f}")

# 별 변경
def change_star():
    global current_star_index, sun_color, sun_radius, sun_name, sun_absolute_magnitude
    current_star_index = (current_star_index + 1) % len(star_options)
    sun_color, sun_radius, sun_name, sun_absolute_magnitude = star_options[current_star_index]

    canvas.itemconfig(sun_id, fill=sun_color)
    canvas.coords(sun_id, 0, 0, sun_radius * 2, sun_radius * 2)

    # 거리 고정: 태양과 지구 간의 거리를 200px로 설정
    sun_distance = 200
    distance_slider.set(sun_distance)
    update_sun_position(sun_distance)  # 위치 업데이트

    star_info_label.config(text=f"{sun_name} (절대등급: {sun_absolute_magnitude})")

# 슬라이더 변경 이벤트
distance_slider.config(command=update_sun_position)

# 별 바꾸기 버튼
change_star_button = tk.Button(root, text='별 바꾸기', command=change_star)
change_star_button.pack()

# 초기 그리기
draw_circle()  # 원 그리기
draw_earth()    # 지구 그리기
update_sun_position(sun_distance)  # 태양 위치 업데이트

# Tkinter 메인 루프
root.title("Earth and Star Simulation")
root.mainloop()

