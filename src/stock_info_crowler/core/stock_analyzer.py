from src.stock_info_crowler.core import StockFetcher
from src.stock_info_crowler.models import StockSummary
from src.stock_info_crowler.utils import MarketType, get_current_usd_krw, get_market_symbols


def get_top_upside_stocks(market: MarketType, fetch_limit: int = 20, top_n: int = 10) -> list[StockSummary]:
    """지정된 시장에서 상승 여력이 가장 높은 종목들을 분석하여 반환합니다."""
    # 1. 환율 정보 가져오기
    usd_krw = get_current_usd_krw()

    # 2. 종목 리스트 수집
    symbols = get_market_symbols(market, limit=fetch_limit)
    if not symbols:
        return []

    # 3. 데이터 수집 및 분석
    all_stocks = StockFetcher.get_multiple_summaries(symbols, usd_to_krw=usd_krw)

    # 4. 정렬 및 필터링
    return sorted(
        all_stocks,
        key=lambda x: x.upside_potential,
        reverse=True
    )[:top_n]