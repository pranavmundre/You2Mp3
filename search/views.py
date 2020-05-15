from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
import youtube_dl
from youtube_dl import DownloadError
import re
import uuid
import os
from youtube_search import YoutubeSearch
import json
@csrf_exempt
def search(request):
    query=request.POST.get("query")
    result=str(uuid.uuid1()).split('-')[0]+".mp3"
    ydl_opts = {
    'format': 'bestaudio/bestaudio',
    'postprocessors': [{'key': 'FFmpegExtractAudio',
               'preferredcodec': 'mp3',
               'preferredquality': '192'}],
    'outtmpl': 'media/'+result,
    'quiet': False,
    'noplaylist':True,
    'ignoreerrors':True,
    'max-downloads':1,
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    try:
        title=(ydl.extract_info(query,download=False))['title']
    except youtbe_dl.utils.ExtractorError:
        return JsonResponse({"INVALID":"This mp3 is not available for download by you tube"},safe=False)
    title=re.sub('[\W_]+', '', str(title))+".mp3"
    try:
        ydl.download([query])
    except  youtube_dl.utils.DownloadError:
        print('Something went wrong!')
    except  youtube_dl.utils.UnavailableVideoError:
        return JsonResponse({"INVALID":"Mp3 format is not available for this song."},safe=False)
    except  youtube_dl.utils.GeoRestrictedError:
        return JsonResponse({"INVALID":"Song is not available in your country."},safe=False)
    except  youtube_dl.utils.YoutubeDLError:
        return JsonResponse({"INVALID":"Some error occured. Try again please."},safe=False)
    return JsonResponse({"fn":result,"sn":title},safe=False)
def autosuggest(request):
    data = request.GET.get("term")
    results = YoutubeSearch(''+data, max_results=5).to_json()
    mimetype = 'application/json'
    return HttpResponse(json.dumps(results), mimetype)