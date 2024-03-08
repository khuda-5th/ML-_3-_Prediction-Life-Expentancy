# 💻 다변량 데이터 분석을 통한 기대수명 예측
> ML_team3 : Prediction-Life-Expectancy
<br/>

## 프로젝트 소개
<img width="784" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/e906837d-22f0-4e12-9825-1b486c61e534">
<br/>

## 팀원 구성

> ## 1. 주제 선정 배경
<img width="784" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/69056efc-217f-451c-97b3-75c83234f59c"> 

* 코로나 19 이후 건강에 대한 관심은 높아지고 있으며, 평균 기대수명은 높아지고 있는 추세이다. 허나, 시장에 나와 있는 기대수명은 대부분 국가나 지역의 평균 수명을 기반으로 하고 있다. <br/> <br/>
- 이에 따라 우리 조는 내가 얼마나 오래 살 수 있을까?에 대한 답을 평균적인 관점이 아닌, 개인 맞춤형으로 제공하여 개인의 건강에 대한 관심 및 경각심이 부각될 수 있는 효과를 도출하고자 하였다.
<br/>

> ## 2. EDA, Preprocessing
<br/>

### 원본 데이터셋
<img width="746" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/85d5b147-39f0-4e2e-9478-1638cd9129da">

- 원본 데이터셋 : Kaggle의 Life Expectancy Data <br/> <br/>
- url : https://www.kaggle.com/datasets/rachchua/life-expectancy-data
<br/>

### 히트맵, 산점도 분석 수행
<img width="742" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/9928ea31-ad20-4482-9482-c8eed22458a6">

- 처음에는 히트맵 분석 시 상관계수 0.5 미만의 feature들을 제거하려고 하였으나, 이 기준을 적용해도 될지 의문점이 생겼다. <br/>
<br/>


### 선형 회귀, 랜덤 포레스트 모델 적용
<img width="759" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/d2ad9675-5c58-4096-bc0d-466091eccf52">

- 상관계수 0.5 미만의 feature들을 제거한 나머지 feature들로 모델을 훈련시키고 score를 출력했을 때 각각 과소적합과 과대적합이 발생하여 새로운 고려 기준을 세워야 했다.
<br/>


### 최종 feature 선정
<img width="719" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/033c753d-b489-411f-9d7c-608fee4d51fb">

<img width="737" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/ba89ada1-06be-4f35-8f85-056b90c01813">

- 상관계수 0.5 미만을 제거한 후 나머지 속성, 랜덤 포레스트의 특성 중요도, 선형회귀 가중치 특성 중요도를 고려하여 최종 feature 8개를 선정하였다.

<img width="696" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/79a72887-a12d-4ec3-81c2-b037e9c096ac">
<br/>

### 데이터 전처리
<img width="663" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/0cfdcc66-49b9-4cd4-8cdb-d63767148741">

- Alcohol_consumption을 년/리터 단위 -> 한달/병 단위로 수정하여 범주화된 데이터로 사용자에게 입력을 받는 것으로 수정

<img width="756" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/eeb82f42-c2ab-499d-a598-b075ee328422">

- Null값을 포함한 행 삭제

<br/>

> ## Modeling & Architecture

<img width="746" alt="image" src="https://github.com/leeeunda/ML_team3_Prediction-Life-Expectancy/assets/132417166/6845d5ba-5491-4e99-8f3a-3b40df44ca4e">

