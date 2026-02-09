# Python Stock Info Crowler

이 프로젝트는 국내(KOSPI, KOSDAQ) 및 해외(NASDAQ, S&P500) 주식 시장의 데이터를 수집하고 분석하여, 목표가 대비 상승 여력이 높은 종목들을 리포트 형태로 제공하는 파이썬 기반 스톡 크롤러 및 분석 도구입니다.

## 🚀 주요 기능

- **실시간 주식 정보 수집**: `yfinance`를 활용하여 실시간 주가, 목표 주가, 통화 정보를 가져옵니다.
- **다양한 시장 지원**: `FinanceDataReader`를 통해 KOSPI, KOSDAQ, NASDAQ, S&P500 시장의 종목 리스트를 조회합니다.
- **자동 환율 적용**: 달러(USD) 기반 주식의 경우 실시간 환율을 적용하여 원화(KRW) 환산 가격을 제공합니다.
- **상승 여력 분석**: 현재가 대비 목표 주가(Target Price)의 상승 여력(Upside Potential)을 계산하고 상위 종목을 추출합니다.
- **정렬된 리포트 출력**: 분석 결과를 표 형식으로 깔끔하게 출력합니다.

## 🛠 설치 방법

이 프로젝트를 실행하기 위해 필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

### 필수 라이브러리
- `finance-datareader`: 주식 시장별 종목 리스트 수집
- `yfinance`: 상세 주가 및 재무 데이터 수집
- `pydantic`: 데이터 모델링 및 유효성 검사
- `pandas`: 데이터 가공 및 테이블 출력

## 💻 사용 방법

`main.py`를 실행하여 원하는 시장의 분석 리포트를 생성할 수 있습니다.

```bash
python main.py
```

### 코드 예시 (`main.py`)
```python
from src.stock_info_crowler.utils import MarketType

# 코스피 시장 분석 리포트 실행
run_market_report(MarketType.KOSPI)

# 나스닥 시장 분석 리포트 실행 (주석 해제 후 사용)
# run_market_report(MarketType.NASDAQ)
```

## 📂 프로젝트 구조

```text
python_stock_info_crowler/
├── main.py                 # 실행 진입점
├── requirements.txt        # 의존성 패키지 목록
└── src/
    └── stock_info_crowler/
        ├── core/           # 핵심 로직 (데이터 수집 및 분석)
        │   ├── stock_fetcher.py
        │   └── stock_analyzer.py
        ├── models/         # 데이터 모델 (Pydantic 모델)
        │   └── stock_summary.py
        └── utils/          # 유틸리티 (환율, 포맷터, 시장 타입 등)
            ├── finance_utils.py
            └── formatter.py
```

## 📝 라이선스
이 프로젝트는 교육 및 개인 분석용으로 제작되었습니다. 제공되는 데이터는 투자 권유를 목적으로 하지 않으며, 투자 결정의 책임은 본인에게 있습니다.
