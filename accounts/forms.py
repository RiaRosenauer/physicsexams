from allauth.account.forms import SignupForm
from FSapp.models import Student


class MyCustomSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        Student.objects.create(user=user)
        print("")
        print("")
        print("")
        print("")
        print("")

        print("")
        print("test")
        # You must return the original result.
        return user