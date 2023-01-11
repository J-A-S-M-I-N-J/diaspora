from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import Booking

# Create your views here.
def booking(request):
    """ A view to return the booking page, and sending a booking """
    
    if request.method == 'POST':
        form = Booking(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('emails/bookingform.html', {
                'name': name,
                'email': email,
                'message': message,
            })

            send_mail('The contact form subject', 'The contact form message', 'jasmin.juzbasic@gmail.com', ['jasmin.juzbasic@gmail.com'], html_message=html)
            return redirect('booking')
    else:
        form = Booking()
    return render(request, 'booking.html', {'Booking': form})
