from django.db import models
from django.utils import timezone


class Cadastro(models.Model):
    """
    Esta classe cria o cadastro dos usuários
    """

    class Meta:
        verbose_name = 'Cadastro'
        verbose_name_plural = 'Cadastros'

    def __str__(self):
        return self.nome

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
        default=timezone.now,
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
    class Meta:
        verbose_name = 'Recarga'
        verbose_name_plural = 'Recargas'

    def __str__(self):
        return self.usuario.nome + ' - R$ ' + str(self.saldo_atual)

    usuario = models.ForeignKey(
        Cadastro,
        on_delete=models.CASCADE, blank=True, null=True,
    )
    data_recarga = models.DateField(
        'Data',
        default=timezone.now,
    )
    saldo_atual = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        default=0.0,
    )
    valor_recarga = models.DecimalField(
        'Valor da recarga',
        decimal_places=2,
        max_digits=6,
        default=0.0,
    )

    def save(self, *args, **kwargs):
        # Saldo atual <-- 100,00, adicionei valor da recarga mais 50,00, então o saldo atual deve ser 150,00
        self.saldo_atual = self.saldo_atual + self.valor_recarga
        super().save(*args, **kwargs)


class Utilizacao(models.Model):
    class Meta:
        verbose_name = 'Utilização'
        verbose_name_plural = 'Utilizações'

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
        default=0.0,
    )

    def save(self, *args, **kwargs):
        # Busque em recarga o usuário que eu escolhi em Utilização
        recarga = Recarga.objects.get(usuario=self.usuario)
        recarga.saldo_atual = recarga.saldo_atual - self.valor
        recarga.save()

        super().save(*args, **kwargs)
