from django.contrib import admin
from django import forms
from departments.models import *

# --- Custom Widget for Datalist Suggestions ---
class DatalistWidget(forms.TextInput):
    def __init__(self, datalist, list_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._datalist = datalist
        self._list_name = list_name

    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        attrs['list'] = self._list_name
        html = super().render(name, value, attrs, renderer)
        datalist_html = f'<datalist id="{self._list_name}">'
        for item in self._datalist:
            datalist_html += f'<option value="{item}">'
        datalist_html += '</datalist>'
        return html + datalist_html

class CurriculumDocumentForm(forms.ModelForm):
    class Meta:
        model = CurriculumDocument
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        PROGRAM_SUGGESTIONS = [
            "B.Tech (Computer Science & Engineering)",
            "B.Tech (Data Science)",
            "B.Tech (CSBS)",
            "B.Tech (Electronics & Communication)",
            "B.Tech (VLSI)",
            "B.Tech (Electrical & Electronics)",
            "B.Tech (Mechanical)",
            "B.Tech (Civil)",
            "M.Tech",
            "MBA",
            "MCA",
            "B.Tech",
        ]
        SEMESTER_SUGGESTIONS = [
            "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S1&S2"
        ]
        
        if 'program' in self.fields:
            self.fields['program'].widget = DatalistWidget(
                datalist=PROGRAM_SUGGESTIONS, 
                list_name="program_list",
                attrs={'class': 'vTextField'} # Keep Django admin styling
            )
        if 'semester' in self.fields:
            self.fields['semester'].widget = DatalistWidget(
                datalist=SEMESTER_SUGGESTIONS, 
                list_name="semester_list",
                attrs={'class': 'vTextField'}
            )

# Register your models here.
admin.site.register(DepHero)
admin.site.register(POES)
admin.site.register(POS)
admin.site.register(WKS)
admin.site.register(PSOS)
admin.site.register(Vission)
admin.site.register(Mission)
admin.site.register(DepUpdates)
admin.site.register(ProfessionalBodies)
admin.site.register(ProfessionalBodiesTeamMembers)
admin.site.register(ProfessionalBodiesEvents)
admin.site.register(SyllabusPDFS)
admin.site.register(Handouts)
admin.site.register(Laboratories)
admin.site.register(Achivements)
admin.site.register(Events)
admin.site.register(ExtraEvents)
admin.site.register(Contact)
admin.site.register(DepAbout)
admin.site.register(NewsLetters)
admin.site.register(Magazines)
admin.site.register(Associations)
admin.site.register(AssociationsEvents)
admin.site.register(AssociationTeamMembers)
admin.site.register(Objectives)
admin.site.register(InnovativeTLM)
admin.site.register(TLM_table)
admin.site.register(DAB)
admin.site.register(DabTable)
admin.site.register(PAC)
admin.site.register(PacTable)
admin.site.register(Streams)
admin.site.register(StreamComm)
admin.site.register(Students)
admin.site.register(AchievementTables)
admin.site.register(Econtent)
admin.site.register(Products)
admin.site.register(Mooc_courses)
admin.site.register(Fdps)
admin.site.register(Social_activities)
admin.site.register(Holistics)
admin.site.register(Higher)
admin.site.register(Placements)
admin.site.register(Activity)
admin.site.register(Alumni)
admin.site.register(ResearchAbout)
admin.site.register(Facultypdf)
admin.site.register(AutonomousCurriculum)


@admin.register(CurriculumDocument)
class CurriculumDocumentAdmin(admin.ModelAdmin):
    form = CurriculumDocumentForm
    list_display = ("title", "department", "syllabus_type", "program", "semester", "order")
    list_editable = ("order",)
    list_filter = ("department", "syllabus_type", "program")
    search_fields = ("title", "program", "semester")
    ordering = ("department", "syllabus_type", "program", "order", "semester")
    fieldsets = (
        (None, {
            "fields": ("department", "syllabus_type", "program", "semester", "title", "file", "order"),
        }),
    )