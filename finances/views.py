from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Case, When, Value, DecimalField
from django.db.models.functions import Coalesce
from .models import Category, Transaction
from .forms import CategoryForm, TransactionForm
from datetime import datetime


@login_required
def dashboard(request):
    today = datetime.today()
    current_month = today.month
    current_year = today.year

    transactions = Transaction.objects.filter(user=request.user)

    # Monthly summary
    monthly_summary = transactions.filter(
    date__year=current_year,
    date__month=current_month
).aggregate(
    total_income=Coalesce(
        Sum(
            Case(
                When(transaction_type='income', then='amount'),
                default=Value(0),
                output_field=DecimalField(max_digits=12, decimal_places=2)
            ),
            output_field=DecimalField(max_digits=12, decimal_places=2)
        ),
        Value(0),
        output_field=DecimalField(max_digits=12, decimal_places=2)
    ),
    total_expense=Coalesce(
        Sum(
            Case(
                When(transaction_type='expense', then='amount'),
                default=Value(0),
                output_field=DecimalField(max_digits=12, decimal_places=2)
            ),
            output_field=DecimalField(max_digits=12, decimal_places=2)
        ),
        Value(0),
        output_field=DecimalField(max_digits=12, decimal_places=2)
    ),
)


@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Category added!')
            return redirect('category_list')
    return render(request, 'category_list.html', {'categories': categories, 'form': form})


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    form = TransactionForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, 'Transaction added!')
            return redirect('transaction_list')
    return render(request, 'transaction_list.html', {'transactions': transactions, 'form': form})


@login_required
def dashboard(request):
    today = datetime.today()
    current_month = today.month
    current_year = today.year

    transactions = Transaction.objects.filter(user=request.user)

    monthly_summary = transactions.filter(
        date__year=current_year,
        date__month=current_month
    ).aggregate(
        total_income=Coalesce(
            Sum(
                Case(
                    When(transaction_type='income', then='amount'),
                    default=Value(0),
                    output_field=DecimalField(max_digits=12, decimal_places=2)
                ),
                output_field=DecimalField(max_digits=12, decimal_places=2)
            ),
            Value(0),
            output_field=DecimalField(max_digits=12, decimal_places=2)
        ),
        total_expense=Coalesce(
            Sum(
                Case(
                    When(transaction_type='expense', then='amount'),
                    default=Value(0),
                    output_field=DecimalField(max_digits=12, decimal_places=2)
                ),
                output_field=DecimalField(max_digits=12, decimal_places=2)
            ),
            Value(0),
            output_field=DecimalField(max_digits=12, decimal_places=2)
        ),
    )

    balance = monthly_summary['total_income'] - monthly_summary['total_expense']

    context = {
        'monthly_income': monthly_summary['total_income'],
        'monthly_expense': monthly_summary['total_expense'],
        'balance': balance,
        'recent_transactions': transactions[:5],
    }
    # ← The problem: missing return here!
        # ... all the code above ...

    context = {
        'monthly_income': monthly_summary['total_income'],
        'monthly_expense': monthly_summary['total_expense'],
        'balance': balance,
        'recent_transactions': transactions[:5],
    }

    return render(request, 'dashboard.html', context)   # ← Add this line!    