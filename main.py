from src.stock_info_crowler.core import StockFetcher

def main():
    analyzer = StockFetcher("AAPL")
    summary = analyzer.get_summary()
    history = analyzer.get_history()
    print(f"{summary.name}의 현재가: {summary.current_price}")
    print(f"{summary.name}의 역사: {history}")

if __name__ == "__main__":
    main()
