from django.http import StreamingHttpResponse
import time


def stream_response(request):
    words = ["это", "пример", "того", "как", "chatgpt", "нам", "отвечает"]

    return StreamingHttpResponse(
        stream_response_generator(words),
        # content_type="application/json"
    )

def stream_response_generator(words):
    for word in words:
        yield f"{word} "
        time.sleep(0.5)