# 모델 불러오는 코드
model = xgb.Booster()
model.load_model('/content/xgb_model.model')

# 사용자 입력 받는 함수
def get_user_input():
  user_input = {}

  user_input['나라'] = input('나라를 입력하세요: ')
  user_input['성별'] = input('성별을 입력하세요.(남자/여자): ')
  user_input['키'] = float(input('키(cm)를 입력하세요: '))
  user_input['체중'] = float(input('체중(kg) 을 입력하세요: '))
  user_input['흡연 여부'] = input('흡연 여부를 입력하세요(Y/N): ')
  user_input['음주량'] = float(input('음주량을 입력하세요 1~5 수준으로 입력해주세요.(1병 이하: 1, 1병~2병: 2, 2병~3병: 3, 3병~4병: 4, 5병 이상: 5): '))
  user_input['수면량'] = input('평균적으로 7시간 이상 주무시나요?(Y/N): ')

  # 사용자가 '한국' 또는 '대한민국'을 입력했을 때 추가적인 정보를 제공
  if user_input['나라'] in ['한국', '대한민국']:
      user_input['Incidents_HIV'] = 0.01
      user_input['Alcohol_consumption'] = user_input['음주량']
      user_input['Polio'] = 97.4
      user_input['Diphtheria'] = 95.9
      user_input['Economy_status'] = 1
      if['성별'] == '남자':
        user_input['Adult_mortality'] = 57.02
      else:
        user_input['Adult_mortality'] = 22.07
      user_input['BMI'] = user_input['체중'] / (user_input['키']*0.01)**2
  user_df = pd.DataFrame([user_input])
  

  return user_df

# 사용자 입력을 모델에 넣어 예측값을 계산하고 출력하는 코드
def predict_lifespan(model, user_input):
  user_input_processed = xgb.DMatrix(user_input.drop(['나라', '성별', '키', '체중', '흡연 여부', '음주량', '수면량'], axis=1))

  predicted_lifespan = model.predict(user_input_processed)
  print('예상 수명: ', predicted_lifespan[0])
  return predicted_lifespan

# 사용자 입력 받기
user_input = get_user_input()

# 예측값 계산 및 출력
predicted_lifespan = predict_lifespan(model, user_input)

# 수면량에 따른 기대수명 조정
if user_input['수면량'][0] == 'N' or user_input['수면량'][0] == 'n':
  if user_input['성별'][0] == '남자':
      predicted_lifespan -= 4.7
  else:
      predicted_lifespan -= 2.5

# 흡연 여부에 따른 기대수명 조정
if user_input['흡연 여부'][0] == 'Y' or user_input['흡연 여부'][0] == 'y':
  if user_input['성별'][0] == '남자':
      predicted_lifespan -= 3.73
  else:
      predicted_lifespan -= 1
    
print('조정된 예상 수명: ', predicted_lifespan[0])
