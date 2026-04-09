from synapsekit import eval_case

@eval_case(min_score=0.80)
async def eval_passing():
    """Simulates a passing eval case — no API key needed."""
    return {"score": 0.92, "cost_usd": 0.001, "latency_ms": 150}

@eval_case(min_score=0.70)
async def eval_another_passing():
    return {"score": 0.85, "cost_usd": 0.002, "latency_ms": 300}
