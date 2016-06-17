import bartlb, env

b = bartlb.scribbler (db_conf={ "username" : env.DB_USER,
                                "password" : env.DB_PASS,
                                "hostname" : env.DB_HOST,
                                "database" : env.DB_NAME},
                      table="table_name",
                      infile="data_file.csv",
                      if_exists="replace")

b.read()
b.create()
