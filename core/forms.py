from django import forms
from django.core.mail import message
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto',max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        mail = EmailMessage(
            subject=assunto,
            body=mensagem,
            from_email=email,
            to=['contato@gmail.com',],
            headers={
                'reply_to':email
            }
        )

        mail.send()