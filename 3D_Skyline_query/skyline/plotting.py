# plotting.py

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

# 각 레이어의 스카이라인 포인트들을 선으로 이어주는 함수
def plot_skyline(skyline, ax, color, label):
    scatter = ax.scatter(skyline[:, 0], skyline[:, 1], skyline[:, 2], c=color, marker='o', label=label)
    if len(skyline) >= 4:  # ConvexHull을 사용하기 위해 최소 4개의 점이 필요합니다.
        hull = ConvexHull(skyline)
        for simplex in hull.simplices:
            ax.plot(skyline[simplex, 0], skyline[simplex, 1], skyline[simplex, 2], color=color)
    elif len(skyline) == 3:  # 3개의 점일 경우, 삼각형으로 연결
        ax.plot(skyline[[0, 1, 2, 0], 0], skyline[[0, 1, 2, 0], 1], skyline[[0, 1, 2, 0], 2], color=color)
    elif len(skyline) == 2:  # 2개의 점일 경우, 직선으로 연결
        ax.plot(skyline[:, 0], skyline[:, 1], skyline[:, 2], color=color)
    
    return scatter  # scatter 객체 반환

def plot_skyline_with_marker(skyline, ax, color, marker, label, draw_lines=True):
    scatter = ax.scatter(skyline[:, 0], skyline[:, 1], skyline[:, 2], c=color, marker=marker, label=label)
    scatter.set_picker(True)  # Pickable로 설정
    
    # 스카이라인을 선으로 연결 (draw_lines가 True일 경우에만)
    if draw_lines and len(skyline) >= 4:
        from scipy.spatial import ConvexHull
        hull = ConvexHull(skyline)
        for simplex in hull.simplices:
            ax.plot(skyline[simplex, 0], skyline[simplex, 1], skyline[simplex, 2], color=color)