import re, pandas as pd, sqlalchemy as sa
from sqlalchemy import *

class scribbler:

    def read(self):
        print "Reading " + self.csv_file
        # try:
        if self.no_index_mode:
            self.df = pd.read_csv(self.csv_file)
        else:
            self.df = pd.read_csv(self.csv_file, index_col=False)
        if self.fill_na_mode:
            self.df = self.df.fillna("")
        print "Successfully read dataframe"
        # print self.df.dtypes
        # except:
        #     "Failed to read csv '" + self.csv_file + "'"
        print "Done"

    def create(self):
        print "Creating table " + self.table_name
        
        engine = create_engine(
                            "mysql+pymysql://"+ self.db_info["username"] + ":" +\
            self.db_info["password"] +"@"+ self.db_info["hostname"] + "/" +\
            self.db_info["database"])

        # try:
        self.df.to_sql(self.table_name,
                       engine,
                       if_exists=self.if_exists_mode,
                       dtype=self.custom_data_types)
        # except e:
        #     print "Unable to create table", e

    # if_exists = "fail" | "replace" | "append"  
    def __init__(self, db_conf, table, infile,
                 if_exists="fail",custom_dtypes={},fill_na=False,no_index=False):
        
        print "Making new object"

        self.db_info = db_conf
        self.csv_file = infile
        self.table_name = table
        self.if_exists_mode = if_exists
        self.custom_data_types = custom_dtypes
        self.fill_na_mode = fill_na
        self.no_index_mode = no_index
        
