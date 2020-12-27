from django.db import models

# Create your models here.
class ProjectCode(models.Model):
    pcode = models.CharField(db_column='PCODE', primary_key=True, max_length=4)  # Field name made lowercase.
    pname = models.CharField(db_column='PNAME', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_code'

class Todo_list(models.Model):
    no = models.AutoField(primary_key=True)  # auto_increment
    pcode = models.CharField(max_length=4)
    user_id = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    is_complete = models.BooleanField()
    priority = models.BooleanField()
    end_date = models.DateField()

    def todo_save(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'todo_list'

