from src.configs import TrainerConfig, base_step, step_c
from zenml import pipeline


@pipeline(enable_cache=False)
def pipeline_c(config: TrainerConfig):
    print(f"base_step parameters before run: {base_step.configuration.parameters=}")
    base_step(config)
    step_c(config)
