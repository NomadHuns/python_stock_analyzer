import yfinance as yf

from src.stock_info_crowler.models import StockSummary

class StockFetcher:
    def __init__(self, symbol, usd_to_krw=1400.0):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)
        self.usd_to_krw = usd_to_krw  # 전달받은 환율을 저장

    # [인스턴스 메서드] 개별 종목의 상세 요약 (모델 반환)
    def get_summary(self) -> StockSummary:
        info = self.ticker.info
        currency = info.get('currency', 'USD')

        # 통화가 KRW가 아니면 저장된 환율을 사용, KRW면 1.0 적용
        rate = self.usd_to_krw if currency != 'KRW' else 1.0

        return StockSummary(
            name=info.get("longName", "Unknown"),
            current_price=info.get("currentPrice"),
            target_price=info.get("targetMeanPrice"),
            currency=currency,
            exchange_rate=rate
        )

    # [인스턴스 메서드] 개별 종목의 과거 데이터
    def get_history(self, period="5y", interval="1mo"):
        return self.ticker.history(period=period, interval=interval)

    # [정적 메서드] 여러 종목의 상세 요약 리스트
    @staticmethod
    def get_multiple_summaries(symbols: list[str], usd_to_krw: float) -> list[StockSummary]:
        results = []
        for sym in symbols:
            try:
                # 여기서도 생성자에 환율을 넘겨줘야 합니다.
                fetcher = StockFetcher(sym, usd_to_krw=usd_to_krw)
                results.append(fetcher.get_summary())
            except Exception as e:
                print(f"{sym} 오류: {e}")
        return results

    # [정적 메서드] 여러 종목의 가격 변동 비교용
    @staticmethod
    def get_combined_history(symbols: list[str], period="1y"):
        # 여러 종목의 종가(Close)를 하나의 DataFrame으로 가져옴
        data = yf.download(symbols, period=period)["Close"]
        return data