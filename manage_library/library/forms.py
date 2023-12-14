from django import forms


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=255, required=True)
    lastname = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    phone = forms.CharField(max_length=11, required=True)
    nationalCode = forms.IntegerField()


class createBook(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    code = forms.CharField(max_length=255, required=True)


class createReservation(forms.Form):
    user_id = forms.IntegerField()
    book_id = forms.IntegerField()
    targetDay = forms.CharField(max_length=255)
