from http import HTTPStatus
import pytest


@pytest.mark.asyncio
class TestQuestsAnswerAPI:
    async def test_create_and_get_question(self, async_client, test_user, faker):
        fake_text = faker.sentence()
        question_data = {"text": fake_text}
        response = await async_client.post("/api/v1/questions/", json=question_data)
        assert response.status_code == HTTPStatus.CREATED, f"Статус код создания вопроса не соответсвует {HTTPStatus.CREATED}"

        question = response.json()
        question_id = question["id"]
        assert question["text"] == fake_text, "Текст ответа не совпадает отправленному"

        response = await async_client.get(f"/api/v1/questions/")
        assert response.status_code == HTTPStatus.OK, f"Статус получение всех вопросов не соответсвует {HTTPStatus.OK}"

        response = await async_client.get(f"/api/v1/questions/{question_id}")
        assert response.status_code == HTTPStatus.OK, f"Статус код получения 1 вопроса не соответсвует {HTTPStatus.OK}"
        data = response.json()
        assert data["id"] == question_id, "Вопрос не соответсвует запрошенному"
        assert data["text"] == fake_text, "Текст ответа не совпадает отправленному"

        answer_ids = []
        for i in range(1, 6):
            answer_response = await async_client.post(
                f"/api/v1/questions/{question_id}/answers",
                json={"text": fake_text}
            )
            data = answer_response.json()
            assert data["question_id"] == question_id, "Вопрос не соответсвует запрошенному"
            assert data["text"] == fake_text, "Текст ответа не совпадает отправленному"

            assert answer_response.status_code == HTTPStatus.CREATED, f"Ответ {i} к вопросу {question_id} не создался"
            answer_ids.append(answer_response.json()["id"])

        del_response = await async_client.delete(f"/api/v1/questions/{question_id}")
        assert del_response.status_code == HTTPStatus.NO_CONTENT, "Не удалось удалить вопрос"

        for idx, a_id in enumerate(answer_ids, start=1):
            get_response = await async_client.get(f"/api/v1/answers/{a_id}")
            assert get_response.status_code == HTTPStatus.NOT_FOUND, f"Ответ {idx} не был удалён"
