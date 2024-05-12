from datetime import datetime, timezone
from dataclasses import dataclass
from typing import TypeAlias

Matrix: TypeAlias = list[list[int | float]]
type Matriz = list[list[int | float]]

@dataclass
class CoinTrans:
	_id: str
	simbolo: str
	exchange: float
	amount: float
	success: bool
	trace: list


def main():
	transfer = CoinTrans(
		'MX-US-0001234',
		'mxn',
		16.25,
		10_000.00,
		True,
		[datetime.now(timezone.utc)])
	print(transfer)


if __name__ == '__main__':
	main()
