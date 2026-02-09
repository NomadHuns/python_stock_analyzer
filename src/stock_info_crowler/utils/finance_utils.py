import yfinance as yf
import FinanceDataReader as fdr
from enum import Enum

def get_current_usd_krw() -> float:
    """
    현재 달러/원 환율을 가져옵니다.
    실패 시 기본값 1400.0을 반환합니다.
    """
    try:
        # yfinance를 통해 환율 티커 조회
        exchange_rate = yf.Ticker("USDKRW=X")
        # regularMarketPrice 또는 currentPrice 시도
        rate = exchange_rate.info.get('regularMarketPrice') or exchange_rate.info.get('currentPrice')

        if rate is None:
            print("Warning: 환율 정보를 가져오지 못했습니다. 기본값을 사용합니다.")
            return 1400.0

        return float(rate)
    except Exception as e:
        print(f"환율 조회 중 오류 발생: {e}")
        return 1400.0

class MarketType(str, Enum):
    KOSPI = "KOSPI"
    KOSDAQ = "KOSDAQ"
    SP500 = "S&P500"  # FDR에서 사용하는 문자열 그대로 매핑
    NASDAQ = "NASDAQ"

def get_market_symbols(market: MarketType, limit: int = 10) -> list[str]:
    """
    Enum을 사용하여 정해진 시장의 티커 리스트를 가져옵니다.
    """
    # Enum의 value 값을 FDR에 전달
    df = fdr.StockListing(market.value)

    if market == MarketType.KOSPI:
        return [f"{code}.KS" for code in df['Code'].head(limit)]
    elif market == MarketType.KOSDAQ:
        return [f"{code}.KQ" for code in df['Code'].head(limit)]
    else:
        # 미국 주식 (S&P500, NASDAQ)
        return df['Symbol'].head(limit).tolist()