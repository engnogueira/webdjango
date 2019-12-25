from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 381369324},
        'instalacao-windows': {'titulo': 'Video Aperitivo: Instalação Windows', 'vimeo_id': 381437493}
    }
    video = videos[slug]
    return render(request, "aperitivos/video.html", context={'video': video})
