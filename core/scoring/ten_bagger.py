# core/scoring/ten_bagger.py

import yaml


def load_weights(path: str = "config/rules.yaml") -> dict:
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)
    return cfg.get("weights", {})


def calculate_ten_bagger_score(
    price_position: float,
    volume_ratio: float,
    historical_spike: bool,
    weights: dict
) -> float:
    """
    Calculate total ten-bagger score from features.
    """

    price_score = max(0.0, 10.0 - price_position)
    volume_score = min(5.0, volume_ratio)
    spike_score = 3.0 if historical_spike else 0.0

    total = (
        weights.get("price", 1.0) * price_score +
        weights.get("volume", 1.0) * volume_score +
        weights.get("spike", 1.0) * spike_score
    )

    return float(total)
