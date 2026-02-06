import yfinance as yf

from src.stock_info_crowler.models import StockSummary


class StockFetcher:
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    def get_summary(self):
        info = self.ticker.info
        # 모델 객체를 생성하여 반환
        return StockSummary(
            name=info.get("longName", "Unknown"),
            current_price=info.get("currentPrice"),
            target_price=info.get("targetMeanPrice")
        )

    def get_history(self, period="5y", interval="1mo"):
        return self.ticker.history(period=period, interval=interval)