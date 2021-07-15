from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name="index.html"
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = ""
        return ctxt

class AboutView(TemplateView):
    template_name="about.html"
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["number"] = 12
        ctxt["name"]= [
            "金城みなみ",
            "仲本愛香",
            "仲宗根香穂",
            "山城愛涼",
            "比嘉香月"]
        return ctxt

