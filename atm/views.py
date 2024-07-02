from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction_type = form.cleaned_data['transaction_type']
            amount = form.cleaned_data['amount']
            Transaction.objects.create(transaction_type=transaction_type, amount=amount)
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transaction_create.html', {'form': form})
