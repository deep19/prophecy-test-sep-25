Config = {"abc" : "'t1'"}
Schedule = Schedule(cron = "0 0/2 * * * ? *", timezone = "Asia/Kolkata")
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Config = Config, Schedule = Schedule, SensorSchedule = SensorSchedule):
    t1 = Task(
        task_id = "t1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "t1", "sourceType" : "Table", "sourceName" : "deeptanshu.default", "alias" : ""}
    )
