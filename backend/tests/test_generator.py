from app.services.generator import get_program_params, add_exercises_to_workout, generate_workout

def test_get_program_params():
    sets, reps, rest = get_program_params("activation_p", "strength")
    assert sets == 2
    assert reps == 1
    assert rest == 1.5

# def test_add_exercises_to_workout():
#     workout = []
#     exercises = [

#     ]