from django.shortcuts import render

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Motivação', vimeo_id='381369324'),
    Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id='381437493'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, "aperitivos/indice.html", context={'videos': videos})


# noinspection PyUnresolvedReferences
def video(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, "aperitivos/video.html", context={'video': video})
