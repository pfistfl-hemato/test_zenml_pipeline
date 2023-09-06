from src.configs import TrainerConfig, base_step
from zenml import pipeline


@pipeline(enable_cache=False)
def pipeline_c(config: TrainerConfig):
    base_step(config)
