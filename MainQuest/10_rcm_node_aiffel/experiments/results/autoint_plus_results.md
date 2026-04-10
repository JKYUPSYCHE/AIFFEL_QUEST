# AutoInt+ 실험 결과 비교표

원본 CSV: `/Users/jkyu/aiffel/AIFFEL_QUEST/MainQuest/10_rcm_node_aiffel/experiments/results/autoint_plus_results_template.csv`

| 실험 | 선호 기준 | 최근성 조건 | 장르 재시청 | 데이터셋 | 학습 행 수 | 검증 행 수 | 테스트 행 수 | 학습 Positive 비율 | 검증 BCE | NDCG@10 | HitRate@10 | 상태 | 비고 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E0 | 평점 4점 이상을 선호로 간주 | 사용자 전체 이력 사용 | 장르 재시청 피처 사용 안 함 | E0_autoint_plus_dataset.csv | 720150 | 80017 | 200042 | 0.574964 | 0.54474 | 0.66221 | 0.63022 | 완료 | 가중치와 메타데이터는 /Users/jkyu/aiffel/AIFFEL_QUEST/MainQuest/10_rcm_node_aiffel/experiments/artifacts/E0에 저장했습니다. |
| E1 | 4~5점은 선호, 1~2점은 비선호, 3점은 제외 | 사용자 전체 이력 사용 | 장르 재시청 피처 사용 안 함 | E1_autoint_plus_dataset.csv | 532088 | 59121 | 147803 | 0.778187 | 0.35974 | 0.73929 | 0.68310 | 완료 | 가중치와 메타데이터는 /Users/jkyu/aiffel/AIFFEL_QUEST/MainQuest/10_rcm_node_aiffel/experiments/artifacts/E1에 저장했습니다. |
| E2 | 평점 4점 이상을 선호로 간주 | 사용자별 최근 6개월 이력만 사용 | 장르 재시청 피처 사용 안 함 | E2_autoint_plus_dataset.csv | 528599 | 58734 | 146834 | 0.576125 | 0.54856 | 0.71606 | 0.70441 | 완료 | 가중치와 메타데이터는 /Users/jkyu/aiffel/AIFFEL_QUEST/MainQuest/10_rcm_node_aiffel/experiments/artifacts/E2에 저장했습니다. |
| E3 | 평점 4점 이상을 선호로 간주 | 사용자 전체 이력 사용 | 장르 재시청 여부를 이진 피처로 추가 | E3_autoint_plus_dataset.csv | 720150 | 80017 | 200042 | 0.575318 | 0.54347 | 0.66403 | 0.63102 | 완료 | 가중치와 메타데이터는 /Users/jkyu/aiffel/AIFFEL_QUEST/MainQuest/10_rcm_node_aiffel/experiments/artifacts/E3에 저장했습니다. |
| E4 | 4~5점은 선호, 1~2점은 비선호, 3점은 제외 | 사용자별 최근 6개월 이력만 사용 | 장르 재시청 피처 사용 안 함 | E4_autoint_plus_dataset.csv | 390695 | 43411 | 108527 | 0.778042 | 0.37760 | 0.79291 | 0.75308 | 완료 | 가중치와 메타데이터는 /Users/jkyu/aiffel/AIFFEL_QUEST/MainQuest/10_rcm_node_aiffel/experiments/artifacts/E4에 저장했습니다. |
| E5 | 4~5점은 선호, 1~2점은 비선호, 3점은 제외 | 사용자 전체 이력 사용 | 장르 재시청 여부를 이진 피처로 추가 | E5_autoint_plus_dataset.csv | 532088 | 59121 | 147803 | 0.778027 | 0.36271 | 0.73782 | 0.68185 | 완료 | 가중치와 메타데이터는 /Users/jkyu/aiffel/AIFFEL_QUEST/MainQuest/10_rcm_node_aiffel/experiments/artifacts/E5에 저장했습니다. |
| E6 | 평점 4점 이상을 선호로 간주 | 사용자별 최근 6개월 이력만 사용 | 장르 재시청 여부를 이진 피처로 추가 | E6_autoint_plus_dataset.csv | 528599 | 58734 | 146834 | 0.575675 | 0.55082 | 0.71496 | 0.70405 | 완료 | 가중치와 메타데이터는 /Users/jkyu/aiffel/AIFFEL_QUEST/MainQuest/10_rcm_node_aiffel/experiments/artifacts/E6에 저장했습니다. |
| E7 | 4~5점은 선호, 1~2점은 비선호, 3점은 제외 | 사용자별 최근 6개월 이력만 사용 | 장르 재시청 여부를 이진 피처로 추가 | E7_autoint_plus_dataset.csv | 390695 | 43411 | 108527 | 0.778592 | 0.38610 | 0.79305 | 0.75297 | 완료 | 가중치와 메타데이터는 /Users/jkyu/aiffel/AIFFEL_QUEST/MainQuest/10_rcm_node_aiffel/experiments/artifacts/E7에 저장했습니다. |
| summary | 4~5점은 선호, 1~2점은 비선호, 3점은 제외 | 사용자별 최근 6개월 이력만 사용 | 장르 재시청 여부를 이진 피처로 추가 | E7_autoint_plus_dataset.csv | 390695 | 43411 | 108527 | 0.778592 | 0.38610 | 0.79305 | 0.75297 | 요약 완료 | 현재 최고 실험은 E7입니다. NDCG@10=0.79305, HitRate@10=0.75297. |
