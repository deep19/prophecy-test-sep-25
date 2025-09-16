Config = {"abc" : "'ogconf'"}
Schedule = Schedule(cron = "0 0/5 * * * ? *", timezone = "Asia/Kolkata")
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Config = Config, Schedule = Schedule, SensorSchedule = SensorSchedule):
    pp002__Limit_1 = Task(task_id = "pp002__Limit_1", component = "Model", modelName = "pp002__Limit_1")
    send_email_notification = Task(
        task_id = "send_email_notification", 
        component = "Email", 
        body = "asdadads", 
        subject = "Yo!!", 
        includeData = True, 
        fileName = "test.csv", 
        to = ["deeprtm3997@gmail.com"], 
        connection = Connection(kind = "smtp", id = "smtp_1"), 
        fileFormat = "csv", 
        hasTemplate = False
    )
    pp002__Limit_1.out_0 >> send_email_notification.in0
