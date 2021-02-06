
# views.py

from app.signals import test_signal1, test_signal2

def service_view(request, service_code):
    service = get_object_or_404(Service, code=service_code)
    test_signal1_response = test_signal1.send(sender=Service, service=service, user=request.user)
    print('\ntest_signal1_response', test_signal1_response)
    test_signal2_response = test_signal2.send(sender=Service, arg2='s', arg3='as', service=service, user=request.user)
    print('\ntest_signal2_response', test_signal2_response)


# signals.py

from django.dispatch import Signal


test_signal1 = Signal(providing_args=["service", "user"])
test_signal2 = Signal(providing_args=["arg2", "arg3"])

# receivers.py

@receiver(test_signal1, sender=Service)
def test_receiver(sender, service, user, **kwargs):
    print('\ntest_receiver')
    print("sender: ", sender)
    print("kwargs: ", kwargs)
    return 'return'


@receiver(test_signal2, sender=Service)
@receiver(test_signal1, sender=Service)
def test_receiver2(sender, **kwargs):
    print('\ntest_receiver2')
    print("sender: ", sender)
    print("kwargs: ", kwargs)
    return 'return'


@receiver(test_signal2, sender=Service)
def test_receiver3(sender, arg2, arg3, **kwargs):
    print('\ntest_receiver3')
    print("sender: ", sender)
    print("kwargs: ", kwargs)
    return 'return'

