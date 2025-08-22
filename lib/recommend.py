from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
"""
    유사도 벡터 생성
    documents : 생성을 위한 np array
    vector_type : 0 - CountVectorizer, 1 - TfidfVectorizer
"""
def make_similarity_vector(documents:list[object], vector_type=0):
    base_params = {
        'max_features':1000,    # 최대 특성 수
        'min_df':2,             # 최소 문서 빈도
        'max_df':0.8,           # 최대 문서 빈도 비율
        'ngram_range':(1, 4)    # n-gram 범위 (1-gram, 2-gram)
    }
    vectorizer = CountVectorizer(
        **base_params,
        lowercase=True,        # 소문자 변환
    ) if vector_type == 0 else TfidfVectorizer(
        **base_params,
        sublinear_tf=True,
        smooth_idf=True,         # IDF 스무딩
        norm='l2',               # 정규화 방법 ('l1', 'l2', None)
        use_idf=True             # IDF 사용 여부
    )
    vector_ = vectorizer.fit_transform(documents)
    features = vectorizer.get_feature_names_out()
    vector = vector_.toarray()
    return cosine_similarity(vector,vector),features