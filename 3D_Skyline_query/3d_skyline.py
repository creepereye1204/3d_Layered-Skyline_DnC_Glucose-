import numpy as np
import matplotlib.pyplot as plt
import random
from skyline.skyline import dnc_skyline  # DNC 기능을 skyline 모듈에서 가져옴
from skyline.plotting import plot_skyline_with_marker  # 시각화 기능을 skyline 모듈에서 가져옴
from src.data_generation import generate_random_data  # 데이터 생성 함수

# 레이어를 할당하는 함수
def assign_layer(point):
    if point[0] > 125 or point[1] > 199 or point[2] > 6.4:
        return 3  # Diabetes
    elif point[0] > 99 or point[1] > 140 or point[2] > 5.7:
        return 2  # Prediabetes
    else:
        return 1  # Normal


# 메인 함수
def main():
    num_samples = 30  # 랜덤 데이터 개수 설정
    data = generate_random_data(num_samples=num_samples)  # 데이터 생성
    
    layers = np.array([assign_layer(point) for point in data])
    
    layer1 = data[layers == 1]  # Normal layer
    layer2 = data[layers == 2]  # Prediabetes layer
    layer3 = data[layers == 3]  # Diabetes layer
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # 각 레이어에 대해 DNC 알고리즘을 사용하여 스카이라인을 계산하고, 좌표 표시
    if len(layer1) > 0:
        skyline1 = dnc_skyline(layer1)
        plot_skyline_with_marker(skyline1, ax, 'green', 's', 'Normal')  # 네모
        

    if len(layer2) > 0:
        skyline2 = dnc_skyline(layer2)
        plot_skyline_with_marker(skyline2, ax, 'blue', 'o', 'Prediabetes')  # 동그라미
       

    if len(layer3) > 0:
        skyline3 = dnc_skyline(layer3)
        plot_skyline_with_marker(skyline3, ax, 'red', '^', 'Diabetes', draw_lines=False)  # 세모, 선 연결 X
        
    
    ax.set_xlabel('Fasting Glucose (mg/dL)')
    ax.set_ylabel('Postprandial Glucose (mg/dL)')
    ax.set_zlabel('HbA1c (%)')
    ax.set_xlim(70, 160)
    ax.set_ylim(0, 300)
    ax.set_zlim(0, 9.5)
    ax.set_title('Layered Skyline 3D Visualization using DNC Algorithm')
    
    ax.text2D(0.05, 0.95, f"Data: {num_samples}", transform=ax.transAxes, fontsize=12, color='black')

    plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
    
    plt.show()

if __name__ == "__main__":
    main()
