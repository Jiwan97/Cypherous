from django.contrib import messages


def errors(request, form_data):
    err = None
    for i in form_data:
        r = i.label
        for error in i.errors:
            err = error
            messages.add_message(request, messages.ERROR,
                                 err.lower().replace("this", r).replace("field", "").capitalize())
            if err:
                break
        if err:
            break
