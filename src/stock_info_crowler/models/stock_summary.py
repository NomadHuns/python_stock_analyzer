from pydantic import BaseModel

class StockSummary(BaseModel):
    name: str
    current_price: float | None = None # 상장 폐지일 경우 값이 없을 수 있음
    target_price: float | None = None # Python 3.10+ 스타일