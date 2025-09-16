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
    send_email_notification = Task(
        task_id = "send_email_notification", 
        component = "Email", 
        body = "asdadads", 
        subject = "Yo!!", 
        includeData = False, 
        fileName = "", 
        to = ["deeprtm3997@gmail.com"], 
        connection = Connection(kind = "smtp", id = "smtp_1"), 
        fileFormat = "", 
        hasTemplate = False
    )
    t1.out >> send_email_notification.in0
