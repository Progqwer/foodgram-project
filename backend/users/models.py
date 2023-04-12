from django.contrib.auth.models import AbstractUser
from django.db import models

ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'

CHOICES = (
    (ADMIN, ADMIN),
    (MODERATOR, MODERATOR),
    (USER, USER),
)


class CustomUser(AbstractUser):
    username = models.CharField(
        verbose_name='Логин',
        max_length=200,
        unique=True,
        help_text='Укажите имя пользователя',
    )
    password = models.CharField(
        verbose_name=('Пароль'),
        max_length=150,
        help_text='Придумайте пароль',
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=200,
        unique=True,
        help_text='Укажите электронную почту'
    )
    first_name = models.CharField(
        verbose_name='Имя пользователя',
        max_length=200,
        help_text='Укажите своё имя',
    )
    last_name = models.CharField(
        verbose_name='Фамилия пользователя',
        max_length=200,
        help_text='Укажите свою фамилию',
    )
    registered = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True,
    )
    role = models.CharField(
        verbose_name='Статус пользователя',
        max_length=20,
        choices=CHOICES,
        default=USER
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return (
            self.role == ADMIN or self.is_staff
            or self.is_superuser
        )

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='uniq_follow',
            ),
        )

    def __str__(self):
        return f'{self.user} подписан на {self.author}'