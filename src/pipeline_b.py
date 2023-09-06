from src.configs import TrainerConfig, base_step, step_b
from pydantic import BaseModel
from zenml import step, pipeline


@pipeline(enable_cache=False)
def pipeline_b(config: TrainerConfig):
    print(f"base_step parameters before run: {base_step.configuration.parameters=}")
    base_step(config)
    step_b(config)
