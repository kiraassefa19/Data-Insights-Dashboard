from kedro.pipeline import Pipeline, node
from .nodes.load_data_nodes import load_data

from .nodes import (
    process_telegram_stats,
    process_playstore_reviews,
    process_app_downloads,
    process_telegram_growth,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                process_telegram_stats,
                inputs="telegram_stats_raw",
                outputs="telegram_stats_intermediate",
                name="process_telegram_stats_node",
            ),
            node(
                process_playstore_reviews,
                inputs="playstore_reviews_raw",
                outputs="playstore_reviews_intermediate",
                name="process_playstore_reviews_node",
            ),
            node(
                process_app_downloads,
                inputs="app_downloads_raw",
                outputs="app_downloads_intermediate",
                name="process_app_downloads_node",
            ),
            node(
                process_telegram_growth,
                inputs="telegram_growth_raw",
                outputs="telegram_growth_intermediate",
                name="process_telegram_growth_node",
            ),
        ]
    )
from .nodes import load_data_to_postgresql


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            # Other nodes...
            node(
              
                    load_data,
                    inputs=None,
                    outputs=["telegram_data", "banks_ad_data", "apollo_reviews"],
                    name="load_data_node",
                
            ),
        ]
    )
