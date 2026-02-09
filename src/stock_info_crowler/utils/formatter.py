import pandas as pd

def print_company_info_table(data_list):
    df = pd.DataFrame([s.model_dump() for s in data_list])

    # 한글 폭 자동 조절 핵심 옵션
    pd.set_option('display.unicode.east_asian_width', True)  # 한글 폭 계산
    pd.set_option('display.unicode.ambiguous_as_wide', True)  # 모호한 폭을 넓게 설정
    pd.set_option('display.max_colwidth', 30)  # 종목명 길면 생략 방지

    # 정렬 방식 지정 (to_string 내의 justify는 헤더에만 적용됨)
    print(df.to_string(index=False, justify='center'))