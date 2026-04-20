from django import forms

class UserForm(forms.Form):
    username  = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email     = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), label="Confirm Password")

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned

class LoginForm(forms.Form):
    email    = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label="Password")

class CheckForm(forms.Form):
    name    = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email   = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message...', 'rows': 4}))
