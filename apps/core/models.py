from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Documento(models.Model):
    TIPO = (
        ("", ""),
        ("Formulário", "Formulário"),
        ("Manual", "Manual"),
    )

    documento = models.CharField(max_length=255)
    upload = models.FileField(upload_to='', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    descricao = models.TextField('descrição', blank=True, null=True)
    tipo = models.CharField(choices=TIPO, max_length=255)
    criado = models.DateTimeField( 'criado em', auto_now_add=True, auto_now=False)
    modificado = models.DateTimeField( 'modificado em', auto_now_add=False, auto_now=True)

    class Meta :
        ordering = ['tipo','documento']

    def __str__(self):
        return f"{self.documento}"
