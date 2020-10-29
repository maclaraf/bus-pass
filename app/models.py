from django.db import models


class Cadastro(models.Model):
    """
    Esta classe cria o cadastro dos usuários
    """
    nome = models.CharField(
        'Usuário',
        max_length=40,
    )
    email = models.EmailField(
        'E-mail',
        max_length=40,
    )
    cpf = models.CharField(
        'CPF',
        max_length=11,
    )
    data_nasc = models.DateField(
        'Data de nascimento',
    )
    fone = models.CharField(
        'Telefone',
        max_length=11,
    )
    inst_ensino = models.CharField(
        'Instituição de Ensino',
        max_length=40,
    )
    numero_cadastro = models.CharField(
        'Cadastro Nº',
        max_length=7,
    )


class Recarga(models.Model):
    usuario = models.ForeignKey(
        Cadastro,
        on_delete=models.CASCADE, blank=True, null=True,
    )
    data_recarga = models.DateField(
        'Data',
    )
    saldo_atual = models.DecimalField(
        decimal_places=2,
        max_digits=6,
    )
    valor_recarga = models.DecimalField(
        'Valor da recarga',
        decimal_places=2,
        max_digits=6,
    )


class Utilizacao(models.Model):
    usuario = models.ForeignKey(
        Cadastro,
        on_delete=models.CASCADE, blank=True, null=True,
    )
    alters_data = models.DateField(
        'Data',
    )
    valor = models.DecimalField(
        'Valor',
        decimal_places=2,
        max_digits=6,
    )
