from src.stock_info_crowler.core import StockFetcher
from src.stock_info_crowler.utils import print_company_info_table, get_current_usd_krw


def main():
    usd_krw = get_current_usd_krw()
    symbols = ["AAPL", "NVDA", "005930.KS"]

    # 2. 데이터를 가져올 때 환율 정보 전달
    results = []
    for sym in symbols:
        fetcher = StockFetcher(sym, usd_to_krw=usd_krw)
        results.append(fetcher.get_summary())

    # 유틸 함수로 출력
    print_company_info_table(results)

if __name__ == "__main__":
    main()