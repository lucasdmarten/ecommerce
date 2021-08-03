'''
Tools used on accounts/views.py 
'''



def get_data(form, register=True):
    email = form.cleaned_data['email']
    if register:
        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        return {
        'username': username,
        'email': email,
        'password1': password1,
        'password2': password2,
        }
    else:  
        password = form.cleaned_data['password']
        return {
        'email': email,
        'password': password,
        }