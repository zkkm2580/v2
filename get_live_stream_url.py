import yt_dlp

def get_live_stream_url(youtube_url):
    try:
        # 配置yt-dlp选项
        ydl_opts = {
            'quiet': True,  # 静默模式，不输出多余信息
            'format': 'best',  # 获取最佳视频质量
            'extract_flat': True,  # 只提取视频信息，不下载
        }

        # 使用yt-dlp提取视频信息
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 获取视频信息
            info_dict = ydl.extract_info(youtube_url, download=False)
            
            # 提取直播流的 URL
            live_url = info_dict.get('url', None)
            
            if live_url:
                print(f"直播流地址: {live_url}")
            else:
                print("无法获取直播流地址")
    except Exception as e:
        print(f"发生错误: {e}")

# 示例：获取某个 YouTube 直播的流地址
youtube_live_url = "https://www.youtube.com/watch?v=vr3XyVCR4T0"  # 中天新闻台直播链接
get_live_stream_url(youtube_live_url)
