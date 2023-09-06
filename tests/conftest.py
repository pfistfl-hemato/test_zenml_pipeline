import pytest
from pydantic import BaseModel
from src.configs import TrainerConfig, ModelConfigB, ModelConfigC


def patch_config(config: BaseModel):
    return type(config)(**config.dict())


@pytest.fixture()
def model_config_b():
    return patch_config(ModelConfigB())


@pytest.fixture()
def trainer_config_b(model_config_b):
    config = TrainerConfig(model_config=model_config_b)
    return patch_config(config)


@pytest.fixture()
def model_config_c():
    return patch_config(ModelConfigC())


@pytest.fixture()
def trainer_config_c(model_config_c):
    config = TrainerConfig(model_config=model_config_c)
    return patch_config(config)
