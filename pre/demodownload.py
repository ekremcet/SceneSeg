import os
import argparse
import os.path as osp
import shutil

from pytube import YouTube


def clean_prev_demo():
    if os.path.exists("../data/demo/"):
        shutil.rmtree("../data/demo/")


def main(yt_link):
    # clean the previous folders
    clean_prev_demo()
    os.makedirs("../data/demo", exist_ok=True)
    os.makedirs("../data/demo/video", exist_ok=True)
    video_save_path = "../data/demo/video"
    yt = YouTube(yt_link)
    yt.streams.get_highest_resolution().download(video_save_path)
    shutil.move(osp.join(video_save_path,os.listdir(video_save_path)[0]),osp.join(video_save_path,"demo.mp4"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass a YouTube link and it will be prepared")
    parser.add_argument("yt_link", help="YouTube link of demo video")
    args = parser.parse_args()
    yt_link = args.yt_link
    main(yt_link=yt_link)
