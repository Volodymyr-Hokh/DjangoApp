from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Record, Tag
from .forms import RecordForm


def main(request, page=1):
    records = Record.objects.all()

    per_page = 10
    paginator = Paginator(list(records), per_page)
    records_on_page = paginator.page(page)

    context = {"records": records_on_page}
    return render(request, "records/index.html", context)


@login_required
def add_record(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            tags = form.cleaned_data["tags"]
            tags = [tag.strip() for tag in tags.split(" ")]
            record = form.save(commit=False)
            record.user = request.user
            record.save()

            for tag_text in tags:
                tag = Tag.objects.get_or_create(name=tag_text)[0]
                record.tags.add(tag)
            return redirect("records:index")
    else:
        form = RecordForm()

    context = {"form": form}
    return render(request, "records/add_record.html", context)


def show_records(request, tag_name, page=1):
    records = Record.objects.filter(tags__name=tag_name)

    per_page = 10
    paginator = Paginator(list(records), per_page)
    records_on_page = paginator.page(page)

    context = {"records": records_on_page, "tag": tag_name}
    return render(request, "records/show_records.html", context)
