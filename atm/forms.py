from django import forms

class TransactionForm(forms.Form):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]
    transaction_type = forms.ChoiceField(choices=TRANSACTION_TYPES)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
