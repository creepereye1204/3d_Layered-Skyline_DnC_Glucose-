import numpy as np

# 데이터 생성 함수
def generate_random_data(num_samples=True):
    # 공복 혈당 (Fasting Glucose) 데이터 생성
    fasting_glucose = np.random.uniform(70, 160, num_samples)  # 70~160 mg/dL 범위

    # 식후 혈당 (Postprandial Glucose) 데이터 생성
    postprandial_glucose = np.random.uniform(0, 300, num_samples)  # 0~300 mg/dL 범위

    # HbA1c 데이터 생성
    hba1c = np.random.uniform(0, 9.5, num_samples)  # 0%~9.5% 범위

    # 데이터를 하나의 배열로 결합
    data = np.vstack((fasting_glucose, postprandial_glucose, hba1c)).T

    return data