from django.views.generic import DetailView, ListView
from .models import Snack


# Create your views here.
class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Bugles_brand_snack_food.jpg",
                "title": "Bugles",
                "description": "Bugles chips.",
                "reference_url": "https://en.wikipedia.org/wiki/Rake_(tool)"
            }, {
                "image_url": "https://i0.hippopx.com/photos/970/742/346/potato-french-fries-snacks-food-preview.jpg",
                "title": "Fries",
                "description": "Fries with cheese.",
                "reference_url": "https://en.wikipedia.org/wiki/Spoon"
            }, {
                "image_url": "https://live.staticflickr.com/3353/4643536339_040a11812c_b.jpg",
                "title": "Cookies",
                "description": "Chocolate Cookies.",
                "reference_url": "https://en.wikipedia.org/wiki/Spoon_(band)"
            },
        ]

        return context
