import yfinance as yf

from src.stock_info_crowler.models import StockSummary


class StockFetcher:
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    # [인스턴스 메서드] 개별 종목의 상세 요약 (모델 반환)
    def get_summary(self):
        info = self.ticker.info
        # 모델 객체를 생성하여 반환
        return StockSummary(
            name=info.get("longName", "Unknown"),
            current_price=info.get("currentPrice"),
            target_price=info.get("targetMeanPrice")
        )

    # [인스턴스 메서드] 개별 종목의 과거 데이터
    def get_history(self, period="5y", interval="1mo"):
        return self.ticker.history(period=period, interval=interval)

    # [정적 메서드] 여러 종목의 상세 요약 리스트
    @staticmethod
    def get_multiple_summaries(symbols: list[str]) -> list[StockSummary]:
        """여러 종목 코드를 받아 StockSummary 리스트를 반환"""
        results = []
        for sym in symbols:
            try:
                fetcher = StockFetcher(sym)
                results.append(fetcher.get_summary())
            except Exception as e:
                print(f"{sym} 데이터를 가져오는 중 오류 발생: {e}")
        return results

    # [정적 메서드] 여러 종목의 가격 변동 비교용
    @staticmethod
    def get_combined_history(symbols: list[str], period="1y"):
        # 여러 종목의 종가(Close)를 하나의 DataFrame으로 가져옴
        data = yf.download(symbols, period=period)["Close"]
        return data