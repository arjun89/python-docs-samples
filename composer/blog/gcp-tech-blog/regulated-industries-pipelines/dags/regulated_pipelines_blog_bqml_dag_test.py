# Copyright 2021 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from airflow import models
import internal_unit_testing
import pytest

# user should substitute their project ID
PROJECT_ID = "you-project-id"
DATASET = "your-dataset-id"


@pytest.fixture(autouse=True, scope="function")
# The fixture `airflow_database` lives in ./conftest.py.
def set_variables(airflow_database):
    models.Variable.set("gcp_project_id", PROJECT_ID)
    models.Variable.set("bigquery_dataset", DATASET)
    yield
    models.Variable.delete("gcp_project_id")
    models.Variable.delete("bigquery_dataset")


def test_dag_import():
    from . import regulated_pipelines_blog_bqml_dag

    internal_unit_testing.assert_has_valid_dag(regulated_pipelines_blog_bqml_dag)