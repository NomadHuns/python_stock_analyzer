import FinanceDataReader as fdr
from enum import Enum

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