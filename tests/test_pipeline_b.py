import pytest
from uuid import uuid4
from src.pipeline_b import pipeline_b
from zenml.post_execution import get_run
from zenml.enums import ExecutionStatus


def test_pipeline_b(trainer_config_b):
    run_name = f"run_b+{uuid4()}"

    pipeline = pipeline_b.with_options(
        run_name=run_name,
        unlisted=True,
    )
    pipeline(trainer_config_b)

    pipeline_run = get_run(run_name)

    assert pipeline_run.status == ExecutionStatus.COMPLETED
