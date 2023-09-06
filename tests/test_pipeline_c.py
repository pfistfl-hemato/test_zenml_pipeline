import pytest
from uuid import uuid4
from src.pipeline_c import pipeline_c
from zenml.post_execution import get_run
from zenml.enums import ExecutionStatus


def test_pipeline_c(trainer_config_c):
    run_name = f"run_c+{uuid4()}"

    pipeline = pipeline_c.with_options(
        run_name=run_name,
        unlisted=True,
    )
    pipeline(trainer_config_c)

    pipeline_run = get_run(run_name)

    assert pipeline_run.status == ExecutionStatus.COMPLETED
