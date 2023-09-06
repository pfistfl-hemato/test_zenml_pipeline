from pydantic import BaseModel, Extra
from zenml import step
from typing import List
import enum
import copy


class BaseConfig(BaseModel):
    """Base configuration class that allows arbitrary subtypes"""

    class Config:
        arbitrary_types_allowed = True
        extra = Extra.forbid

    def __getitem__(self, item):
        return getattr(self, item)


class ModelConfigs(str, enum.Enum):
    ModelConfig = "ModelConfig"
    ModelConfigB = "ModelConfigB"
    ModelConfigC = "ModelConfigC"


class ParameterConfig(BaseModel):
    param: List = []


class ModelConfig(BaseConfig):
    config_class: ModelConfigs = ModelConfigs.ModelConfig
    a_s: str = "a"


class ModelConfigB(ModelConfig):
    config_class: ModelConfigs = ModelConfigs.ModelConfigB
    b_s: str = "b"


class ModelConfigC(ModelConfig):
    config_class: ModelConfigs = ModelConfigs.ModelConfigC
    c_s: str = "c"


model_config_map = {"ModelConfigB": ModelConfigB, "ModelConfigC": ModelConfigC}


def instantiate_config(config):
    return model_config_map[config["config_class"]](**config)


class TrainerConfig(BaseConfig):
    model_config: ModelConfig

    def __init__(self, **kwargs):
        if not isinstance(kwargs["model_config"], ModelConfig):
            kwargs["model_config"] = instantiate_config(config=kwargs["model_config"])
        super().__init__(**kwargs)


@step
def base_step(config: TrainerConfig):
    model_config = config.model_config
    return model_config.dict()


@step
def step_b(config: TrainerConfig):
    model_config = config.model_config
    return model_config.dict()


@step
def step_c(config: TrainerConfig):
    model_config = config.model_config
    return model_config.dict()
