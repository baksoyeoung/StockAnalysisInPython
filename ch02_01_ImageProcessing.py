import requests
import hashlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image

url = 'http://bit.ly/2JnsHnT'
r = requests.get(url, stream=True).raw

img = Image.open(r)
img.show()
img.save('src.png')
print(img.get_format_mimetype)

BUF_SIZE = 1024
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)

sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())

print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest()))

dst_img = mpimg.imread('dst.png')
print(dst_img)

pseudo_img = dst_img [:,:, 0]
print(pseudo_img)

plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1, 2, 1) #1행 2열의 행렬에서 첫번째 그림을 설정 하는 것
plt.title('Origina Image')
plt.imshow(mpimg.imread('src.png'))

plt.subplot(122) # 1행 2열의 영역에서 두 번째 영역으로 지정
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img [:, :, 0]  # 의사 색상 적용
plt.imshow(pseudo_img)
plt.show()
