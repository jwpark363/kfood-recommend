# K-Food Recommendation System
- 레시피의 재료 데이터를 형태소 분석하여 suprese를 이용하여 학습

## 이미지 분석 : pytorch CNN 계열 모델 적용
- **torchvision models의 ResNet tkdyd**
- fc 레이어 3단으로 적용
- 데이터 로드시 회전, 확대, 축소, 색깔 조정 처리

## 추천 데이터 : 한식 진흥원 레시피 데이터
- 농촌진흥청 레시피 데이터의 음식별 재료 중량을 활용
- 판다스 pivot을 이용 음식코드별 재료 중량들 벡터를 생성
- sklearn.metrics.pairwise의 consine_similarity 사용
- 생성된 similarity 벡터를 이용하여 적용할 최종 모델 클래스 작성
- 백엔드 적용을 위해 pkl 파일 생성
- 프론트 적용을 위해 코드, 메뉴명, 추천 코드 리스트 파일 생성
```python
class SimilarityModel():
    def __init__(self,data_df,feature_map) -> None:
        ## data : 농촌진흥청 한식 요리 정보 재료 DataFrame
        self.data = data_df
        ## reature_similarity_map : 유사도 정보를 이용한 최종 결과물
        self.feature_similarity_map = feature_map
    ## 음식 코드에 대한 음식명 가져오기
    ## pkl 대상 : feature_similarity_map, data
    def find_food(self,food_code):
        ## data load
        food = self.data.loc[self.data['음식_코드'] == food_code,'음식명']
        if not food.empty:
            return food.values[0]
        return None
    def find_food_and_recommend(self,food_code,top=3):
        ## feature_similarity_map
        food = self.find_food(food_code)
        recommend = []
        for code in self.feature_similarity_map[food_code]:
            food_name = self.find_food(code)
            if food_name not in recommend:
                recommend.append(self.find_food(code))
            if len(recommend) == top+1:
                break
        recommend.remove(food)
        return food, recommend
    def find_food_by_name(self,food_name):
        ## 해당 음식명이 포함된 리스트 찾기
        food_df = self.data.loc[self.data['식품명'].str.contains(food_name),['음식_코드','음식명']]
        ## 중복된 것 삭제
        food_df.drop_duplicates(inplace=True)
        ## 코드로 소팅하여 (코드,명) 형식의 리스트 리턴
        return food_df.sort_values(by='음식_코드').values.tolist()

## 프론트용 JSON 파일
"D014027": {
        "name": "육회비빔밥",
        "recommend": [
            "비빔밥(고추장, 돼지고기)", "황등비빔밥(육회비빔밥)",
            "버섯밥", "김밥(햄)", "쌀밥"
        ]
    },
"D014028": {
    "name": "전주비빔밥",
    "recommend": [
        "호두산채비빔밥", "공주장국밥",
        "이천영양밥", "표고버섯밥", "해물솥밥"
    ]
},
## 
```


## 프로젝트 상세 설명

- 기본
    - 기간
    - 인원
    - 역할
- 기술 
    - 이미지 분류
    - 추천 시스템
    - 백앤드
    - 프론트
    - 기타 : 한식 진흥원 데이터 크롤

