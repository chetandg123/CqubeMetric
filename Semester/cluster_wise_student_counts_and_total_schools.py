import configparser
import time
import unittest
import pandas as pd
from Queries.test_query import TestQuery
from TS.reuse_func import cqube
from get_dir import pwd

p = pwd()
config = configparser.ConfigParser()
config.read(p.get_json_data_ini_path())

class Semester(unittest.TestCase):
    def setUp(self):
        con = cqube()
        self.connection = con.connect_to_postgres()

    def test_query(self):
        cluster = TestQuery()
        df1 = pd.read_sql_query(cluster.cluster_wise_semester, self.connection)
        df1 = df1[['cluster_name', 'students_count', 'total_schools']]
        df2 = pd.read_json(config['jsondata']['cluster_semester'])
        df2 = df2[['cluster_name', 'students_count','total_schools']]
        df_diff = pd.concat([df1, df2]).drop_duplicates(keep=False)
        assert df_diff.empty, "Found difference between s3 bucket metrics and the metrics generated outside cqube for cluster wise semester "
        print("No Difference between s3 bucket metrics and the metrics generated outside cqube for cluster wise semester ")

    def tearDown(self):
        self.connection.close()