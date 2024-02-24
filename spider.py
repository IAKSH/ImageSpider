import argparse
from download_images_baidu import download_images
from remove_identical import delete_duplicates

parser = argparse.ArgumentParser(description='download images with keyword from image.baidu.com')
parser.add_argument('--keyword', type=str, required=True, help='the keyword of images that you are searching for')
parser.add_argument('--start_page', type=int, default=0, help='start downloading from this page')
parser.add_argument('--end_page', type=int, default=10, help='stop downloading after this page')
parser.add_argument('--delete_duplicates', type=bool, default=True, help='delete all duplicates automatically or not')
args = parser.parse_args()


download_images(args.keyword, args.keyword, args.start_page, args.end_page)
if args.delete_duplicates:
    delete_duplicates(f"./{args.keyword}")