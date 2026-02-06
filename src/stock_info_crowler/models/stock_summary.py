from pydantic import BaseModel, computed_field
from typing import Optional

class StockSummary(BaseModel):
    name: str
    current_price: Optional[float] = None
    target_price: Optional[float] = None

    @computed_field
    @property
    def upside_potential(self) -> float:
        # 현재가나 목표가가 없으면 0 반환
        if not self.target_price or not self.current_price:
            return 0.0
        # 계산 로직: ((목표가 - 현재가) / 현재가) * 100
        return round(((self.target_price - self.current_price) / self.current_price) * 100, 2)