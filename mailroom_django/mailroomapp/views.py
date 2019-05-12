# Create views here.
from django.shortcuts import render

import os


from django.shortcuts import render
from django.http import Http404
from mailroomapp.models import User, Donations, Donor
# from passlib.hash import pbkdf2_sha256
# from model import Donations, Donor, User


def donations_view(request):
    context = {'donations': Donations.objects.all()}
    return render(request, 'mrapp/donations.html', context)

def donate_view(request, name):
    try:
        donor = Donor.objects.get(pk=name)
    except Donor.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("name") == "name":
            all_donor = Donor.object.all()
            filter_donor = all_donor.filter(name__exact="name")
            donor = [(donor_name.name) for donor_name in filter_donor]
            donation = Donations.object.select_for_update().filter(value=request.form['value'], donor=donor)
            donation.save()

        context = {'donations': donations}
        return render(request, 'mrapp/donations.html', context)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
