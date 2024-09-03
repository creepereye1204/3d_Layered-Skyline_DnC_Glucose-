import numpy as np

# 지배 관계를 확인하는 함수
def dominates(point1, point2):
    """ point1이 point2를 지배하는지 여부를 판단 """
    return all(x <= y for x, y in zip(point1, point2)) and any(x < y for x, y in zip(point1, point2))

# DNC 스카이라인 계산을 위한 병합 함수
def merge_skyline(left_skyline, right_skyline):
    merged_skyline = []

    # 두 스카이라인을 병합하면서 지배 관계를 판단
    for point in left_skyline:
        if not any(dominates(other, point) for other in right_skyline):
            merged_skyline.append(point)

    for point in right_skyline:
        if not any(dominates(other, point) for other in left_skyline):
            merged_skyline.append(point)

    # 중복 제거 및 최종 스카이라인 포인트 계산
    final_skyline = []
    for point in merged_skyline:
        if not any(dominates(other, point) for other in final_skyline):
            final_skyline.append(point)
    
    return np.array(final_skyline)

# DNC 스카이라인 계산 함수
def dnc_skyline(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left_skyline = dnc_skyline(data[:mid])
    right_skyline = dnc_skyline(data[mid:])
    return merge_skyline(left_skyline, right_skyline)
