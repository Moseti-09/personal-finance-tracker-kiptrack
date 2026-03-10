from django.db import models
from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=20,
        choices=[('income', 'Income'), ('expense', 'Expense')],
        default='expense'
    )

    class Meta:
        unique_together = ['user', 'name', 'type']
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name} ({self.type})"

    def get_absolute_url(self):
        return reverse('category_list')


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_type = models.CharField(
        max_length=10,
        choices=[('income', 'Income'), ('expense', 'Expense')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.transaction_type} {self.amount} - {self.date}"

    def get_absolute_url(self):
        return reverse('transaction_list')