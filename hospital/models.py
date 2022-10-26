from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


Modalities=(
    (None, ' modalities'),
    ('CT','CT'),
    ('US','US'),
    ('MRI','MRI'),
    ('Mammogram','Mammogram'),
)

Study_part=(
    (None, 'Study_part'),
     ('Abdomen','Abdomen'),
     ('KUB','KUB'),
    ('OB less than 14 Weeks','OB less than 14 Weeks '),
     ('OB  more than 14 Weeks','OB more than 14 Weeks '),
    ('Brain','Brain'),
     ('Neck','Neck'),
    ('Chest','Chest'),
   
     ('pelvis','pelvis'),
     ('pan-CT','pan-CT'),
     
    ('thyroid','thyroid'),
     ('breast','breast'),
    ('scrotal','scrotal'),

     ('cervical spine','cervical spine'),
     ('L/S spine','L/S spine'),
    ('D/L spine','D/L spine'),

    ('doppler-venous-lower','doppler-venous-lower'),
    ('doppler-arterial-lower','doppler-arterial-lower'),
    ('doppler-venous-upper','doppler-venous-upper'),
    ('doppler-arterial-upper','doppler-arterial-upper'),
   
    
    ('all spine','all spine'),
     ('Shoulder','Shoulder'),
     ('elbow','elbow'),
       ('wrist&hand','wrist&hand'),
     ('hip','hip'),
       ('knee','knee'),
     ('ankle&foot','ankle&foot'),
       ('superficial-MSK','superficial-MSK'),
       
)

Side_label =(
     (None, 'Side_label'),
    ('right','right'),
    ('left','left'),
    ('all','all'),
)


Nationalty=(
    (None, 'Nationality'),
    ('Suadi','Suadi'),
    ('Non Suadi','Non Suadi'),
)

gender=(
    (None, 'gender'),
    ('Male','Male'),
    ('Female','Female'),
)



# doctor_name=(
#     (None, 'doctor_name'),
#     ('HAMID ALHADI','HAMID ALHADI'),
#     ('MOHAMED ALHADI','MOHAMED ALHADI'),
#     ('MOHMD A/GADER','MOHMD A/GADER'),
#     ('Pedia','Pedia'),
#     ('Ortho','Ortho'),
#     ('ENT','ENT'),
#     ('Opthalomo','Opthalomo'),
#     ('Others','Others'),
# ) 

Unit_name =(
    (None, 'Unit_name'),
    ('ER','ER'),
    ('pedia_ward','pedia_ward'),
    ('male_ward','male_ward'),
    ('female_ward','female_ward'),
    ('OB_ward','OB_ward'),
    ('L&D_ward','L&D_ward'),
    ('covid_ward','covid_ward'),
    ('OPD','OPD'),
    ('refferal','referral'),
    
) 

# departments=[
#     (None, 'departments'),
#      ('Surgery','Surgery'),
#     ('IMC','IMC'),
#     ('OBG','OBG'),
#     ('Pedia','Pedia'),
#     ('Ortho','Ortho'),
#     ('ENT','ENT'),
#     ('Opthalomo','Opthalomo'),
#     ('Cardiologist','Cardiologist'),
# ('Dermatologists','Dermatologists'),
# ('Radilogist','Radilogist'),
# ('Nursery',''),

# ]
STATUS_FLAG=(
    (None, 'STATUS_FLAG'),
    ('Top_Emergency','Top_Emergency'),
    ('Emergency','Emergency'),
    ('Routine','Routine'),
  

)



departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):
        user=models.OneToOneField(User,on_delete=models.CASCADE)
        profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
        address = models.CharField(max_length=40)
        mobile = models.CharField(max_length=20,null=True)
        department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
        status=models.BooleanField(default=False)
        
        @property
        def get_name(self):
            return self.user.first_name+" "+self.user.last_name
        @property
        def get_id(self):
            return self.user.id
        def __str__(self):
          return "{} ({})".format(self.user.first_name,self.department)



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)


    admitDate=models.DateField(auto_now=True,null=True)
    status=models.BooleanField(default=False)
    IdNumber=models.CharField(_('IdNumber') ,max_length=30 , null=True)
    date=models.DateField(default=timezone.now,null=True)
    time=models.TimeField(default=timezone.now,null=True )
    age = models.CharField(_('age'),max_length=30, null=True)
    gender = models.CharField(_('gender'), max_length = 10,choices=gender, null=True)
    Nationality  = models.CharField(_('Nationalty'), max_length = 10,choices=Nationalty, null=True)
    Unit_name = models.CharField(_('Unit_name'), max_length = 30,choices=Unit_name , null=True)
    flag = models.CharField(_('Flag'), max_length = 30,choices=STATUS_FLAG, null=True)
    Modalities = models.CharField(_('Modalities'), max_length = 30,choices=Modalities, null=True)
                
    Study_part = models.CharField(_('Study_part'), max_length = 30,choices=Study_part , null=True)
    Side_label = models.CharField(_('Side_label '), max_length = 30,choices=Side_label  , null=True)
    Other_study = models.CharField(_(' Other_study'),max_length=30, null=True)
    departments = models.CharField(_('departments'), max_length = 30,choices=departments, null=True)
    # doctor_name = models.CharField(_(' doctor_name '), max_length = 30,choices=doctor_name, null=True)
                
    clinical_indication = models.CharField(_(' clinical_indication '),max_length=300, null=True)
    provisional_diagnosis = models.CharField(_(' provisional_diagnosis '),max_length=100, null=True)
                
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


#Developed By : sumit kumar
#facebook : fb.com/sumit.luv
#Youtube :youtube.com/lazycoders
