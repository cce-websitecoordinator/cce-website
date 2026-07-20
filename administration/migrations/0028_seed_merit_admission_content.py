from django.db import migrations


SCHEDULE_SLOTS = [
    ("July 21st", "CS-DS, CS-BS, EEE", 1),
    ("July 22nd", "ECE, VLSI, CS (Rank below 18000)", 2),
    ("July 23rd", "CS (Rank above 18000)", 3),
    ("July 24th", "ME, CE", 4),
]

ORIGINAL_DOCUMENTS = [
    "Print out of the data entry form",
    "Higher Secondary mark list",
    "Pass Certificate (CBSE / ISC)",
    "Allotment Memo (CEE)",
    "Candidate's Data Sheet (CEE)",
    "Fee Receipt",
    "10th Mark list & Certificate (CBSE / ICSE)",
    "Transfer & Conduct Certificates",
    "Equivalence Certificate (if applicable)",
    "Fitness Certificate",
    "Migration Certificate",
    "3 Passport Size Photos",
]

COPY_DOCUMENTS = [
    "10th Certificate (3 copies)",
    "HSE Mark list (3 copies)",
    "Aadhar (1 copy)",
]

DOCUMENT_NOTES = [
    "*Soft copy of 10th Certificate, 12th Certificate, Aadhar etc in pdf format for completing the data entry form.",
    "*Soft copy of photo and Signature in JPEG format for uploading in the portal*",
    "*Everyone must bring the originals of all the documents uploaded on the CEE Portal during the application process (e.g., Income certificate, Minority certificate, Birth certificate, etc.)*",
]

GENERAL_CONTACTS = [
    ("General Admission Queries", "9497707439", 1),
]

FORM_CONTACTS = [
    ("Form Assistance", "+91 94963 47313", 1),
    ("Form Assistance", "+91 96560 42842", 2),
]


def seed_data(apps, schema_editor):
    MeritAdmissionScheduleSlot = apps.get_model("administration", "MeritAdmissionScheduleSlot")
    MeritAdmissionDocument = apps.get_model("administration", "MeritAdmissionDocument")
    MeritAdmissionDocumentNote = apps.get_model("administration", "MeritAdmissionDocumentNote")
    MeritAdmissionBankDetail = apps.get_model("administration", "MeritAdmissionBankDetail")
    MeritAdmissionUniformFee = apps.get_model("administration", "MeritAdmissionUniformFee")
    MeritAdmissionFormLink = apps.get_model("administration", "MeritAdmissionFormLink")
    MeritAdmissionTutorial = apps.get_model("administration", "MeritAdmissionTutorial")
    MeritAdmissionContact = apps.get_model("administration", "MeritAdmissionContact")

    for date_label, departments, order in SCHEDULE_SLOTS:
        MeritAdmissionScheduleSlot.objects.create(
            date_label=date_label, departments=departments, order=order
        )

    for order, name in enumerate(ORIGINAL_DOCUMENTS, start=1):
        MeritAdmissionDocument.objects.create(type="original", name=name, order=order)

    for order, name in enumerate(COPY_DOCUMENTS, start=1):
        MeritAdmissionDocument.objects.create(type="copy", name=name, order=order)

    for order, text in enumerate(DOCUMENT_NOTES, start=1):
        MeritAdmissionDocumentNote.objects.create(text=text, order=order)

    MeritAdmissionBankDetail.objects.create(
        name="Christ College of Engineering (Autonomous) - ADMISSION FEE COLLECTION",
        account_no="924010069315255",
        ifsc_code="UTIB0000879",
        bank="Axis Bank",
        branch="Irinjalakuda",
        note="*Account should be added as beneficiary atleast 24 hour before for Bank transfer*",
    )

    MeritAdmissionUniformFee.objects.create(
        boys_fee="₹11,000", girls_fee="₹12,000", note="*Cash only*"
    )

    MeritAdmissionFormLink.objects.create(
        warning_1="To be filled in, upload all documents mentioned.",
        warning_2=(
            "No need for the submission of a new application for those who already "
            "submitted an application form for the Management/NRI quota admission process."
        ),
        form_url="https://christ.etlab.app/newregistration/default/signup?reg_type=1",
    )

    MeritAdmissionTutorial.objects.create(
        video_url="https://drive.google.com/file/d/1g5HrxfpJ2ZnLykTY2424Dw-B4e13s1EE/view?usp=drive_link"
    )

    for label, phone, order in GENERAL_CONTACTS:
        MeritAdmissionContact.objects.create(
            category="general", label=label, phone=phone, order=order
        )

    for label, phone, order in FORM_CONTACTS:
        MeritAdmissionContact.objects.create(
            category="form", label=label, phone=phone, order=order
        )


def unseed_data(apps, schema_editor):
    model_names = [
        "MeritAdmissionScheduleSlot",
        "MeritAdmissionDocument",
        "MeritAdmissionDocumentNote",
        "MeritAdmissionBankDetail",
        "MeritAdmissionUniformFee",
        "MeritAdmissionFormLink",
        "MeritAdmissionTutorial",
        "MeritAdmissionContact",
    ]
    for model_name in model_names:
        apps.get_model("administration", model_name).objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("administration", "0027_merit_admission_content_models"),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
