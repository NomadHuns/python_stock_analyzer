import pandas as pd
from typing import List
from pydantic import BaseModel

def print_company_info_table(data: List[BaseModel]):
    """
    Pydantic 모델 리스트를 받아 한글 깨짐 없이 표 형태로 출력합니다.
    """
    if not data:
        print("출력할 데이터가 없습니다.")
        return

    # 1. 모델 리스트를 데이터프레임으로 변환
    df = pd.DataFrame([s.model_dump() for s in data])

    # 2. 컬럼명 매핑 (영문 -> 한글)
    column_mapping = {
        'name': '종목명',
        'current_price': '현재가',
        'target_price': '목표가',
        'upside_potential': '상승여력(%)'
    }
    df = df.rename(columns=column_mapping)

    # 출력 전 정렬 (상승여력 기준 내림차순)
    if '상승여력(%)' in df.columns:
        df = df.sort_values(by='상승여력(%)', ascending=False)

    # 3. 한글 폭 맞춤 설정
    pd.set_option('display.unicode.east_asian_width', True)

    # 4. 출력용 문자열 생성 및 출력
    table_str = df.to_string(
        index=False,
        justify='center',
        float_format="%.2f",
        na_rep="N/A"  # 데이터가 없을 때 표시할 문자
    )

    print("\n" + "=" * len(table_str.split('\n')[0]))  # 구분선
    print(table_str)
    print("=" * len(table_str.split('\n')[0]) + "\n")