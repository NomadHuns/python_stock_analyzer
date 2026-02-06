import yfinance as yf


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