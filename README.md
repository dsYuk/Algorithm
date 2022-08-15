# 머신러닝 (ML)

### Feature (= attribute)
  - 데이터 x의 특징, 항목을 의미
  - N: 데이터 샘플 갯수, D: 피처의 갯수
  
### Parameter (= weight)
  - 주어진 데이터 말고 모델이 가지고 있느 학습 가능한 파라미터
  - w로 표현
  
### Hyperparameter
  - 모델 학습에 있어 인간이 정해야 하는 변수들
  - 학습률, 배치 크기 등등

### 지도학습 
  * 훈련 데이터가 '입력'과 '타깃'으로 구성
  * 분류(Classification), 회귀(Regression)

### 비지도학습
  * '타깃'이 없는 훈련 데이터
  * 군집화(Clustering), 차원축소(Dimensionality reduction)
  
### 강화학습
  * 특정 환경에 최적화된 행동을 수행하고 수행에 대한 '보상'과 '현재 상태'를 받고 '최대한 많은 보상'을 위해 강화하는 학습
  
### 경사하강법
  * 함수 값이 낮아지는 방향으로 독립 변수르 변형시켜가면서 최종적을 최소값을 갖도록 하는 독립변수르 찾는 방법
  
### 선형 회귀
  - 단순 선형 회귀
     - 피처의 종류가 한 개인 데이터에 대한 회귀 모델

  - 다중 선형 회귀
     - 피처의 종류가 여러 개인 데이터에 대한 회귀 모델

  - 다항 회귀
     - 독립 변수의 차수를 높인 회귀 모델
---
# 라이브러리

* [Pandas](https://github.com/JAEHYUNYUK/Machine-Learning/blob/main/Pandas/Pandas.md)

* [sklearn](https://github.com/JAEHYUNYUK/Machine-Learning/blob/main/sklearn/sklearn.md)


---

# Deep-learning

---

## 자연어 처리

### 자연어 : 일상 생활에서 사용하는 보편적인 언어

### 자연어 처리(NLP) : 컴퓨터가 자연어를 처리하는 말

### 컴퓨터 및 컴퓨터 언어에서 자연어를 효과적으로 처리할 수 있도록 전처리 과정을 거침

### 전처리 과정 : Sentence -> Tokenization -> Cleaning, Stemming -> Encoding -> Sorting -> Padding, Similarity
  * Tokenization : 의미가 있는 단위(Token)로 나누는 작업
  * Cleaning : 데이터 사용 목적에 맞춰 노이즈 제거
  * Stemming
    * Stem : 단어의 의미를 담은 핵심
    * Affix : 단어에 추가 용법을 부여
    * Porter Algorithm : 대표적인 Stemming 방법
