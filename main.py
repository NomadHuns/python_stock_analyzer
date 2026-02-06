from src.stock_info_crowler.core import StockFetcher
from src.stock_info_crowler.utils import print_company_info_table


def main():
    symbols = ["AAPL", "GOOGL", "NVDA", "005930.KS"]
    all_data = StockFetcher.get_multiple_summaries(symbols)

    # 유틸 함수로 출력
    print_company_info_table(all_data)

if __name__ == "__main__":
    main()