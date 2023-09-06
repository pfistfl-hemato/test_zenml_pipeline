from src.configs import TrainerConfig, base_step
from pydantic import BaseModel
from zenml import step, pipeline


@pipeline(enable_cache=False)
def pipeline_b(config: TrainerConfig):
    base_step(config)
