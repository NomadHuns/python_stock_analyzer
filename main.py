from src.stock_info_crowler.core import get_top_upside_stocks
from src.stock_info_crowler.utils import print_company_info_table, get_current_usd_krw, get_market_symbols, MarketType


def run_market_report(market: MarketType):
    """시장 분석 리포트를 실행하고 화면에 출력합니다."""
    header = f"[{market.value} 시장 분석 리포트]"
    print(f"\n{header:=^60}")  # 등호(=)로 채운 중앙 정렬 헤더

    try:
        # 데이터 엔진 호출 (위에서 만든 함수)
        top_stocks = get_top_upside_stocks(market, fetch_limit=20, top_n=10)

        if not top_stocks:
            print("❌ 분석할 수 있는 데이터가 없습니다.")
            return

        # 결과 출력 (유틸 함수)
        print_company_info_table(top_stocks)
        print(f"{'=' * 60}\n")

    except Exception as e:
        print(f"⚠️ 리포트 생성 중 오류 발생: {e}")

def main():
    # 원하는 시장을 선택해서 리포트 실행
    # 예: 코스피 분석
    run_market_report(MarketType.KOSPI)

    # 예: 나스닥 분석
    # run_market_report(MarketType.NASDAQ)

if __name__ == "__main__":
    main()