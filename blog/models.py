from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    
# titulo = models(...) cria o campo de texto para o titulo

# conteudo cria um campo de texto longo (sem max_length) para o corpo do post

#autor a chave estrangeira que liga o post ao usuario que o criou, on_delete=models.CASCADE significa que se o usuario for deletado, todos os posts dele serao deletados tambem

#data_criacao cria um campo de data e hora que é preenchido automaticamente (auto_now_add=True) quando o post é criado

#__str__ (self) define como o objeto sera representado como string, nesse caso retornando o titulo do post