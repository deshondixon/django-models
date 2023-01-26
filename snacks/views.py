from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

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
