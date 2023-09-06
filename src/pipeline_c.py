from src.configs import TrainerConfig, base_step, step_c
from zenml import pipeline


@pipeline(enable_cache=False)
def pipeline_c(config: TrainerConfig):
    base_step(config)
    step_c(config)
