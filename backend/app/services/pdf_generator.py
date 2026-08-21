from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors


def generate_workout_pdf(workout, pdfFilters):
    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # -------------------------
    # Custom styles
    # -------------------------

    title_style = ParagraphStyle(
        "WorkoutTitle",
        parent=styles["Title"],
        fontSize=22,
        leading=26,
        alignment=TA_CENTER,
        spaceAfter=8
    )

    exercise_name_style = ParagraphStyle(
        "ExerciseName",
        parent=styles["Heading4"],
        fontSize=12,
        leading=14,
        spaceBefore=4,
        spaceAfter=2
    )

    description_style = ParagraphStyle(
        "Description",
        parent=styles["BodyText"],
        fontSize=8.5,
        leading=10,
        textColor=colors.grey,
        spaceAfter=2
    )

    details_style = ParagraphStyle(
        "Details",
        parent=styles["BodyText"],
        fontSize=9,
        leading=11,
        spaceAfter=5
    )

    footer_style = ParagraphStyle(
        "Footer",
        parent=styles["BodyText"],
        fontSize=7,
        leading=9,
        textColor=colors.grey,
        alignment=TA_CENTER,
        spaceBefore=10
    )

    content = []

    # -------------------------
    # Title
    # -------------------------

    content.append(
        Paragraph(
            pdfFilters.programName,
            title_style
        )
    )

    content.append(Spacer(1, 8))

    # -------------------------
    # Exercises
    # -------------------------

    for exercise in workout.exercises:

        content.append(
            Paragraph(
                exercise.Name,
                exercise_name_style
            )
        )

        if pdfFilters.showDescriptions:
            content.append(
                Paragraph(
                    exercise.Description,
                    description_style
                )
            )

        content.append(
            Paragraph(
                f"<b>{exercise.Sets} × {format_reps_type(exercise.RepsType, exercise.Reps)}</b> "
                f"/ {exercise.Rest}s rest",
                details_style
            )
        )

    # -------------------------
    # Footer
    # -------------------------

    content.append(
        Paragraph(
            "Made with Flag's Muscle Maker",
            footer_style
        )
    )

    document.build(content)

    buffer.seek(0)

    return buffer

def format_reps_type(repsType, reps):
    if repsType == "time":
        minutes = reps//60
        seconds = reps % 60
        if minutes == 0:
            return f"{seconds}s"
        elif seconds ==0:
            return f"{minutes}min"
        else:
            return f"{minutes}min {seconds}s"
    else:
        return reps
        



