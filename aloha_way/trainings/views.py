from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


class DashboardView(View):
    pass
    # def get(self, request):
    #     plan = Plan.objects.order_by('-created').first()
    #     recipe_plans = RecipePlan.objects.filter(plan_id=plan.id).all()
    #     return render(request, "dashboard.html", dict(
    #         recipes_count=Recipe.objects.all().count(),
    #         plans_count=Plan.objects.all().count(),
    #         day_names=DayName.objects.all().order_by('order'),
    #         last_added_plan=plan,
    #         recipe_plans=recipe_plans
    #     ))


class MainPage(View):
    pass
    # def get(self, request):
    #     recipes = Recipe.objects.all()
    #     array = []
    #     for recipe in recipes:
    #         array.append(recipe.id)
    #     shuffle(array)
    #     try:
    #         about = '/' + Page.objects.get(title='o aplikacji').slug
    #         contact = '/' + Page.objects.get(title='kontakt').slug
    #     except:
    #         about = "#about"
    #         contact = "#contact"
    #     try:
    #         recipe1 = Recipe.objects.get(id=array[0])
    #         recipe2 = Recipe.objects.get(id=array[1])
    #         recipe3 = Recipe.objects.get(id=array[2])
    #         resp = {
    #             "recipe1": recipe1,
    #             "recipe2": recipe2,
    #             "recipe3": recipe3,
    #             "about": about,
    #             "contact": contact,
    #         }
    #     except IndexError:
    #         empty = {
    #             "name": "Nie ma przepisów!",
    #             "description": "Wprowadź minimum 3 przepisy do bazy danych."
    #         }
    #         resp = {
    #             "recipe1": empty,
    #             "recipe2": empty,
    #             "recipe3": empty,
    #             "about": about,
    #             "contact": contact,
    #         }
    #     return render(request, 'index.html', resp)


class ContactView(View):
    pass
    # def get(self, request):
    #     try:
    #         contact = Page.objects.get(title='kontakt')
    #     except:
    #         contact = "#contact"
    #     description = contact.description.split('\r\n')
    #     title = contact.title.upper()
    #     return render(request, 'contact.html', {
    #         'title': title,
    #         'contact': description
    #     })


class AboutView(View):
    pass
    # def get(self, request):
    #     try:
    #         about = Page.objects.get(title='o aplikacji')
    #     except:
    #         about = "#about"
    #     slug= about.slug
    #     description = about.description.split('\r\n')
    #     title = about.title.upper()
    #     return render(request, slug + '.html', {
    #         'title': title,
    #         'contact': description
    #     })


class TrainerListView(View):
    pass
    # def get(self, request):
    #     recipeList = Recipe.objects.all().order_by("-votes", "-created")
    #     paginator = Paginator(recipeList, 50)
    #     page_number = request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)
    #     ctx = dict(page_obj=page_obj)
    #     if 'delete' in request.GET:
    #         recipe_id = request.GET['delete']
    #         recipe_plans = RecipePlan.objects.filter(recipe_id_id=recipe_id).distinct('plan_id')
    #         ctx['recipe_plans'] = recipe_plans
    #         if not recipe_plans:
    #             Recipe.objects.get(pk=recipe_id).delete()
    #         else:
    #             ctx['delete_error'] = True
    #     return render(request, 'app-recipes.html', ctx)


class StudentListView(View):
    pass
