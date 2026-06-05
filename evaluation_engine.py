def evaluate_answer(question, answer):

    if len(answer.strip()) == 0:
        return """
Score: 0/10

No answer provided.
"""

    elif len(answer) < 50:
        return """
Score: 5/10

Your answer is too short. Try adding more details and examples.
"""

    elif len(answer) < 150:
        return """
Score: 7/10

Good answer. Try providing more technical depth.
"""

    else:
        return """
Score: 9/10

Excellent answer. Well explained with sufficient detail.
"""