from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_workout_pdf(workout):
    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(
        Paragraph("Muscle Maker", styles["Title"])
    )

    content.append(
        Paragraph("Workout Program", styles["Heading2"])
    )

    content.append(Spacer(1, 20))

    # Exercises
    for exercise in workout.exercises:

        content.append(
            Paragraph(
                exercise.Name,
                styles["Heading3"]
            )
        )

        content.append(
            Paragraph(
                exercise.Description,
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"{exercise.Sets} x "
                f"{exercise.Reps} "
                f"{exercise.RepsType}",
                styles["BodyText"]
            )
        )

        content.append(Spacer(1, 15))

    document.build(content)

    buffer.seek(0)

    return buffer