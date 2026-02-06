from src.stock_info_crowler.core import StockFetcher
import pandas as pd


def main():
    symbols = ["AAPL", "GOOGL", "NVDA", "005930.KS"]
    all_data = StockFetcher.get_multiple_summaries(symbols)

    # 1. Pydantic 모델 리스트를 딕셔너리 리스트로 변환하여 DataFrame 생성
    df = pd.DataFrame([s.model_dump() for s in all_data])

    # 2. 컬럼명 한글로 변경
    df.columns = ['종목명', '현재가', '목표가', '상승여력(%)']

    # 3. 출력 옵션 설정 (한글 정렬 깨짐 방지)
    pd.set_option('display.unicode.east_asian_width', True)

    # 4. to_string으로 출력
    # index=False: 왼쪽의 행 번호 제거
    # justify='center': 컬럼 헤더 정렬
    print(df.to_string(index=False, justify='center', float_format="%.2f"))


if __name__ == "__main__":
    main()