from pydantic import BaseModel, Extra
from zenml import step
from typing import List
import enum


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


class ModelConfig(BaseConfig):
    config_class: ModelConfigs = ModelConfigs.ModelConfig
    a_s: str = "a"


class ModelConfigB(ModelConfig):
    config_class: ModelConfigs = ModelConfigs.ModelConfigB
    b_s: str = "b"
    b_l: List = ["model b"]


class ModelConfigC(ModelConfig):
    config_class: ModelConfigs = ModelConfigs.ModelConfigC
    c_s: str = "c"
    c_l: List = ["model c"]


class TrainerConfig(BaseConfig):
    a: str = "basemodel"
    model_config: ModelConfig


@step
def base_step(config: TrainerConfig):
    model_config = config.model_config
    return model_config.dict()
