Config = {"abc" : "'t1'"}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Config = Config, Schedule = Schedule, SensorSchedule = SensorSchedule):
    varabc_1 = Task(
        task_id = "varabc_1", 
        component = "Dataset", 
        table = {
          "name": "{{var('abc')}}", 
          "sourceType": "Table", 
          "sourceName": "deeptanshu.default", 
          "alias": "", 
          "additionalProperties": None
        }, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    s1 = Task(
        task_id = "s1", 
        component = "Dataset", 
        table = {"name" : "s1", "sourceType" : "Source", "sourceName" : "deeptanshu.default", "alias" : ""}
    )
    s2 = Task(
        task_id = "s2", 
        component = "Dataset", 
        table = {"name" : "s2", "sourceType" : "Source", "sourceName" : "deeptanshu.default", "alias" : ""}
    )
