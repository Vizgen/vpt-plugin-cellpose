from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class CellposeSegProperties:
    model: str
    model_dimensions: str
    version: str
    custom_weights: Optional[str] = None
    use_gpu: bool = False


@dataclass(frozen=True)
class CellposeSegParameters:
    nuclear_channel: str
    entity_fill_channel: str
    diameter: int
    flow_threshold: float
    mask_threshold: float
    minimum_mask_size: int
    batch_size: Optional[int] = 8  # default in Cellpose v1*
