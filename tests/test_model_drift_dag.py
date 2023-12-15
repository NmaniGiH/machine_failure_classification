import unittest
from airflow.models import DagBag

class TestModelDriftDag(unittest.TestCase):

    def setUp(self):
        self.dagbag = DagBag(dag_folder="/dags", include_examples=False)

    def test_dag_loaded_successfully(self):
        self.assertFalse(
            len(self.dagbag.import_errors),
            f"DAG import errors: {self.dagbag.import_errors}"
        )

if __name__ == '__main__':
    unittest.main()
