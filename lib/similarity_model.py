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