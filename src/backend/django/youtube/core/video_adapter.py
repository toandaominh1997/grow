
from youtube.models import Video
from minio import Minio
from datetime import timedelta
from pathlib import Path
import youtube_dl


mo = Minio(
    "0.0.0.0:9000",
    access_key="adminminio",
    secret_key="adminminio",
    secure=False
)
class VideoAdapter(object):
    def __init__(self):
        pass
    def add_video(self, title, description= None, origin_url = None, s3_url = None):
        Video.objects.update_or_create(title = title, description=description, origin_url=origin_url, s3_url=s3_url)
    def search(self, origin_url):
        res = Video.objects.filter(origin_url=origin_url)
        s3_url = None
        if res.exists():
            print("Exist:", res)
            s3_url = res[0].s3_url
        else:
            res = self.download_video(origin_url)
            filename = res['filename'].split('/')[-1]
            mo.fput_object(bucket_name = 'mlops', object_name = f'video/{filename}', file_path = res['filename'])
            self.add_video(title = res['title'], description=res['description'], origin_url= origin_url, s3_url=f"video/{filename}")
            s3_url = f"video/{filename}"
        url = mo.get_presigned_url(
            "GET",
            "mlops",
            s3_url,
            expires=timedelta(hours=2),
        )
        return {"url": url}
    @staticmethod
    def download_video(url):
        root_path = Path.cwd().joinpath("video").joinpath("%(uploader)s/%(title)s.%(ext)s")
        dl_ops = {
          'outtmpl': str(root_path)
        }
        with youtube_dl.YoutubeDL(dl_ops) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return {"filename": filename, "title": info['title'], 'description': info['description']}
