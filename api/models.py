from django.db import models

#class Acceso(models.Model):
#    nombreAula = models.CharField(max_length=200)
#    nombreProfesor = models.CharField(max_length=200)
#    password = models.CharField(max_length=20)
#    pub_date = models.DateTimeField('fecha de registro',auto_now=True)
STATUS_CHOICES = (
        ('libre', 'libre'),
        ('ocupado', 'ocupado'),
        
    )

class Zona(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class TipoAula(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Aula(models.Model):
    descripcion = models.CharField(max_length=50)
    
    zona = models.ForeignKey(Zona,on_delete=models.CASCADE)
    tipo_aula = models.ForeignKey(TipoAula,on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50 ,default='')
    fecha_nacimiento = models.DateTimeField('fecha...', null=True , blank=True)
    def __str__(self):
        return self.nombre
    


class Horario(models.Model):

    #dia= models.CharField(max_length=20, choices=STATUS_CHOICES_DIA ,default='lunes')
    fecha= models.DateField(null=True)
    hora_inicio = models.TimeField(null=True)
    hora_final = models.TimeField(null=True)
    estado = models.CharField(max_length=20, choices=STATUS_CHOICES, default='libre')
    aula = models.ForeignKey(Aula,on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.estado

class HorarioPersona(models.Model):
 
    horario = models.OneToOneField(Horario,on_delete=models.CASCADE , null=True)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE, null = True)
    password = models.CharField(max_length=50,null=True )

class User(models.Model):
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    
    def __str__(self):
        return self.username
