from django import forms


class ChangePasswordForm(forms.Form):
    current_password=forms.CharField(max_length=50,label="current password",widget=forms.PasswordInput(attrs={"placeholder":"Current Password","class":"form-control"}))
    new_password=forms.CharField(max_length=50,label="new password",widget=forms.PasswordInput(attrs={"placeholder":"New Password","class":"form-control"}))
    confirm_password=forms.CharField(max_length=50,label="confirm password",widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password","class":"form-control"}))