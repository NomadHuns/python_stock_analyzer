import yfinance as yf

# 애플(AAPL) 객체 생성
apple = yf.Ticker("AAPL")

# 1. 기업의 기본 정보 (섹터, 시가총액, PER 등)
print(apple.info)

# 2. 역사적 주가 데이터 (최근 1개월, 1일 간격)
hist = apple.history(period="1mo")
print(hist)

# 3. 배당금 및 주식 분할 정보
print(apple.actions)

# 4. 재무제표 (연간/분기)
print(apple.financials)
print(apple.quarterly_balance_sheet)
