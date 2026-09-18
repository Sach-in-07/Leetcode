class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[i])):
                image[i][j]=1-image[i][j]
        # print(image)
        return image
        