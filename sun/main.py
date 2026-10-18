from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

# FastAPI 애플리케이션 생성
app = FastAPI()

# CORS 설정: 구글 앱스 스크립트 등 외부 도메인에서의 API 접근을 허용합니다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 모든 도메인 허용 (실무에서는 특정 도메인만 허용하는 것이 안전함)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 클라이언트로부터 받을 데이터 구조를 정의 (Pydantic의 BaseModel 활용)
class SearchRequest(BaseModel):
    array: list[int]  # 검색을 수행할 대상 배열
    target: int       # 찾고자 하는 값

# POST 메서드로 동작하는 선형 검색 API 엔드포인트
@app.post("/linear-search")
def linear_search(req: SearchRequest):
    steps = []
    count = 0
    found_index = -1

    # 선형 검색 알고리즘: 배열의 처음부터 끝까지 순차적으로 비교
    for i, val in enumerate(req.array):
        count += 1
        is_match = (val == req.target)
        
        # 클라이언트에서 시각화할 수 있도록 매 단계의 상태를 저장
        steps.append({
            "step": count,
            "index": i,
            "value": val,
            "match": is_match
        })
        
        # 값을 찾으면 인덱스를 저장하고 반복 종료
        if is_match:
            found_index = i
            break

    # 최종 결과 반환
    return {
        "steps": steps,
        "count": count,
        "complexity": "$O(N)$", # 선형 검색의 최악 시간 복잡도는 O(N)
        "found_index": found_index
    }

# Uvicorn을 이용해 FastAPI 서버 실행
if __name__ == "__main__":
    import uvicorn
    # Cloud Run에서 할당해 주는 PORT 환경 변수를 사용. 기본값은 8080.
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
