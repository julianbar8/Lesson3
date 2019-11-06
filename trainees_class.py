from trainers_class import *

class trainees(trainers):
    def __init__(self,trainee_id,name,age,trainer_stream,trainer_name):
        super().__init__(trainer_stream,trainer_name)
        self.trainee_id = trainee_id
        self.name = name
        self.age = age
        self.stream = trainer_stream
        self.trainer_name = trainer_name



Trainee1 = trainees(1,"Julian",24,"data","Isabella")
Trainee2 = trainees(2,"Leah",24,"data","Isabella")
Trainee3 = trainees(3,"Ibs",22,"data","Isabella")
Trainee4 = trainees(4,"Karam",22,"data","Isabella")
Trainee5 = trainees(5,"Jack",25,"data","Isabella")
Trainee6 = trainees(6,"Beth",21,"data","Isabella")
Trainee7 = trainees(7,"Daniel",27,"data","Isabella")
Trainee8 = trainees(8,"Maf",23,"data","Isabella")
Trainee9 = trainees(9,"Arun",21,"data","Isabella")
Trainee10 = trainees(10,"Sharim",24,"data","Isabella")

TraineeList = [Trainee1,Trainee2,Trainee3,Trainee4,Trainee5,Trainee6,
               Trainee7,Trainee8,Trainee9,Trainee10]

print(Trainee1.trainer_name)

