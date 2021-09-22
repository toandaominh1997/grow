from typing import List

from fastapi import APIRouter, Depends

from polls import adapters
from polls.models import Question
from polls.schemas import FastQuestion, FastQuestions

router = APIRouter()


@router.get("/")
def get_questions(
    questions: List[Question] = Depends(adapters.retrieve_questions),
) -> FastQuestions:
    return FastQuestions.from_qs(questions)


@router.get("/{q_id}")
def get_question(
    question: Question = Depends(adapters.retrieve_question),
) -> FastQuestion:
    return FastQuestion.from_orm(question)


@router.get("/")
def get_choices(
    choices: List[Choice] = Depends(adapters.retrieve_choices),
) -> FastChoices:
    return FastChoices.from_qs(choices)


@router.get("/{c_id}")
def get_choice(choice: Choice = Depends(adapters.retrieve_choice)) -> FastChoice:
    return FastChoice.from_orm(choice)

