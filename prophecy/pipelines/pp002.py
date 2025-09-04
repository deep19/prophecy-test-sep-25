Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    t1 = Task(
        task_id = "t1", 
        component = "Dataset", 
        table = {"name" : "t1", "sourceType" : "Source", "sourceName" : "deeptanshu.default", "alias" : ""}
    )
