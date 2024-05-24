from kedro.pipeline import Pipeline
from data_insights.pipelines import data_processing as dp
from typing import Dict


def register_pipelines() -> Dict[str, Pipeline]:
    data_processing_pipeline = dp.create_pipeline()
    return {"__default__": data_processing_pipeline}
